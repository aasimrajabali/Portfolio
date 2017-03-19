class Ripple {
  int texture[];
  Ripple() {
    texture = new int[width * height];
  }
  //DISPLAY OF RIPPLE
  void display() {
    texture = pixels;
    for (int i = 0; i < pixels.length; i++) {
      pixels[i] = ripple[i];
    }
  }
  
}