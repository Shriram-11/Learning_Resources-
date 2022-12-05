
/*Design a class by name myCircle to model Circle geometrical object with its center and
radius that enables:
1. Initializing the center, radius and
2. Compute area, perimeter, and diameter of the circle object/s.

TASK 1: Identify member variable/s and their types
TASK 2: Identify Constructor/s along with their arguments (if any) to initialize the
member variables
TASK 3: Identify the methods along with their arguments and return types.
TASK 4: Identify member variable getters/setters (if needed) */
import java.util.*;

class circle {
    double rad, area, peri, dia;

    circle() {
        System.out.println("Enter radiuns of the circle:");
        Scanner a = new Scanner(System.in);
        rad = a.nextDouble();
    }

    void calc() {
        area = 3.14 * rad * rad;
        peri = 2 * 3.14 * rad;
        dia = 2 * rad;
    }

    void display() {
        System.out.println("Radius:" + rad + "\nDiameter:" + dia + "\nPerimeter:" + peri + "\nArea:" + area);
    }
}

public class tw2_1 {
    public static void main(String[] args) {
        circle c = new circle();
        c.calc();
        c.display();
    }

}
