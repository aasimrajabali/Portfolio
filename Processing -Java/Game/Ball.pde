class Ball {
  float xSpd;
  float ySpd;
  
  float x, y, spd, r;
  color c = color(255);
  
  Ball (float _x,float _y, float _r) {
    x = _x;
    y = _y;
    r = _r;
    spd = 0;
  }
  
  
  void change() { //whenever the player gets food
    r += 5;
  }
  
  void display() {
    fill(c);
    if (game == 2){
      fill(100,0,0);
    }
    noStroke();
    ellipse(x,y,r,r);
    fill(0,0,0,50);
    ellipse(x+2*xSpd, y+2*ySpd, r-25, r-25);
  }
  
  //KEY COMMANDS
  void keyPressed(){
    if (key == CODED){
      
      if (keyCode == UP) {
        y = y - 5;
        ySpd = -5;
        xSpd = 0;
        if (y <= 25){ //boundary line for the top
          y = 25;
        }
      }
      
      else if (keyCode == DOWN) {
        y = y + 5;
        ySpd = 5;
        xSpd = 0;
        if (y >= height -25) { //bottom line
          y = height - 25;
        }
      }
      
      if (keyCode == RIGHT){
        x = x + 5;
        xSpd = 5;
        ySpd = 0;
        if (x >= width - 25) {
          x = width - 25;
        }
      }
      
      if (keyCode == LEFT){
        x = x - 5;
        xSpd = -5;
        ySpd = 0;
        if (x <= 25) {
          x = 25;
        }
      }
      
    }
  }
  
  boolean intersect(Food a) {
    float dist = dist(x,y,a.x,a.y);
    
    //compare distance to the sum of radii of food and player
    if (dist < r - a.r) {
      return true;
    }
    else {
      return false;
    }
  }
  
  boolean collides (Enem b) {
     float dist = dist(x,y,b.x,b.y);
     
     if (dist < (r/2 + b.r/2)) {
       b.xSpd = 0;
       b.ySpd = 0;
       return true;
     }
     else { return false; }
  }
  
}