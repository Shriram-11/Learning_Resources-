import java.util.*;

public class tw1_1 {
    public static void main(String[] args) {

        // int[][] dat = new int[6][12];
        int[][] dat = { { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 }, { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 },
                { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 }, { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 },
                { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 }, { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 } };

        String[] car = { "Pagani", "Porsche", "Rimac", "Koeinegsegg", "Ferrari", "Lamborghini" };
        Scanner a = new Scanner(System.in);
        System.out.println("Enter:");

        for (int i = 0; i < 6; i++) {
            System.out.println("Manufacturer " + car[i] + ":");
            for (int j = 0; j < 12; j++) {
                System.out.println("Enter sales in motnth " + (j + 1) + "");
                dat[i][j] = a.nextInt();
            }
        }

        int[] tot = total(dat);
        int[] max = Mx(dat);
        double[] avg = cavg(dat);
        double[] sd = SD(dat);

        int ch = 0;
        while (ch != 5) {
            System.out.println(
                    "Enter choices:\n 1.Find maximum sales of a manufacturer\n 2.Find total no. of cars sold by all manufacturer\n 3.Find average no. of cars sold by all manufacturer\n 4. Find standard deviation of sales of manufacturer\n 5.Exit\nEnter Choice:");
            ch = a.nextInt();
            if (ch == 1) {
                System.out.println(
                        "Choose manufacturer:\n1. Pagani\n2. Porsche\n3. Rimac\n4. Koeinegsegg\n5. Ferrari\n6.Lamborghini\nEnter code:");
                int c = a.nextInt();
                System.out.println("Manufacturer:" + car[c - 1] +
                        "\nMaximum cars sold in month " + month(max[c - 1])
                        + "\nUnits sold:" + dat[c - 1][c - 1]);
            } else if (ch == 2) {
                for (int i = 0; i < 6; i++) {
                    System.out.println(car[i] + ":" + tot[i] + " units");
                }
            } else if (ch == 3) {
                for (int i = 0; i < 6; i++) {
                    System.out.println(car[i] + ":" + avg[i] + " units");
                }
            } else if (ch == 4) {
                System.out.println(
                        "Choose manufacturer:\n1. Pagani\n2. Porsche\n3. Rimac\n4. Koeinegsegg\n5. Ferrari\n6.Lamborghini\nEnter code:");
                int c = a.nextInt();
                System.out.println("Manufacturer:" + car[c - 1] + "   Standard Deviation " +
                        sd[c - 1]);
            } else if (ch == 5) {
                break;
            } else {
                System.out.println("Invalid input");
            }
        }

    }

    static String month(int i) {
        String[] m = { "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                "November", "December" };
        return m[i - 1];
    }

    static int[] total(int[][] a) {
        int[] tot = new int[6];
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 12; j++) {
                tot[i] += a[i][j];
            }
        }
        return tot;
    }

    static double[] SD(int a[][]) {
        double[] avg = cavg(a);
        double[] sd = new double[6];
        double s = 0;
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 12; j++) {
                s += Math.pow(a[i][i] - avg[i], 2);
            }
            sd[i] = s;
            s = 0;
        }
        return sd;
    }

    static double[] cavg(int[][] a) {
        double[] avg = new double[6];
        int[] sum = total(a);
        for (int i = 0; i < 6; i++) {
            avg[i] = (double) sum[i] / 12;
        }
        return avg;
    }

    static int[] Mx(int[][] a) {
        int[] r = new int[6];
        int m;
        for (int i = 0; i < 6; i++) {
            m = a[i][0];
            for (int j = 1; j < 12; j++) {
                if (m < a[i][j]) {
                    m = a[i][j];
                }
            }
            r[i] = m;
        }
        return r;
    }
}
