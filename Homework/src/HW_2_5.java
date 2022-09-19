public class HW_2_5 {
    public static void main(String[] args) {
        System.out.println("please input x: ");
        double x = HW_2_3.get_and_test_double();
        System.out.println("please input y: ");
        double y = HW_2_3.get_and_test_double();
        System.out.println("please input z: ");
        double z = HW_2_3.get_and_test_double();

        System.out.println("(4x - 3y) / 2z = " + ((4*x - 3*y) / (2*z)));
    }
}
