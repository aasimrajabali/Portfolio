//Small credit to 
//http://freespace.virgin.net/hugo.elias/graphics/x_water.htm
//for the concept

int size, radius, texture[], ripple_list[], ripple[], diameter;
Ripple ripple1;
//location indexes of each ripple being made
int index1, index2, index3;
boolean guiState1, guiState2, guiState3; //For multiple GUI functions
int i, a, b;
int intensity = 32;
PImage img, water1, water2; 
import ddf.minim.*;
Minim minim;
AudioPlayer background;
PFont font;
//String[] data;
String data[];


void setup() {
  
  minim = new Minim(this);
  background = minim.loadFile("water.mp3");
  //background.loop();
  font = createFont("Courier-New",32);
  textFont(font,32);
  
  data=loadStrings("Texture.txt");  
  img = loadImage("background.jpg");
  water1 = loadImage("water1.jpg");
  water2 = loadImage("water2.jpg");
  
  size(500, 500);
  frameRate(40);
  radius = 6; //radius of each ripple, works best with 3-10;
  //total size the ripple's spacing takes up; note how it goes beyond canvas size
  size = width * (height+2) * 2; 
  index1 = width;
  index2 = width * (height+3);
  ripple_list = new int[size];
  ripple = new int[width*height];
  texture = new int[width*height];
  ripple1 = new Ripple();
  diameter = 20;
  image(img, 0, 0);
  loadPixels();
  smooth();
  
  guiState1 = true; //start out with the welcome screen
  guiState2 = false; //main screen
  guiState3 = false; //help screen
}

void draw() {
  if (guiState1 == true){
    background.loop();
    background(water1);
    textAlign(CENTER);
    textSize(35);
    fill(155, 3, 255);
    text("WATER VISUALIZATION",250,40);
    textSize(20);
    text("Press 's' to Start",250,80);
    text("Press 'h' for Help",250,120);
  }
  
  if (guiState2 == true){ 
    image(img, 0, 0);
    fill(3, 255, 231);
    ellipse(mouseX, mouseY, diameter, diameter);
    loadPixels();
    texture = pixels;
    render();
    ripple1.display();
    updatePixels();
    fill(0);
    textAlign(CENTER);
    text(data[0],width/2,50);
    textAlign(LEFT);
    textSize(15);
    text("'m':MUTE SOUND, 'u':UNMUTE SOUND", 0, 460);
    text("'h':HELP",0,490);
    
    if (keyPressed == true && key == 'b'){ //enlarge the object, works best from 20-50
      diameter += 2;
      intensity += 32;
      if (diameter > 45){
        diameter = 45;
        intensity = 512;
      }
    }
    if (keyPressed == true && key == 'v'){ //shrink the object, works best from 20-50
      diameter -= 2;
      intensity -= 32;
      if (diameter < 20){
        diameter = 20;
        intensity = 32;
      }
    }
    
    if (keyPressed == true && (key =='m')){
      background.mute();
    }
    if (keyPressed == true && (key =='u')){
      background.unmute();
    }
    
  }
  
  if (guiState3 == true){
    image(water2, 0, 0);
    textAlign(CENTER);
    textSize(35);
    fill(155, 3, 255);
    text("WATER VISUALIZATION",250,40);
    textSize(15);
    text("The visualization is simple. Move the object",250,80);
    text("across the screen and watch the ripples form",250,110);
    text("for a soothing effect. You can even enlarge",250,140);
    text("or shrink the object, and thus increase or",250,170);
    text("decrease the ripple intensity using the 'v' and 'b' keys.", 250, 200);
    text("Press 's' to move to the visualization,",250,240);
    
    if (keyPressed == true && (key =='m')){
      background.mute();
    }
    if (keyPressed == true && (key =='u')){
      background.unmute();
    }
  }
}

//RIPPLE RENDER
void render() {
  if (guiState2 == true){
    i = index1;
    index1 = index2;
    index2 = i;
  
    i = 0;
    index3 = index1;
    for (int y = 0; y < height; y++) {
      for (int x = 0; x < width; x++) {
        //the function of data is to render the ripple 
        short data = (short)((ripple_list[index3-width]+ripple_list[index3+width]+ripple_list[index3-1]+ripple_list[index3+1])>>1);
        data -= ripple_list[index2+i];
        data -= data >> 5;
        ripple_list[index2+i]=data;
        //when date is 0, the ripple is still, and when it's a value the waves render
        data = (short)(1024-data);
        //boundary lines
        a = ((x-width)*data/1024)+width;
        b = ((y-height)*data/1024)+height;
        if (a >=width) {a = width - 1;}
        if (a<0) {a = 0;}
        if (b>=height) {b = height - 1;}
        if (b<0) {b = 0;}
  
        ripple[i] = texture[a+(b*width)];
        index3++;
        i++;
      }
    }
  }
}
void keyPressed(){
  if (key == 's'){
    guiState1 = false;
    guiState2 = true;
    guiState3 = false;
  }
  if (key == 'h'){
    guiState1 = false;
    guiState2 = false;
    guiState3 = true;
  }
}
void mouseMoved() {
  move(mouseX, mouseY);
}

//RIPPLE MOVING EFFECT
void move(int x, int y) {
  if (guiState2 == true){
    //traverse the entire area of the ripple using radius
    for (int j = y - radius; j < y + radius; j++) {
      for (int k = x - radius; k < x + radius; k++) {
        //if the mouse is outside the ripple area, create another ripple
        if (j>=0 && j<height && k>=0 && k<width) {
          ripple_list[index1+(j*width)+k] += intensity;   //the "intensity" of the ripple; works best with 128-512
        }
      }
    }
  }
}