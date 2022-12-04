/*
 * Given, score of first student is 60, 55 and 70 while score of the second
 * student is 80, 60 and 41. In the same way collect the score of another three
 * students. We can store the score of the two students in a 2D array having 5
 * rows and 3 columns. The rows will represent the student and the columns will
 * hold the score of the students.
 * Create a Score two dimensional array
 * Create a sum array
 * Create an average array
 * Compute sum
 * Compute average
 * Print the result
 */

import java.util.*;

public class tw1_3 {
    public static void main(String[] args) {
        int[][] marks = { { 60, 55, 70 }, { 80, 60, 41 }, { 0, 0, 0 }, { 0, 0, 0 }, { 0, 0, 0 } };
        Scanner a = new Scanner(System.in);
        for (int i = 2; i < 5; i++) {
            System.out.println("Enter marks if student" + (i + 1));
            for (int j = 0; j < 3; j++) {
                marks[i][j] = a.nextInt();
            }
        }
        double[] total = sum(marks);
        double[] avg = avg(total);
        for (int i = 0; i < 5; i++) {
            System.out.println("Student " + (i + 1) + "\nMarks:\nSubject 1" + marks[i][0] + "\nSubject 2" + marks[i][1]
                    + "\nSubject 3" + marks[i][2]
                    + "\nTotal score:" + total[i] + "\nAverage" + avg[i]);
        }
    }

    static double[] sum(int[][] a) {
        double[] tot = new double[10];
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 3; j++) {
                tot[i] += a[i][j];
            }
        }
        return tot;
    }

    static double[] avg(double[] a) {
        double[] av = new double[5];
        for (int i = 0; i < 5; i++) {
            av[i] = a[i] / 3;
        }
        return av;
    }

}
