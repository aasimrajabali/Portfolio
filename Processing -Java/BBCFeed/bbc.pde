XML rss;
int rectX, rectY;
boolean rectOver = false;
int state;

void setup(){
  rss = loadXML("http://feeds.bbci.co.uk/news/rss.xml?edition=us");
  size(1000,600);
  background(255);
  smooth();
  fill(0);
  noStroke();
  state = 0;
}

void draw(){
    rect(0,500, width, 100);
    XML[] des = rss.getChildren("channel/item/description");
    XML[] titles = rss.getChildren("channel/item/title");
    XML[] heading = rss.getChildren("channel/title");
    XML[] dates = rss.getChildren("channel/lastBuildDate");
    XML[] links = rss.getChildren("channel/item/link");
    
    if (state == 0){
      background(255);
      for (int i = 0; i < titles.length - 19; i++) {
        String description = des[i].getContent();
        String title = titles[i].getContent();
        String sub = title.substring(0,5);//for the VIDEO category
        String head = heading[0].getContent();
        String date = dates[0].getContent();
        String link = links[i].getContent();
        rectX = 120;
        rectY = 90 + (50*i);
        textAlign(LEFT);
        text(head, 100, 50);
        text(date, 100, 75);
        update(mouseX, mouseY);
        if (rectOver){
          fill(0);
          text(description, 120, 120+ 50*i);
          if (mousePressed){
            link(link);
          }
        }
        
        if (sub.equals("VIDEO")){ //if the link includes a video, it's blue. Otherwise, articles are green
          fill(255);
          rect(rectX, rectY, width, 10);
          fill(0, 102, 255);
          text(title, 120, 100+(50*i));
          fill(0);
        }
        
        else{
          fill(255);
          rect(rectX, rectY, width, 10);
          fill(0, 204, 0);
          text(title, 120, 100+(50*i));
          fill(0);
          //text(description, 100, 120 + (50*i));
        //text(sub, 100, 140 + (50*i));
        }
        rectOver = false;
     }
     if (keyPressed && keyCode == RIGHT){
        state = 1;
      }
    }
   
   if (state == 1){
     background(255);
     for (int i = 6; i < titles.length - 13; i++) {
        String description = des[i].getContent();
        String title = titles[i].getContent();
        String sub = title.substring(0,5);//for the VIDEO category
        String head = heading[0].getContent();
        String date = dates[0].getContent();
        String link = links[i].getContent();
        rectX = 120;
        rectY = 90 + (50*(i-5));
        textAlign(LEFT);
        text(head, 100, 50);
        text(date, 100, 75);
        update(mouseX, mouseY);
        if (rectOver){
          fill(0);
          text(description, 120, 120+ 50*(i-5));
          if (mousePressed){
            link(link);
          }
        }
        
        if (sub.equals("VIDEO")){ //if the link includes a video, it's blue. Otherwise, articles are green
          fill(255);
          rect(rectX, rectY, width, 10);
          fill(0, 102, 255);
          text(title, 120, 100+(50*(i-5)));
          fill(0);
        }
        
        else{
          fill(255);
          rect(rectX, rectY, width, 10);
          fill(0, 204, 0);
          text(title, 120, 100+(50*(i-5)));
          fill(0);
          //text(description, 100, 120 + (50*i));
        //text(sub, 100, 140 + (50*i));
        }
        rectOver = false;
     }
     if (keyPressed && keyCode == LEFT){
        state = 0;
      }
    }
   }
   


void update(int x, int y) {
  if ( overRect(rectX, rectY, width, 10) ) {
    rectOver = true;
  } 
  else {
    rectOver = false;
  }
}
boolean overRect(int x, int y, int width, int height) {
  if (mouseX >= x && mouseX <= x+width && 
      mouseY >= y && mouseY <= y+height) {
    return true;
  } else {
    return false;
  }
}