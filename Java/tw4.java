import java.util.*;

public class tw4 {
    public static void main(String[] args) {
        System.out.println("Permanent:");
        permanent a = new permanent();
        a.calc();
        a.display();
        System.out.println("Temp:");
        temp b = new temp();
        b.calc();
        b.display();

    }
}

class employee {
    String name, gender, address;
    double salary;
    int age;

    employee() {
        Scanner a = new Scanner(System.in);
        System.out.println("Name:");
        name = a.nextLine();
        System.out.println("Age:");
        age = a.nextInt();
        System.out.println("Gender:");
        gender = a.nextLine();
        gender = a.nextLine();
        System.out.println("Address:");
        address = a.nextLine();
        System.out.println("Basic salary:");
        salary = a.nextDouble();
    }
}

class permanent extends employee {
    double hra, da, it, gsal;

    permanent() {
        super();
    }

    void calc() {
        hra = (0.075 * salary);
        da = (0.75 * salary);
        it = (0.1 * salary);
        gsal = hra + da + it + salary;
    }

    void display() {
        System.out.println("Name:" + name + "\nAge:" + age + "\nGender" + gender + "\nAddress:" + address
                + "\nBasic Salary" + salary + "\nGross Salary:" + gsal);
    }

}

class temp extends employee {
    double gsal;
    String deg;
    int exp, hrs;

    temp() {
        super();
        Scanner a = new Scanner(System.in);
        System.out.println("Experience:");
        exp = a.nextInt();
        System.out.println("Degree:");
        deg = a.nextLine();
        deg = a.nextLine();
        System.out.println("Working hrs:");
        hrs = a.nextInt();
    }

    void calc() {
        if (deg.equals("BTECH")) {
            if (exp > 10) {
                gsal = salary + (hrs * 500);
            } else if (exp > 5 && exp <= 10) {
                gsal = salary + (hrs * 400);
            } else if (exp >= 1 && exp <= 5) {
                gsal = salary + (hrs * 300);
            }
        } else if (deg.equals("MTECH")) {
            if (exp > 10) {
                gsal = salary + (hrs * 1000);
            } else if (exp > 5 && exp <= 10) {
                gsal = salary + 700;
            } else if (exp >= 1 && exp <= 5) {
                gsal = salary + (hrs * 500);
            }
        } else if (deg.equals("PHD")) {
            if (exp > 10) {
                gsal = salary + (hrs * 1500);
            } else if (exp > 5 && exp <= 10) {
                gsal = salary + (hrs * 1200);
            } else if (exp >= 1 && exp <= 5) {
                gsal = salary + (hrs * 800);
            }
        }
    }

    void display() {
        System.out.println("Name:" + name + "\nAge:" + age + "\nGender" + gender + "\nAddress:" + address
                + "\nBasic Salary" + salary + "\nGross Salary:" + gsal);
    }

}
