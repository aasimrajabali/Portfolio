class Enem {
  float x, y; //spawn points
  float r; 
  float xSpd; //speed of enemies
  float ySpd; 
  
  Enem (){
    x = random(100, width - 200);
    y = random(100, height - 200);
    r = 20; 
    xSpd = 5;
    ySpd = 5;
  }
  
  void move(){
    x += xSpd;
    y += ySpd;
    if (x > width -10 || x < 10){ 
      xSpd *= -1; 
    } 
    if (y > width -10 || x <10) { 
      ySpd *= -1; 
    } 
  }
  
  void display(){
    fill(random(200,255),200,0);
    noStroke();
    rect(x,y,r,r,-10);
  }
  
}