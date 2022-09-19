public class HW_2_4 {
    public static void main(String[] args) {
        System.out.println("please input length of area: ");
        double length = HW_2_3.get_and_test_double();
        System.out.println("please input width of area: ");
        double width = HW_2_3.get_and_test_double();
        
        System.out.println("area: " + length * width);
    }
}
