import java.util.*;

public class tw3 {
    public static void main(String[] args) {
        mybankAccount c1 = new mybankAccount();
        c1.interest(3);
        c1.withdraw();
        c1.deposit();
        c1.display();
        /*
         * mybankAccount c2=new mybankAccount(10000,"raju","pta nhi","RD");
         * c2.interest(3);
         * c2.withdraw();
         * c2.deposit();
         * c2.display();
         * mybankAccount c3=new mybankAccount();
         * c3.interest(3);
         * c3.withdraw();
         * c3.deposit();
         * c3.display();
         */
    }
}

class mybankAccount {
    static int accno;
    double bal;
    String name, address, accType;

    mybankAccount(double b, String n, String add, String acct) {
        bal = b;
        name = n;
        address = add;
        accType = acct;
        accno++;
    }

    mybankAccount() {
        System.out.println("Enter details");
        Scanner in = new Scanner(System.in);
        System.out.println("Enter Name:");
        name = in.nextLine();
        System.out.println("Enter Address");
        address = in.nextLine();
        System.out.println("Enter Account Type:");
        accType = in.nextLine();
        System.out.println("Enter Initial Balance");
        bal = in.nextDouble();
        accno++;
    }

    void interest(int t) {
        double r = 0, si;
        if (accType.equals("SB")) {
            r = 5;
        } else if (accType.equals("RD")) {
            r = 6.5;
        } else if (accType.equals("FD")) {
            r = 7.65;
        } else {
            System.out.println("Invalid account type");
            return;
        }
        si = (bal * r * t) / 100;
        bal += si;
        System.out.println("New balance:" + bal);
    }

    void deposit() {
        double amt;
        Scanner a = new Scanner(System.in);
        System.out.println("Enter amount to be deposited:");
        amt = a.nextDouble();
        bal += amt;
        System.out.println("New balance:" + bal);
    }

    void withdraw() {
        double amt;
        Scanner a = new Scanner(System.in);
        System.out.println("Enter amount to be withdrawn:");
        amt = a.nextDouble();
        if (bal - amt <= 1000) {
            System.out.println("Insufficient balance");
        } else {
            bal -= amt;
            System.out.println("New balance:" + bal);
        }
    }

    void display() {
        System.out.println("Name:" + name + "\nAddress:" + address + "\nAccount Number:" + accno + "\nAccount Type:"
                + accType + "\nBalance" + bal);
    }
}
