
/*
 * A company has 10 zonal sales offices in four zones namely, North, East, West
 * and South. The company wants to organize the sales data of each of the office
 * in each zone and find answers to queries such as,
 * Which office has performed the highest sales in each zone?
 * What is the average sales done by all the offices in each zone?
 * Which office among each zone is the poorly office?
 * You are required to answer the following:
 * How do you organize the above data?
 * How do you provide answers to the above queries?
 */
import java.util.*;

public class tw1_4 {
    public static void main(String[] args) {
        String[] zones = { "North", "East", "West", "South" };
        int[][] sales = new int[4][10];
        int[][] s = { { 20, 25, 19, 15, 16, 19, 21, 18, 13, 33 }, { 20, 25, 19, 15, 16, 19, 21, 18, 13, 33 },
                { 20, 25, 19, 15, 16, 19, 21, 18, 13, 33 }, { 20, 25, 19, 15, 16, 19, 21, 18, 13, 33 } };
        Scanner a = new Scanner(System.in);
        for (int i = 0; i < 4; i++) {
            System.out.println(zones[i] + " Zone\n");
            for (int j = 0; j < 10; j++) {
                System.out.println("Sales in office" + (j + 1));
                sales[i][j] = a.nextInt();
            }
        }
        // double[] total = sum(sales);
        // double[] avg = avg(total);
        // int[] low = poor(sales);
        // int[] high = good(sales);
        double[] total = sum(s);
        double[] avg = avg(total);
        int[] low = poor(s);
        int[] high = good(s);
        for (int i = 0; i < 4; i++) {
            System.out.println("\n" + zones[i] + " Zone" + "\nTotal sales:" + total[i] + "\nAverage sales" + avg[i] +
                    "\nOffice with lowest sales" + (low[i] + 1) + "\nOffice with highest sales" + (high[i] + 1));
        }

    }

    static double[] sum(int[][] a) {
        double[] tot = new double[4];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 10; j++) {
                tot[i] += a[i][j];
            }
        }
        return tot;
    }

    static double[] avg(double[] a) {
        double[] av = new double[4];
        for (int i = 0; i < 4; i++) {
            av[i] = a[i] / 10;
        }
        return av;
    }

    static int[] poor(int[][] a) {
        int[] p = new int[4];
        for (int i = 0; i < 4; i++) {
            int min = a[i][0];
            for (int j = 0; j < 10; j++) {
                if (min > a[i][j]) {
                    min = j;
                }
            }
            p[i] = min;
            min = 0;
        }
        return p;
    }

    static int[] good(int[][] a) {
        int[] p = new int[4];
        for (int i = 0; i < 4; i++) {
            int max = a[i][0];
            for (int j = 0; j < 10; j++) {
                if (max < a[i][j]) {
                    max = j;
                }
            }
            p[i] = max;
        }
        return p;
    }

}
