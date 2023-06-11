
import java.util.*;

class Stack {
    int[] elem;
    int top, size;

    void initStack(int size) {
        elem = new int[size];
        this.size = size;
        top = -1;
    }

    void initStack(Stack another) {
        size = another.elem.length;
        elem = new int[size];
        top = -1;

        for (int i = 0; i < another.elem.length; i++) {
            elem[i] = another.elem[i];
        }
    }

    void initStack(int[] a) {
        top = -1;
        elem = new int[a.length];
        size = a.length;
        for (int i = 0; i < a.length; i++) {
            push(a[i]);
        }

    }

    boolean isFull() {
        if (top == size - 1) {
            return true;
        }
        return false;
    }

    boolean isEmpty() {
        if (top == -1) {
            return true;
        }
        return false;
    }

    void push(int a) {
        if (isFull()) {
            System.out.println("Overflow");
            return;
        }
        elem[++top] = a;
    }

    int pop() {
        if (isEmpty()) {
            System.out.println("Empty Stack");
        }
        return elem[top--];
    }

    void display() {
        for (int i = top; i >= 0; i--) {
            System.out.println(elem[i]);
        }
    }

}

public class tw5 {
    public static void main(String[] args) {
        Stack a = new Stack();
        a.initStack(5);
        a.push(10);
        a.push(20);
        a.push(30);
        a.push(40);
        a.push(50);

        Stack b = new Stack();
        b.initStack(a);

        Stack c = new Stack();
        int[] ar = { 1, 2, 3, 4, 5 };
        c.initStack(ar);
        System.out.println("Stcak A");
        a.display();
        System.out.println("Stcak B");
        b.display();

        System.out.println("Stcak C");
        c.display();
    }

}
