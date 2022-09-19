public class HW_2_6 {
    public static void main(String[] args) {
        System.out.print("please input the distance of two citys in km: ");
        double z = HW_2_3.get_and_test_double();

        System.out.printf("the distance between two citys is %.2f meter or %.2f centimeters", z*1000, z*1000*100);
    }
}
