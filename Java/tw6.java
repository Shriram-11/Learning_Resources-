import java.util.*;

interface  IsPrime{
    boolean isprime(int n);

}

class PrimeTester implements IsPrime{
    public boolean isprime(int n) {
        for(int i=2;i<n;i++)
        {
            if(n%i==0){
                return false;
            }
        }
        return true;
    }
}

class ImprPrimeTester implements IsPrime{
    public boolean isprime(int n) {
        for(int i=2;i<n/2;i++)
        {
            if(n%i==0){
                return false;
            }
        }
        return true;
    }
}

class FasterPrimeTester implements IsPrime{
    public boolean isprime(int n) {
        for(int i=2;i<Math.sqrt(n);i++)
        {
            if(n%i==0){
                return false;
            }
        }
        return true;
    }
}

class FastestPrimeTester implements IsPrime{
    public boolean isprime(int n) {
        for(int i=1;i<n-1;i++)
        {
            if(Math.pow(i,n-1)%n!=1){
                return false;
            }
        }
        return true;
    }
}

public class tw6 {
    public static void main(String[] args) {
        PrimeTester a=new PrimeTester();
        ImprPrimeTester b=new ImprPrimeTester();
        FasterPrimeTester c=new FasterPrimeTester();
        FastestPrimeTester d=new FastestPrimeTester();
        Scanner in=new Scanner(System.in);
        System.out.println("Enter No.:");
        int n=in.nextInt();
        System.out.println("\nPrime Tester");
        check(a.isprime(n));
        System.out.println("\nImpr Prime Tester");
        check(b.isprime(n));
        System.out.println("\nFaster Prime Tester");
        check(c.isprime(n));
        System.out.println("\nFastest Prime Tester");
        check(d.isprime(n));
    }
    static void check(boolean n){
        if(n){
            System.out.println("Is a Prime No.");
            return;
        }
        System.out.println("Not a prime no.");

    }

    
}
