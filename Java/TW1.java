import java.util.Scanner;

public class TW1 {
    public static void main(String[] args) {
        int[][] marks = new int[5][3];
        int[] total = new int[5];
        try (Scanner in = new Scanner(System.in)) {
            for (int i = 0; i < 5; i++) {
                System.out.println("Student" + (i + 1));
                for (int j = 0; j < 3; j++) {
                    marks[i][j] = in.nextInt();
                    total[i] = marks[i][j];
                }
            }
        }
        System.out.println("--");
        for (int i = 0; i < 5; i++) {
            System.out.println("Student:" + (i + 1));
            System.out.println("Total marks:" + total[i]);
            System.out.println("Average:" + computeAvg(marks[i][0], marks[i][1], marks[i][2]));
        }
    }

    static int computeAvg(int a, int b, int c) {
        int min = a;
        if (b < min)
            min = b;
        if (c < min)
            min = c;
        int sum = a + b + c - min;
        return (int) Math.ceil(sum / 2.0);
    }

}
