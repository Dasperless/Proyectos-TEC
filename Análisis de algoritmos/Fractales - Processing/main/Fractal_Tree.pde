public class FractalTree {

  FractalTree() {
  }
  void branch(float h, float n) {
    // Each branch will be 2/3rds the size of the previous one
    h *= 0.66;

    // All recursive functions must have an exit condition!!!!
    // Here, ours is when the length of the branch is 2 pixels or less
    if (h > 2) {
      pushMatrix();       // Save the current state of transformation (i.e. where are we now)
      rotate(n);          // Rotate by theta
      line(0, 0, 0, -h);  // Draw the branch
      translate(0, -h);   // Move to the end of the branch
      branch(h, n);       // Ok, now call myself to draw two new branches!!
      popMatrix();        // Whenever we get back here, we "pop" in order to restore the previous matrix state

      // Repeat the same thing, only branch off to the "left" this time!
      pushMatrix();
      rotate(-n);
      line(0, 0, 0, -h);
      translate(0, -h);
      branch(h, n);
      popMatrix();
    }
  }
}
