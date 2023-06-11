package practice;

/*
 * TW 2: Write a program to demonstrate the implementation of class and its member methods.
Design a class by name myTriangle to model a triangle geometrical object with three sides.
Include functions to:
● Initialize the three sides of triangle.
● Determine the type of triangle represented by the three sides (Equilateral/
Isosceles/ Scalene triangle).
● Compute and return the area of the triangle.
Note:
When three sides are given we use the following formula:
s=(a+b+c)/2;
area=sqrt(s*(s-a)*(s-b)*(s-c));
 */
//import java.util.*;

class myTriangle {
    double a, b, c;

    myTriangle(double p, double q, double r) {
        a = p;
        b = q;
        c = r;
    }

    void t_type() {
        if (a == b && b == c) {
            System.out.println("Equilateral Triangle");
        } else if ((a == b) || (b == c) || (a == c)) {
            System.out.println("Isoceles Triangle");
        } else {
            System.out.println("Scalene Triangle");
        }
    }

    double area() {
        double s = (a + b + c) / 2;
        double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
        return area;
    }
}

public class t_w_2 {
    public static void main(String[] args) {
        myTriangle t1 = new myTriangle(10.0, 10.0, 10.0);
        myTriangle t2 = new myTriangle(10.0, 10.0, 9.0);
        myTriangle t3 = new myTriangle(11.0, 12.0, 13.0);
        t1.t_type();
        System.out.println("Area:" + t1.area());
        t2.t_type();
        System.out.println("Area:" + t2.area());
        t3.t_type();
        System.out.println("Area:" + t3.area());
    }

}
