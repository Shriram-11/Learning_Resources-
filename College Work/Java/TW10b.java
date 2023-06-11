/* TW10b
Use lambda expressions to design a TaxCalculator interface 
which defines a single method calculateTax that takes in an 
income and returns a double. 
The tax amount based on the following criteria:

   Income <=50000 tax = income * 0.1
   Income >=50000 & <= 100000 tax = income * 0.2 
   Income >=50000 tax = income * 0.1

Determine if the tax amount is less than 1000.
 */

import java.util.function.Predicate;

interface TaxCalculator {
    double calculateTax(double income);
}

public class TW10b {
    public static void main(String[] args) {
        TaxCalculator taxCalculator = (double income) -> {
            if (income <= 50000) {
                return income * 0.1;
            } else if (income > 50000 && income <= 100000) {
                return income * 0.2;
            } else {
                return income * 0.3;
            }
        };

        Predicate<Double> isTaxLessThan1000 = (tax) -> tax < 1000;

        double[] incomes = { 30000, 60000, 80000, 100000, 150000 };
        for (double income : incomes) {
            double tax = taxCalculator.calculateTax(income);
            System.out.println(
                    "Income: " + income + "\nTax: " + tax + "\nLess than 1000: " + isTaxLessThan1000.test(tax) + "\n");
        }
    }
}
