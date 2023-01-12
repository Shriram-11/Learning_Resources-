import java.util.Arrays;
import java.util.*;

public class tw9 {
    public static void main(String[] args) {
        String a1,a2;
        Scanner a=new Scanner(System.in);
        System.out.println("Enter the first string:");
        a1=a.next().toLowerCase();
        a2=a.next().toLowerCase();
        checkAnagram(a1,a2);

    }
    static void checkAnagram(String s1  ,String s2){
        if(s1.length()!=s2.length()){
            System.out.println("The two strings are not of same length");
            return;
        }
        char[] c1=s1.toCharArray();
        char[] c2=s2.toCharArray();
        Arrays.sort(c1);
        Arrays.sort(c2);
        
        if(Arrays.equals(c1,c2)){

            System.out.println("The two strings are anagrams");
        }
        else{
            
            System.out.println("The two strings are not anagrams");
        }
    }
}
