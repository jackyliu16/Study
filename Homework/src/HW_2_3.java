import java.util.*;

public class HW_2_3 {
    static Scanner in = new Scanner(System.in);
    public static void main(String[] args){

        System.out.print("Please input a number :");
        double a = get_and_test_double(); 
        System.out.print("Please input a number :");
        double b = get_and_test_double();

        System.out.println("a + b = " + (a+b));
        System.out.println("a - b = " + (a-b));
        System.out.println("a * b = " + (a*b));
        System.out.println("a / b = " + ((int)a/(int)b));
        System.out.println("a % b = " + (a % b));

    }

    public static double get_and_test_double() {
        while ( !(in.hasNextDouble() || in.hasNextInt()) ) {
            System.out.print("Please input a number: ");
            in.next();
        }
        double ret;
        if (in.hasNextInt()) {
            ret = (double)in.nextInt(); 
        }
        else {
            ret = in.nextDouble();
        }
        return ret;
    }
}
