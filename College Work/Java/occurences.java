import java.util.*;

public class occurences {
    public static void main(String[] args) {
        String s = "cccbbbaaaddd";
        char[] a = s.toCharArray();
        Arrays.sort(a);
        String r = new String(a);
        System.out.println(r);
        int l = 0;
        for (int i = 0; i < r.length(); i = i + 0) {
            System.out.println("Occrence of" + a[i]);
            l = r.lastIndexOf(a[i]);
            System.out.println(":" + (l - i + 1));
            i = l + 1;

        }
    }
}
