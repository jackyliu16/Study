public class HW_2_9 {
    public static void main(String[] args) {
        double jason_age = HW_2_3.get_and_test_double();
        double dany_age = jason_age + 4;
        double jack_age = dany_age / 2;
        System.out.printf("jack: %.1f, dany: %.1f", jack_age, dany_age);
    } 
}
