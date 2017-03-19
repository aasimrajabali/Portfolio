int score;
int game; //3 versions: pregame, ingame, and game-over (PAUSE may be added later)

Ball player; //you
Food food;//what you're trying to collect
Enem enem1;
Enem enem2; 
Enem enem3;

void setup(){
  size(700,700); //the canvas contains the character, so there are boundaries
  smooth();
  rectMode(CENTER);
  ellipseMode(CENTER); //spawnpoint of the character
  
  //PREGAME//
  game = 0; //starts of in pregame state
  player = new Ball(300,250,50);
  food = new Food();
  enem1 = new Enem();
  enem2 = new Enem();
  enem3 = new Enem();
  score = 0;
}

void draw(){
  background(0);
  
  //PREGAME//
  if (game == 0){
    fill(255);
    rect(175,65,370,70,7);
    fill(255);
    rect(250,145,500,50,7);
    fill(0);
    textSize(40);
    text("Collect the Food", 30, 85);
    textSize(40);
    text("Press Any Key to Start", 30, 157);
    if (keyPressed){
      game = 1; //go into in-game
    }
  }
  
  //IN-GAME//
  if (game == 1){ 
    fill(255); 
    textSize(50); 
    text(score, 330, 85); 
    if (player.intersect(food)){ //if you grab the food
      score++; 
      player.change(); //expand the player
      food.reset();  //spawn the food in a random part of the canvas
    } 
    
    if (player.collides(enem1) || player.collides(enem2) || player.collides(enem3)){ 
      game = 2; //if there's contact with an enemy, it's game-over
    }
  } 
  
  //GAME-OVER// 
  if (game == 2){ 
    keyCode = 0; 
    
    fill(255); 
    textSize(50); 
    text("Score:",20, 85); 
    text(score, 290, 85); 
    textSize(30); 
    text("Retry?", 20, 157); 
    textSize(30); 
    text("Press R to Restart", 20, 225); 
    fill(0); 
    if (keyPressed && key == 'r') { 
      game = 0; 
      setup(); 
      game = 1;
    } 
   }
   
  if (game == 3){ 
    keyCode = 0; 
     
    fill(255); 
    textSize(50); 
    text("Score:",20, 85); 
    text(score, 290, 85); 
    textSize(30); 
    text("You Win!", 20, 157); 
    textSize(30); 
    text("Press R to play Again", 20, 225); 
    fill(0); 
    if (keyPressed && key == 'r') { 
      game = 0; 
      setup(); 
      game = 1;
    } 
   }
  if (score == 15){
    game = 3;
  }
  
  /*if (game == 4){ 
    keyCode = 0; 
    
    fill(255); 
    textSize(50); 
    text("Paused",20, 85); 
    text(score, 290, 85); 
    textSize(30); 
    text("Press p to Resume", 20, 150); 
    fill(0); 
    if (keyPressed && key == 'p') { 
      game = 1; 
    } 
   }
  if (keyPressed  && key == 'p'){ //PAUSE
    game = 4;
  }*/
  
  player.display();
  player.keyPressed();
  food.display();
  enem1.move();
  enem2.move();
  enem3.move();
  enem1.display();
  enem2.display();
  enem3.display();
}