public class HW_2_8 {
    public static void main(String[] args) {
        System.out.print("please input the number of pounds in bag:");
        double pounds_in_bage = HW_2_3.get_and_test_double();
        System.out.printf("we approximate need %.2f bag for one metric tons", 2205 / pounds_in_bage);
    }
}
