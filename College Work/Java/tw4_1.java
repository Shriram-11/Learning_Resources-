/*Design a base class called Employee who work for a Hospital and this class would
have name, dob, address, salary and designation as the attributes. Add a constructor to
initialize all these data members. This class would have reportForDuty method to display
reporting time and date with a “Welcome” message to the employee. Devise two derived
classes Doctor and Nurse to have expertise and yearsofExperience as data members
respectively. Devise a method performDuty in each of these derived classes to print
appropriate message depending on expertise of doctor and years of experience. For instance if
the experitise of the Doctor is Surgeon and yearsofExperience &gt;10 then print “Perform Heart
Operation” else perform “Perform minor Surgery”. If his expertise is orthopedic and
experience is more than 5 years “Perform surgery and Plastering” else “Perform Plastering”.
If the nurse has more than 3 years experience in performDuty method print “Check BP,
Sugar” and “Administer medicine” else print “Look after the patient”. Create a Hospital
Class that has main method, and instantiate objects of Doctor and Nurse and Perform
reportForDuty and performDuty and record the output. Add a static method
generateReport(Employee e) that accepts object of employee type and prints in a tabular
form, Name, dob, birthday salary and the designation. */

import java.util.*;
import java.util.Calendar;

class employee {
    String name, dob, address, desig;
    double sal;

    employee() {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter name");
        name = in.nextLine();
        System.out.println("Enter DOB");
        dob = in.nextLine();
        System.out.println("Enter address");
        address = in.nextLine();
        System.out.println("Enter Designation");
        desig = in.nextLine();
    }

    void reportforDuty() {
        Calendar cal = Calendar.getInstance();
        System.out.println("Welcome " + name + "\nDate and Time:" + cal.getTime());
    }

}

public class tw4_1 {

}
