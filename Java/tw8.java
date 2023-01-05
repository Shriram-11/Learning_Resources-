import java.util.*;

class UnderAgeException extends Exception{
    UnderAgeException(String s){
        super(s);
    }

    @Override
    public String toString(){
        return "Age should be > 18";
    }
    
}

class ValidDriversLicenseException extends Exception{
    ValidDriversLicenseException(String s){
        super(s);
    }
    
    @Override
    public String toString(){
        return "learners license not found";
    }
}

class AccidentCasesException extends Exception{
    AccidentCasesException(String s){
        super(s);
    }
    @Override
    public String toString(){
        return "Number of accidents in past one year must be 0";
    }
}

class License{
    String Name,gender;
    char vLr;
    int age,acc;

    License()
    {
        Scanner a = new Scanner(System.in);
        System.out.println("Name:");
        Name=a.nextLine();
        System.out.println("Age:");
        age=a.nextInt();
        System.out.println("Gender:");
        gender=a.nextLine();
        gender=a.nextLine();
        System.out.println("Do you have a valid learners license (Y/N)?:");
        vLr=a.next().charAt(0);
        System.out.println("No. of accidents in last one year:");
        acc=a.nextInt();
    }
}

public class tw8 {
    public static void main(String[] args) {
        License a=new License();
        validate(a);
        
    }

    static void validate(License l){
        try{

            if(l.age<18)
                throw new UnderAgeException("UnderAgeException");
            if(l.vLr != 'Y')
                throw new ValidDriversLicenseException("ValidDriversLicenseExceptiom");
            if(l.acc>0){
                throw new AccidentCasesException("NumberOfAccidentsException");
            }
            System.out.println("Congratulations!!!!! You will get the License");
        }

        catch(UnderAgeException e){
            System.out.println(e.getMessage()+e);
        }
        catch(ValidDriversLicenseException e){
            System.out.println(e.getMessage()+e);
        }
        catch(AccidentCasesException e){
            System.out.println(e.getMessage()+e);
        }
    }
}
