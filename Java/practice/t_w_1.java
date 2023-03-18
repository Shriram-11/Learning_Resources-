package practice;

/*
 * TW 1: Write a program to demonstrate the implementation of 2-dimension array.
Write a Java program to accept IA marks obtained by five students in three subjects. The
program should accept marks obtained by each student and display the total marks and the
average marks. The average marks is computed using a method as the average of best two
marks obtained
 */
import java.util.*;

public class t_w_1 {
    public static void main(String[] args) {
        Double[][] marks = new Double[5][3];
        Double[] total = new Double[5];
        Scanner a = new Scanner(System.in);
        for (int i = 0; i < 4; i++) {
            System.out.println("Student " + (i + 1) + ":");
            Double tot = 0.0;
            for (int j = 0; j < 3; j++) {
                System.out.println("Marks in Subject " + (j + 1) + ":");
                marks[i][j] = a.nextDouble();
                tot += marks[i][j];
            }
            total[i] = tot;
        }

        for (int i = 0; i < 4; i++) {
            System.out.println(
                    "Student " + (i + 1) + ":\n Total marks" + total[i] + "\n Average:" + computeAvg(marks[i]));
        }

    }

    static Double computeAvg(Double[] a) {
        Double min = a[0];
        if (a[1] < min) {
            min = a[1];
        } else if (a[2] < min) {
            min = a[2];
        }
        return ((a[0] + a[1] + a[2] - min) / 2);
    }
}
