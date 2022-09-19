import java.util.*;

public class HW_1_1 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        System.out.println("Enter Hours worked: ");
        int hour = -1, rate = -1;
        hour = in.nextInt();
        System.out.println("Enter hours rate: ");
        rate = in.nextInt();
        
        if ( hour == -1 || rate == -1 ) {
            System.out.println("input error !!!");
        }
        
        double count = 0.0;
        if ( hour >= 8 ) {
            count = 8.0 * rate + ( hour - 8 ) * 1.5 * rate;
        }
        else {
            count = hour * rate;
        }
        System.out.println("The daily wage of worker is: Rs." + count);

        in.close();
        
    }
}
