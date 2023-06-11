/*Write a Java program to define a class Lamp. It can be in on or off state. You can turn
on and turn off lamp (behavior). It makes use of class and its member methods.
Solution Approach:
Lamp class is created.The class has an instance variable isOn and three methods turnOn(),
turnOff() and displayLightStatus().
Two objects l1 and l2 of Lamp class are created in the main() function.
Here, turnOn() method is called using l1 object: l1.turnOn();
This method sets isOn instance variable of l1 object to true.
And, turnOff() method is called using l2 object: l2.turnOff();
This method sets isOff instance variable of l2 object to false.
Finally, l1.displayLightStatus(); statement displays Light on? true because isOn variable
holds true for l1 object.

And, l2.displayLightStatus(); statement displays Light on? false because isOn variable holds
false for l2 object */

class lamp {
    boolean isOn;

    void turnOn() {
        isOn = true;
    }

    void turnOff() {
        isOn = false;
    }

    void lightStatus() {
        if (isOn) {
            System.out.println("Light On");
            return;
        }
        System.out.println("Light Off");
    }
}

public class tw2_3 {
    public static void main(String[] args) {
        lamp l1 = new lamp();
        lamp l2 = new lamp();
        l1.turnOn();
        l2.turnOff();
        System.out.println("Lamp 1:");
        l1.lightStatus();
        System.out.println("Lamp 2:");
        l2.lightStatus();
    }
}
