/*
import java.util.Arrays;

public class Dog{
    static double findBig(double a, String b){
        double B = Double.parseDouble(b);
        return Math.max(a, B);
    }
    static double findSmall(double a, String b) {
//        int A = Integer.parseInt(a);
        double B = Double.parseDouble(b);
        return Math.min(a, B);
    }
    static int compare(String a, String b){
        //  如果 a < b = -1 ;  a > b = 1 ; a == b = 0
        String[] A = a.split("-");
        String[] B = b.split("-");
        for(int i = 0; i < A.length ; i++){
            if (Integer.parseInt(A[i]) > Integer.parseInt(B[i])){
                return 1;
            }
            else if (Integer.parseInt(A[i]) < Integer.parseInt(B[i])){
                return -1;
            }
            else if (Integer.parseInt(A[i]) == Integer.parseInt(B[i])) {
                if (i != A.length - 1)
                    continue;
                else
                    return 0;
            }
            else{
                System.out.println("error in compare");
                return 0;
            }
        }
        System.out.println("out of index");
        return 0;
    }
    static boolean aInSection(String OneTime,String[] split,int sp){
        // insure a is in the section of sp and sp+1
        // 此时可以确保OneTime位于split (sp,sp+1] 的区间中
        if (sp <= split.length - 1)
            return (compare(OneTime, split[sp]) == 1) && (compare(OneTime, split[sp + 1]) != -1);
        else
            System.out.println("analyse out");
        return false;
    }
    static Double[][] analyse(String[][] a, String[] split) {
        Double[][] recode = new Double[split.length][4];
        // recode = {top,bottom,max,min}
        // recode =  0   1    2     3
        // a      = {Date,Open,High,Low,Close,Adj Close,Volume}
        // a      =   0    1     2   3    4      5        6
        int sp = 0;
        recode[0][0] = Double.parseDouble(a[1][1]);
        for ( int i = 0; i < a.length ; i++){
            if (sp != 0) {
                //

            }
            if (sp == 0){

            }
        }
    }

    public static void main(String[] args){
        // open     2603.300049     2578.199951     2536.899902     2553.300049
        // close    2590.800049     2533.899902     2524.000000     2553.300049
        //high      2614.899902     2578.199951     2536.899902     2553.300049
        // low      2561.699951     2449.899902     2484.399902     2553.300049
        String str =
                "Date,      Open,       High,       Low,        Close,      Adj Close,  Volume\n" +
                        "1987-01-08,2603.300049,2603.300049,2603.300049,2603.300049,2603.300049,0\n" +
                        "1987-01-09,2561.699951,2561.699951,2561.699951,2561.699951,2561.699951,0\n" +
                        "1987-01-12,2614.899902,2614.899902,2614.899902,2614.899902,2614.899902,0\n" +
                        "1987-01-13,2590.800049,2590.800049,2590.800049,2590.800049,2590.800049,0\n" +

                        "1987-01-14,2578.199951,2578.199951,2578.199951,2578.199951,2578.199951,0\n" +
                        "1987-01-15,2559.100098,2559.100098,2559.100098,2559.100098,2559.100098,0\n" +
                        "1987-01-16,2542.600098,2542.600098,2542.600098,2542.600098,2542.600098,0\n" +
                        "1987-01-19,2460.500000,2460.500000,2460.500000,2460.500000,2460.500000,0\n" +
                        "1987-01-20,2449.899902,2449.899902,2449.899902,2449.899902,2449.899902,0\n" +
                        "1987-01-21,2533.899902,2533.899902,2533.899902,2533.899902,2533.899902,0\n" +

                        "1987-01-22,2536.899902,2536.899902,2536.899902,2536.899902,2536.899902,0\n" +
                        "1987-01-23,2499.399902,2499.399902,2499.399902,2499.399902,2499.399902,0\n" +
                        "1987-01-26,2484.399902,2484.399902,2484.399902,2484.399902,2484.399902,0\n" +
                        "1987-01-27,2524.000000,2524.000000,2524.000000,2524.000000,2524.000000,0\n" +

                        "1987-01-28,2553.300049,2553.300049,2553.300049,2553.300049,2553.300049,0";

        int line = 0;// account the length of conter(line)
        String[] D1 = str.split("\n");
        String[][] D2 = new String[D1.length][7];
        for (int i = 0 ; i < D1.length ; i++){
            D2[i] = D1[i].split(",");
        }
        String[] split = {"1987-01-08","1987-01-14","1987-01-22","1987-01-28"};

//        System.out.print(aInSection("1987-01-20",split,0));
        Double[][] output = analyse(D2,split);

//        Draw(output);
        // print 2D array with |
        for (Double[] strings : output) {
            for (int j = 0; j < output[0].length; j++) {
                System.out.print(strings[j]);
                System.out.print("|");
            }
            System.out.println();
        }




    }
}
*/
