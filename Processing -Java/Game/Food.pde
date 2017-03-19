class Food {
  float x, y; //spawn points
  float r; //size or radius of food
  
  Food (){
    x = random(100, width - 100);
    y = random(100, height - 100);
    r = 20;
  }
  
  void display(){
    fill(255);
    noStroke();
    ellipse(x,y,r,r);
  }
  
  void reset(){ //when the food is grabbed it needs to respawn randomly
    x = random(100, width - 100);
    y = random(100, height - 100);
  }
}