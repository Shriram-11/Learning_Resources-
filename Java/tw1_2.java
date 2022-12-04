/*
 A joint family consisting of 10 households lives in the same compound.  Due to mounting electricity bills, the head (Mr. X) 
of the joint family decides to analyze the consumption pattern 
(in terms of the billed amount) of each household for a year.   
 Mr. X needs access to the following information for his analysis:
The total expenditure on electricity consumption by each household in a year.
The maximum and minimum electricity consumption of each household in a year.
The amount by which each household exceeded the average consumption (+/-) of all households in the month of June.
The maximum, minimum and average electricity consumption of all households in a year.
Demonstrate how you would use a two dimensional matrix to help Mr. X. 

 */

import java.util.*;

public class tw1_2 {
    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        // double[][] dat = new double[10][12];
        double[][] dat = { { 1000, 1220, 1300, 1400, 1500, 1090, 1200, 1002, 1400, 1500, 1329, 991 },
                { 1010, 1221, 1300, 1400, 1500, 1090, 1200, 1002, 1400, 1500, 1329, 991 },
                { 1020, 1223, 1300, 1400, 1500, 1090, 1200, 1002, 1400, 1500, 1329, 991 },
                { 1030, 1224, 1300, 1400, 1500, 1090, 1200, 1002, 1400, 1500, 1329, 991 },
                { 1040, 1225, 1300, 1400, 1500, 1090, 1200, 1002, 1400, 1500, 1329, 991 },
                { 1050, 1261, 1300, 1400, 1500, 1090, 1200, 1002, 1400, 1500, 1329, 991 },
                { 1060, 1221, 1300, 1400, 1500, 1090, 1200, 1002, 1400, 1500, 1329, 991 },
                { 1070, 1220, 1300, 1400, 1500, 1090, 1200, 1002, 1400, 1500, 1329, 991 },
                { 1080, 1210, 1300, 1400, 1500, 1090, 1200, 1002, 1400, 1500, 1329, 991 },
                { 1090, 1210, 1300, 1400, 1500, 1090, 1200, 1002, 1400, 1500, 1329, 991 },
        };

        /*
         * for (int i = 0; i < 10; i++) {
         * System.out.println("Household " + (i + 1) + ":");
         * for (int j = 0; j < 12; j++) {
         * System.out.println("Enter consumption in " + month(j) + "");
         * dat[i][j] = a.nextInt();
         * }
         * }
         */
        double[] tot = total(dat);
        double[][] maxmin = MaxMin(dat);
        double[] d = delta(dat);
        for (int i = 0; i < 10; i++) {
            System.out.println("Household " + (i + 1));
            System.out
                    .println("Total consumption " + tot[i] + "\nMaximum consumption of electricity:" + maxmin[i][0]
                            + "\nMinimum consumption of electricity:" + maxmin[i][1] + "\nAverage consumption:"
                            + (tot[i] / 12) +
                            "\nThe amount household exceeded the average consumption (+/-) in june" + d[i]);
            System.out.println();
        }

    }

    static String month(int i) {
        String[] m = { "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                "November", "December" };
        return m[i - 1];
    }

    static double[] total(double[][] a) {
        double[] tot = new double[10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 12; j++) {
                tot[i] += a[i][j];
            }
        }
        return tot;
    }

    static double[][] MaxMin(double[][] a) {
        double[][] r = new double[10][2];
        double s, n;
        for (int i = 0; i < 10; i++) {
            n = s = a[i][0];
            for (int j = 1; j < 12; j++) {
                if (n < a[i][j]) {
                    n = a[i][j];
                }
                if (s > a[i][j]) {
                    s = a[i][j];
                }
            }
            r[i][0] = n;
            r[i][1] = s;
            n = s = 0;
        }
        return r;
    }

    static double[] delta(double[][] a) {
        double[] r = new double[10];
        double[] tot = total(a);
        for (int i = 0; i < 10; i++) {
            r[i] = (a[i][5] - (tot[i] / 12));
        }
        return r;
    }
}