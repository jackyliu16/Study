import java.util.*;
public class HW_2_7 {
    static int[] money_list = {100, 50, 10};
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("please input unpay number: ");
        while (!(in.hasNextInt())) {
            System.out.print("please input the number you want to pay: ");
            in.next();
        }
        int unpay_money = in.nextInt();

        dfs(0, unpay_money, new int[money_list.length]);
        in.close();
    }

    static void dfs(int step, int unpay, int[] pay_list) {
        if ( step >= money_list.length || unpay == 0 ) {
            if ( unpay == 0 ) {
                System.out.printf("you have to pay 100:%d, 50:%d, 10:%d\n", pay_list[0], pay_list[1], pay_list[2]);
            }
            return ;
        }
        for ( int i = 0 ; i <= unpay / money_list[step] ; i++ ) {
            pay_list[step] += i;
            dfs(step + 1, unpay - i * money_list[step], pay_list);
            pay_list[step] -= i;
        }
    }
}