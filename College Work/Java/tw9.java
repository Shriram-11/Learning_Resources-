import java.util.Arrays;
import java.util.*;

public class tw9 {
    public static void main(String[] args) {
        String a1, a2;
        try (Scanner a = new Scanner(System.in)) {
            System.out.println("Enter the first string:");
            a1 = a.next().toLowerCase();
            a2 = a.next().toLowerCase();
        }
        checkAnagram(a1, a2);

    }

    static char[] sort(char[] a) {
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a.length; j++) {

                if (a[i] > a[j]) {
                    char temp = a[i];
                    a[i] = a[j];
                    a[j] = temp;
                }

            }
        }
        return a;
    }

    static void checkAnagram(String s1, String s2) {
        if (s1.length() != s2.length()) {
            System.out.println("The two strings are not anagrams");
            return;
        }
        char[] c1 = s1.toCharArray();
        char[] c2 = s2.toCharArray();
        char[] c3 = sort(c1);
        char[] c4 = sort(c2);

        if (Arrays.equals(c3, c4)) {

            System.out.println("The two strings are anagrams");
        } else {

            System.out.println("The two strings are not anagrams");
        }

    }
}
