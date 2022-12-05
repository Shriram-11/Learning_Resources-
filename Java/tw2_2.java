
/*Define a class to represent the student details such as name, roll number, marks obtained
in three internal assessment tests.
a) Identify type and declare the instance variables
b) Identify and develop the constructors to initialize the instance variables
c) Write a method computeAverage() to compute the average as the average of best two
marks
d) Write a method to display the student details
Write the corresponding Driver class to instantiate an array of student objects and
demonstrate the working of the application by invoking appropriate methods.*/
import java.util.*;

class students {
    double a, b, c, avg;
    Scanner in = new Scanner(System.in);

    students() {
        System.out.println("Enter marks:");
        System.out.println("IA 1:");
        a = in.nextDouble();
        System.out.println("IA 2:");
        b = in.nextDouble();
        System.out.println("IA 3:");
        c = in.nextDouble();
    }

    void computeAvg() {
        double min = a;
        if (b < min) {
            min = b;
        }
        if (c < min) {
            min = c;
        }
        double sum = a + b + c - min;
        avg = sum / 2;
        System.out.println("Average: " + avg);
    }
}

public class tw2_2 {
    public static void main(String[] args) {
        students s = new students();
        s.computeAvg();
    }
}