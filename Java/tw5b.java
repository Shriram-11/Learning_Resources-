import java.util.*;

class Rectangle {
    double length, width;

    Rectangle() {
        length = 1.0;
        width = 1.0;
    }

    Rectangle(double l, double w) {
        length = l;
        width = w;
    }

    double computeArea() {
        return length * width;

    }

    double computePerimeter() {
        return 2 * (length + width);
    }
}

class cuboid extends Rectangle {
    double height;

    cuboid() {
        super();
        height = 1.0;
    }

    cuboid(double l, double w, double h) {
        super(l, w);
        height = h;
    }

    double computeArea() {
        double area = 2 * ((length * width) + (length * height) + (height * width));
        return area;

    }

    double computePerimeter() {
        double peri;
        peri = 4 * (length + width + height);
        return peri;
    }

    double computeVoulme() {
        return length * width * height;
    }
}

public class tw5b {
    public static void main(String[] args) {
        cuboid a = new cuboid(10, 10, 10);
        Rectangle c = new Rectangle(10, 10);
        System.out.println("Parameterised Constructor\nCuboid\nArea:" + a.computeArea() + " Perimeter:"
                + a.computePerimeter() + " Volume:" + a.computeVoulme() + "\nRectangle\nArea:" + c.computeArea()
                + " Perimeter" + c.computePerimeter());
        cuboid b = new cuboid();
        Rectangle d = new Rectangle();
        System.out.println("\nDefault Constructor\nCuboid\nArea:" + b.computeArea() + " Perimeter:"
                + b.computePerimeter() + " Volume:" + b.computeVoulme() + "\nRectangle\nArea:" + d.computeArea()
                + " Perimeter" + d.computePerimeter());
    }
}
