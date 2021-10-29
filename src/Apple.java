import java.util.Arrays;

public class Apple{
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
        // 此时可以确保OneTime位于split[sp,sp+1)的区间中
        // 注意： 需要修改成为(sp,sp+1]
        if (sp <= split.length - 1)
            return (compare(OneTime, split[sp]) != -1) && (compare(OneTime, split[sp + 1]) == -1);
        else
            System.out.println("analyse out");
            return false;
    }
    static Double[][] analyse(String[][] a, String[] split) {
        Double[][] recode = new Double[split.length - 1][4];
        // recode = {top,bottom,max,min}
        // recode =  0   1    2     3
        // a      = {Date,Open,High,Low,Close,Adj Close,Volume}
        // a      =   0    1     2   3    4      5        6
        int sp = 0;     // 指向
        // 对于第一项进行初始化操作
        recode[0][0] = Double.parseDouble(a[1][1]);
//        recode[0][1] = Double.parseDouble(a[1][4]);
        for( int i = 1; i < a.length ; i++){
/*            System.out.println("---------------Start----------------");
            System.out.println("i: " + i);
            for (Double[] strings : recode) {
                for (int j = 0; j < recode[0].length; j++) {
                    System.out.print(strings[j]);
                    System.out.print("|");
                }
                System.out.println();
            }
            System.out.println("-------------end-------------------");*/
            // 从头到尾对所有行进行计算
//            if (a[i].contains())
            if (sp != 0) {
                if (recode[sp][2] == null)
                    recode[sp][2] = Double.parseDouble(a[i-1][2]);
                if (recode[sp][3] == null)
                    recode[sp][3] = Double.parseDouble(a[i-1][3]);
            }
            if (sp == 0){
                if (recode[sp][2] == null)
                    recode[sp][2] = Double.parseDouble(a[i][2]);
                if (recode[sp][3] == null)
                    recode[sp][3] = Double.parseDouble(a[i][3]);
            }
            if (aInSection(a[i][0],split,sp)){
                // 如果 i 位于[sp,sp+1]区间中
                recode[sp][2] = findBig(recode[sp][2],a[i][2]);
                recode[sp][3] = findSmall(recode[sp][3],a[i][3]);
/*
            StdOut.println("a[i]:" + Arrays.toString(a[i]));
            System.out.println("***************Start----------------");
            System.out.println("i: " + i);
            for (Double[] strings : recode) {
                for (int j = 0; j < recode[0].length; j++) {
                    System.out.print(strings[j]);
                    System.out.print("|");
                }
                System.out.println();
            }
            System.out.println("-------------end-------------------");
*/
            } else {
                // 如果 一旦不能满足要求，则视为已经达到区分位置，此时如果没有达到split的尾，则进行指针移动操作

                if (sp < split.length -1) {
                    if (sp != split.length - 2)
                        recode[sp + 1][0] = Double.parseDouble(a[i][1]);
                        recode[sp][1] = Double.parseDouble(a[i-1][4]);
//
//                    if (recode[sp][2] == null)
//                        recode[sp][2] = Double.parseDouble(a[i - 1][2]);
//                    if (recode[sp][3] == null)
//                        recode[sp][3] = Double.parseDouble(a[i - 1][3]);
                    sp++;
                    System.out.println("SP :" +sp);
                    System.out.println("---------------------------------------------");
                }
                else if (sp == split.length - 1){
                    //进行最后一次操作，并且输出结果
                    recode[sp][1] = Double.parseDouble(a[i][4]);

                    return recode;
                }
            }
        }
        return recode;
    }
    /*static void Draw(double[][] a){
        // 计算最大最小值以及
        // color 0xff882244 0xff228844
        double width =0.8 / a.length;
        for (int i = 0; i < a.length ; i++){
            // 这个部分算空白距离
            double x0 = i * width/4 ;
            double y0 = a[i][0];//top
            double x1 = x0;
            double y1 = a[i][1];//bottom
            StdDraw.setPenColor(new java.awt.Color(0xff882244));
            StdDraw.setPenRadius(width/4);
            StdDraw.line(x0,y0,x1,y1);
        }
    }*/

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
