/*Design an abstract class Car to have carName, chassiNum, modelName as member
variables and add two abstract methods, startCar and operateSteering . Inherit MarutiCar and
BmwCar from Car class and override the two abstract methods in their own unique way.
Design a driver class to have driver name, gender and age as data members and add a method
driveCar with abstract class reference variable as argument and invoke the two basic
operations namely, startCar and operateStearing and demonstrate run-time polymorphism. */
abstract class Car {
    String name, model, chasisNum;

    Car(String a, String b, String c) {
        name = a;
        model = b;
        chasisNum = c;
    }

    abstract void StartCar();

    abstract void operatesteering();

    void show() {
        System.out.println("Car Name:" + name + "\nModel Name:" + model + "\nChassis No.:" + chasisNum);
    }
}

class BMW extends Car {
    BMW(String a, String b, String c) {
        super(a, b, c);
    }

    void StartCar() {
        System.out.println("BMW is starting");
    }

    void operatesteering() {
        System.out.println("The steering is sharp and powerful");
    }
}

class Maruti extends Car {
    Maruti(String a, String b, String c) {
        super(a, b, c);
    }

    void StartCar() {
        System.out.println("Car is starting");
    }

    void operatesteering() {
        System.out.println("The steering is not good");
    }
}

class Driver {
    String dn, gender;
    int age;

    Driver(String n, String g, int a) {
        dn = n;
        gender = g;
        age = a;
    }

    void drivecar(Car obj) {
        System.out.println("Name:" + dn + "\nGender" + gender + "\nAge:" + age);
        obj.show();
        obj.StartCar();
        obj.operatesteering();
    }
}

public class tw6 {
    public static void main(String[] args) {
        Car a = new Maruti("IGNIS", "1.6 L Petrol", "NOTSAFE01");
        Car b = new BMW("M5", "Touring V10", "BOND007");
        Driver d1 = new Driver("Buddha", "M", 19);
        d1.drivecar(a);
        Driver d2 = new Driver("Shriram", "M", 19);
        d2.drivecar(b);
    }
}
