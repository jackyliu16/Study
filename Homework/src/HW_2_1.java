import java.util.*;

public class HW_2_1 {
    public static int NUM_OF_SUM = 3;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] arr = new int[NUM_OF_SUM];
        for ( int i = 0 ; i < NUM_OF_SUM ; i++ ) {
            System.out.print("please input some kind of number to sum: ");
            while (! in.hasNextInt()) {
                System.out.print("please input a number !!!");
                in.next();
            }
            arr[i] = in.nextInt();
        }

        int sum = Arrays.stream(arr).sum();
        System.out.println("the sum of the arr you input is " + (float)sum / NUM_OF_SUM);

        in.close();
    }
}