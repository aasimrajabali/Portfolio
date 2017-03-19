PImage img;
PImage img_disp;
PImage buffer;
//GAUSSIAN BLUR MATRIX
float[][] kernel = {{ 0.0625, 0.125, 0.0625},
                    { 0.125, 0.25, 0.125},
                    { 0.0625, 0.125, 0.0625}};
//EDGE DETECTION MATRICES
float[][] Gx = {{ -1, 0, 1},
                { -2, 0, 2},
                { -1, 0, 1}};

float[][] Gy = {{ -1, -2, -1},
                { 0, 0, 0},
                { 1, 2, 1}};
                    
   

void setup(){
  surface.setResizable(true);
  img = loadImage("skyline.jpg");
  img_disp = loadImage("skyline.jpg"); //image to reset filters
  surface.setSize(img.width, img.height);
  frameRate(60);
}

void draw(){
  
  image(img, 0, 0);
  //GRAYSCALE
  if (keyPressed && key == '1') {
      loadPixels();
      img.loadPixels();
      for (int y = 0; y < height; y++){
        for (int x = 0; x < width; x++){
          int index = x + y*width;
          //functions red(), green(), and blue() pull out the 3 color components we need
          float r = red(img.pixels[index]);
          float g = green(img.pixels[index]);
          float b = blue(img.pixels[index]);
          //Image Processing for Grayscale
          float avg = (r + g + b)/3;
          pixels[index] = color(avg, avg, avg);
        }
      }
     
  }
  updatePixels();
  
  //HIGH CONTRAST 
   if (keyPressed && key == '2') {
      img = img_disp; //prevent filters from stacking
      image(img, 0, 0);
      loadPixels();
      img.loadPixels();
      for (int y = 0; y < height; y++){
        for (int x = 0; x < width; x++){
          int index = x + y*width;
          float r = red(img.pixels[index]);
          float g = green(img.pixels[index]);
          float b = blue(img.pixels[index]);
          //if the image brightness is below the threshold, decrease brightness values; if above, then increase values
          int threshold = 50;
          if (r < threshold || g < threshold|| b < threshold ){
            r -= 25;
            g -= 50;
            b -= 50;
          }
          else if (r > threshold || g > threshold|| b > threshold ){
            r += 50;
            g += 50;
            b += 25;
          }
          //make sure r, g, b are within the color range
          r = constrain(r, 0, 255);
          g = constrain(g, 0, 255);
          b = constrain(b, 0, 255);
          pixels[index] = color(r, g, b);
        }
      }
     
  }
  updatePixels();
  
  //GAUSSIAN BLUR 
  if (keyPressed && key == '3') {
    img = img_disp;
    image(img, 0, 0);
    loadPixels();
    img.loadPixels();
    for (int y = 1; y < img.height-1; y++) { // Skip top and bottom edges
      for (int x = 1; x < img.width-1; x++) { // Skip left and right edges, now all edges are untouched
        float r = 0; 
        float g = 0;
        float b = 0;
        for (int ky = -1; ky <= 1; ky++) {
          for (int kx = -1; kx <= 1; kx++) {
            // Calculate the adjacent pixel for specific kernel point
            int pos = (y + ky)*img.width + (x + kx);
            float val = red(img.pixels[pos]);
            float val2 = green(img.pixels[pos]);
            float val3 = blue(img.pixels[pos]);
            // Multiply adjacent pixels based on the kernel values
            r += kernel[ky+1][kx+1] * val;
            g += kernel[ky+1][kx+1] * val2;
            b += kernel[ky+1][kx+1] * val3;
          }
        }
        r = constrain(r, 0, 255);
        g = constrain(g, 0, 255);
        b = constrain(b, 0, 255);
        pixels[y*img.width + x] = color(r, g, b);
      }
    }
    updatePixels();
  }
      
  //EDGE DETECTION
  if (keyPressed && key == '4') {
    img = img_disp; 
    loadPixels();
    image(img, 0, 0);
    img.loadPixels();
    for (int y = 1; y < img.height-1; y++) { //same as Gaussian blur: ignore edges
      for (int x = 1; x < img.width-1; x++) { 
        float r1 = 0; 
        float g1 = 0;
        float b1 = 0;
        float r2 = 0; 
        float g2 = 0;
        float b2 = 0;
        for (int ky = -1; ky <= 1; ky++) {
          for (int kx = -1; kx <= 1; kx++) {
            int pos = (y + ky)*img.width + (x + kx);
            float val = red(img.pixels[pos]);
            float val2 = green(img.pixels[pos]);
            float val3 = blue(img.pixels[pos]);
            r1 += Gx[ky+1][kx+1] * val;
            g1 += Gx[ky+1][kx+1] * val2;
            b1 += Gx[ky+1][kx+1] * val3;
            r2 += Gy[ky+1][kx+1] * val;
            g2 += Gy[ky+1][kx+1] * val2;
            b2 += Gy[ky+1][kx+1] * val3;
          }
        }
        float r = sqrt(pow(r1,2) + pow(r2,2));
        float g = sqrt(pow(g1,2) + pow(g2,2));
        float b = sqrt(pow(b1,2) + pow(b2,2));
        r = constrain(r, 0, 255);
        g = constrain(g, 0, 255);
        b = constrain(b, 0, 255);
        pixels[y*img.width + x] = color(r, g, b);
      }
    }
    updatePixels();
  }
    
  //FILTER RESET
  if (keyPressed && key == '0') {
    img = img_disp;
    loadPixels();
    image(img, 0,0);
    img.loadPixels();
    for (int y = 0; y < height; y++){
        for (int x = 0; x < width; x++){
          int index = x + y*width;
          float r = red(img.pixels[index]);
          float g = green(img.pixels[index]);
          float b = blue(img.pixels[index]);
          pixels[index] = color(r, g, b);
        }
    }
  }
  updatePixels();
  

//FILTER 1: SEPIA TONE
  if (keyPressed && key == '5') {
    img = img_disp;
    image(img, 0,0);
    loadPixels();
    img.loadPixels();
    for (int y = 0; y < height; y++){
        for (int x = 0; x < width; x++){
          int index = x + y*width;
          float r = red(img.pixels[index]);
          float g = green(img.pixels[index]);
          float b = blue(img.pixels[index]);
          //SEPIA TONE FORMULA
          float newR = r * 0.393 + g * 0.769 + b * 0.189; 
          float newG = r * 0.349 + g * 0.686 + b * 0.168; 
          float newB = r * 0.272 + g * 0.534 + b * 0.131;
          if (newR > 255 ){newR = 255;}
          if (newG > 255){newG = 255;} 
          if (newB > 255){newB = 255;} 
          pixels[index] = color(newR, newG, newB);
          }
    }
  }
  updatePixels();

//FILTER 2: INVERT TONE
  if (keyPressed && key == '6') {
    img = img_disp;
    image(img, 0,0);
    loadPixels();
    img.loadPixels();
    for (int y = 0; y < height; y++){
        for (int x = 0; x < width; x++){
          int index = x + y*width;
          float r = red(img.pixels[index]);
          float g = green(img.pixels[index]);
          float b = blue(img.pixels[index]);
          //SEPIA TONE FORMULA
          float newR = 255 - r; 
          float newG = 255 - g; 
          float newB = 255 - b;
          
          pixels[index] = color(newR, newG, newB);
          }
    }
  updatePixels();
  }
  
  //FILTER 3: SOLARIZE
  if (keyPressed && key == '7') {
      img = img_disp; //prevent filters from stacking
      image(img, 0, 0);
      loadPixels();
      img.loadPixels();
      for (int y = 0; y < height; y++){
        for (int x = 0; x < width; x++){
          int index = x + y*width;
          float r = red(img.pixels[index]);
          float g = green(img.pixels[index]);
          float b = blue(img.pixels[index]);
          //if the image brightness is below the threshold, decrease brightness values; if above, then increase values
          int threshold = 100;
          if (r < threshold || g < threshold|| b < threshold ){
            r = 255 - r;
            g = 255 - g;
            b = 255 - b;
          }
          else if (r > threshold || g > threshold|| b > threshold ){
            r = 255 + r;
            g = 255 + g;
            b = 255 + b;
          }
          //make sure r, g, b are within the color range
          r = constrain(r, 0, 255);
          g = constrain(g, 0, 255);
          b = constrain(b, 0, 255);
          pixels[index] = color(r, g, b);
        }
      }
     
  }
  updatePixels();
  
 //FILTER 8: THRESHOLDING
 if (keyPressed && key == '8') {
      img = img_disp; //prevent filters from stacking
      image(img, 0, 0);
      loadPixels();
      img.loadPixels();
      for (int y = 0; y < height; y++){
        for (int x = 0; x < width; x++){
          int index = x + y*width;
          float r = red(img.pixels[index]);
          float g = green(img.pixels[index]);
          float b = blue(img.pixels[index]);
          //if the image brightness is below the threshold, decrease brightness values; if above, then increase values
          int threshold = 128;
          if (r < threshold || g < threshold|| b < threshold ){
            r = 0;
            g = 0;
            b = 0;
          }
          else if (r > threshold || g > threshold|| b > threshold ){
            r = 255;
            g = 255;
            b = 255;
          }
          //make sure r, g, b are within the color range
          r = constrain(r, 0, 255);
          g = constrain(g, 0, 255);
          b = constrain(b, 0, 255);
          pixels[index] = color(r, g, b);
        }
      }
     
  }
  updatePixels();
  
}

         