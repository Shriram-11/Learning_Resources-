@FunctionalInterface
interface Add {
    void add(int a, int b);
}

public class tw10 {
    public static void main(String[] args) {
        Add s = (a, b) -> {
            System.out.println(a + "+" + b + "=" + (a + b));
        };
        s.add(10,20);
    }
}