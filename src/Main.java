import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Year;
import java.util.List;
import java.math.*;
import java.util.Scanner;

/**
 * Main Engineering Programme
 * @author Jacky Liu
 * @version final version
 *
 * Fixed Problem:
 * 1.[sp,sp+1) -> (sp,sp+1]     complete in Dog.java
 * 2. null row of Data          complete in Main.java
 * 3. Canvas margin setting problem     complete in Cat.java
 */

public class Main {
    static double findBig(double a, String b){
        //
        double B = Double.parseDouble(b);
        return Math.max(a, B);
    }
    static double findSmall(double a, String b) {
//        int A = Integer.parseInt(a);
        double B = Double.parseDouble(b);
        return Math.min(a, B);
    }

    /** Compare
     * Enter two times and compare them to get the relationship between them
     * if time a < time b return -1
     * if time a = time b return 0
     * if time a > time b return 1
     * @return 1,0,-1
     */
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
    /** aInSection
     * If OneTime is in (split[sp],split[sp+1] ];
     * @param OneTime   Date
     * @param split     Split Array
     * @param sp        Year Number
     * @return          True or False
     */
    static boolean aInSection(String OneTime,String[] split,int sp){
        if (sp <= split.length - 1)
            return (compare(OneTime, split[sp]) != -1) && (compare(OneTime, split[sp + 1]) == -1);
        else
            System.out.println("analyse out");
        return false;
    }

    /**
     * For each input Date in a[i] , Tests whether it is in the corresponding year.
     * if yes :
     *      using bubble sort to find the biggest and the lowest.
     * if not :
     *      Use a simple assignment to get its open and close prices
     * @param a         2D array of Data
     * @param split     Split Year Array
     * @return          recode[EachYear]{ top, bottom, high, low}
     */
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
            /*System.out.println("---------------Start----------------");
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
//                    System.out.println("SP :" +sp);
//                    System.out.println("---------------------------------------------");

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

    /**
     * Look for global maximum and minimum values to determine canvas scope
     * @param a     recode Array
     * @return      global maximum, global minimum
     */
    static double[] findScale(double[][] a){
        // finding the min and the max of all data helping to drawing
        double[] high_collect = new double[a.length];
        double[] low_collect = new double[a.length];
        for( int i = 0 ; i < a.length; i++){
            high_collect[i] = a[i][2];
            low_collect[i] = a[i][3];
        }
        double[] answer = {StdStats.min(low_collect),StdStats.max(high_collect)};
        return answer;
    }

    /**
     * Draw the picture
     * @param a recode data
     */
    static void Draw(double[][] a) {
        final double[] temp = findScale(a);
        StdDraw.setXscale(0,1);
        StdDraw.setYscale(temp[0],temp[1]);

        // 1.0 / a.length = (sp + wSquare);
        final double WIDTH_Total = 1.0 / a.length;

        final double sp = WIDTH_Total * 0.4;
        final double wSquare = WIDTH_Total * 0.6;
        final double wLine = wSquare * 0.5;

        for ( int i = 0 ; i < a.length ; i++) {
            double x = (sp + wSquare) * (i + 1) - 0.5 * wSquare;
            StdDraw.setPenRadius(0.5 * wLine);
            StdDraw.setPenColor(new java.awt.Color(a[i][0] > a[i][1] ? 0xff882244:0xff228844));
            StdDraw.filledRectangle(x,(a[i][0] + a[i][1]) / 2.0 , wSquare * 0.5, Math.abs(a[i][0] - a[i][1]) / 2.0);
            StdDraw.line(x,a[i][2],x,a[i][3]);
        }
        //pen radius = 1/4 * width

        /*for ( int i = 0; i < a.length; i++){
            double x = (1/2) * sp + WIDTH_Total * i;
            StdDraw.setPenRadius((1.0/2) * wSquare);
            StdDraw.line(x,a[i][0],x,a[i][1]);
        }*/


    }


    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        System.out.println("在开始之前请确认本文件被放置于src目录中，并且src目录中包含data目录[里面放有需要进行绘图的数据]");
        System.out.println("中文注释： 此处请输入一个在src的子目录data中的csv文件名称(注：包含.csv)");
        System.out.println("please give a filename under a file(data) at the same catalogue: ");
        String filename = in.next();

        // import file to Stream
        Path path = Paths.get("src/data/" + filename);
        List<String> contents = Files.readAllLines(path, Charset.defaultCharset());
//            object[] apple = contents.toArray();
//            for (String b: contents){
//                System.out.println(b);
//            }

        // get the number who not contain null
        int line = 0; //account the number of line
        for (String b : contents){
            if (! b.contains("null"))
                line++;
        }

        // translate stream to 1D array
        String[] D1 = new String[line];
        String[][] D2 = new String[line][6];

        // BC I don't know how to use stream , So I can only make simple changes to the code
        // goal : change stream to 1D array which showing the row of data(String)
        int account = 0;// Give an index to assign to an array
        for (String b : contents){
            if (! b.contains("null")){
                D1[account] = b;
                account++;
            }
        }

        // translate 1D array to 2D array
        for (int i = 0 ; i < line ; i++){
            D2[i] = D1[i].split(",");
        }

        // print out everything(2D) from data (String[][])
        /*for (String[] strings : D2) {
            for (int j = 0; j < D2[0].length; j++) {
                System.out.print(strings[j]);
                System.out.print("|");
            }
            System.out.println();
        }*/

        /* Create split_Year Array for aInSection to Separate the data ( from first col)  */
        String maxtime = D2[line - 1][0];
        String mintime = D2[1][0];

        int YearAcross = Integer.parseInt(maxtime.split("-")[0]) - Integer.parseInt(mintime.split("-")[0]);

        // create a array of the first year to last year
        int startyear = Integer.parseInt(mintime.split("-")[0]);
        int[] split_time = new int[YearAcross + 1];
        for ( int i = 0; i <= YearAcross; i++){
//                StdOut.println(acc + i);
            split_time[i] = startyear + i;
        }

        String[] split_year = new String[YearAcross+1];
        // BC aInSection using (sp,sp+1] so we need to move the first year forward by one
        {
            String[] apple = mintime.split("-");        // getting the first time of Data
            int banana = Integer.parseInt(apple[2]);
            banana--;                                         // advance the date by one
            split_year[0] = apple[0] + "-" + apple[1] + "-" + Integer.toString(banana);
        }
        split_year[YearAcross] = maxtime;
        // Sets the last day to the last delimited value
        for (int i = 1; i < split_time.length-1 ; i++){
            split_year[i] = Integer.toString(split_time[i]) + "-10-15" ;
        }       // add mon and day to data

        // print the split of year
        /*or (int i = 0; i < split_time.length ; i++){
            System.out.println(split_time[i]);
        }*/

        Double[][] output = analyse(D2,split_year);
        double[][] OutPut = new double[output.length][output[0].length];
        for ( int i = 0 ; i < output.length; i++){
            for ( int j = 0; j < output[0].length; j++){
                OutPut[i][j] = output[i][j];
            }
        }

        // print out the OutPut Array
        /*for(double[] strings : OutPut){
            for ( int j = 0; j < OutPut[0].length ; j++){
                System.out.print(strings[j]);
                System.out.print("|");
            }
            System.out.println();
        }*/


        Draw(OutPut);
    }

}
