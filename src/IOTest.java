import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Year;
import java.util.List;
import java.math.*;

/* 主要修正问题：
1. [sp,sp+1) 修改成为(sp,sp+1]              complete in Dog.java
2. 需要对于不需要的行进行修正                complete in IOTest.java
3. 需要对于图像进行修正                   计划于Cat中进行
 */

public class IOTest {
    static int abigthanb(String a, String b){
//  如果 a < b = -1 ;  a > b = 1 ; a == b = 0
            return b.compareTo(a) ;
    }
    static int findBig(String a, String b){
        int A = Integer.parseInt(a);
        int B = Integer.parseInt(b);
        return Math.max(A, B);
    }
    static int findSmall(String a, String b){
        int A = Integer.parseInt(a);
        int B = Integer.parseInt(b);
        return Math.min(A, B);
    }
//    static int analyse(String[][] a, String[] split){
//        // import array and return a array with top,bottom,max,min
//        for (int row = 1; row < a.length ; row++){
//            for (int sp = 0; sp < split.length ; sp++){
//                int[] recode = new int[4];
//                // recode = {top,bottom,max,min}
//                if (abigthanb(a[row][0], split[sp]) == -1){
//                    // a < b
//                    // 1。 对于max，min进行取最小，最大操作
//                    recode[2] = findBig(Integer.toString(recode[3]),a[row][2]);
//                    recode[3] = findSmall(Integer.toString(recode[3]),a[row][3]);
//                    // 2. 对于
//
//
//                    sp++;
//                }
//            }
//        }
//    }
    public static void main(String[] args) throws IOException {
        // import file to Stream
        Path path = Paths.get("C:\\Programma\\JAVA\\src\\data\\HSI.csv");
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
        int account = 0;// showing the index of row
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

        // get the line number of contens
        /*int line = 0;// account the length of conter(line)
        for (String b : contents) {
            line++;
        }

        // transalte stream to 1D array
        String[] D1 = new String[line];
        String[][] D2 = new String[line][6];
        int account = 0; // 记录附着的行号
        for(String b : contents){
            D1[account] = b;
            account++;
        }*/

        // print 2D array with |
        /*for (String[] strings : D2) {
            for (int j = 0; j < D2[0].length; j++) {
                System.out.print(strings[j]);
                System.out.print("|");
            }
            System.out.println();
        }*/


        /* try to split (using compareForBig method to compare,
        and using max and min , add it to array.*/
        String maxtime = D2[line - 1][0];
        String mintime = D2[1][0];


//            StdOut.print(Integer.parseInt(maxtime.split("-")[0]));
        int YearAcross = Integer.parseInt(maxtime.split("-")[0]) - Integer.parseInt(mintime.split("-")[0]);

        // create a array to
        int acc = Integer.parseInt(mintime.split("-")[0]);
        int[] split_time = new int[YearAcross + 1];
        for ( int i = 0; i <= 35; i++){
//                StdOut.println(acc + i);
            split_time[i] = acc + i;
        }

        String[] split_year = new String[YearAcross+1];
//        split_year[0] = mintime; // 这个地方由于(sp,sp+1]的影响，因而需要提前一位
        {
            String[] apple = mintime.split("-");
            int banana = Integer.parseInt(apple[2]);
            banana--;
            split_year[0] = apple[0] + "-" + apple[1] + "-" + Integer.toString(banana);
        }
        split_year[YearAcross] = maxtime;
        for (int i = 1; i < split_time.length-1 ; i++){
            split_year[i] = Integer.toString(split_time[i]) + "-10-15" ;
        }

        // print the split of year
        /*for (int i = 0; i < split_year.length ; i++){
            System.out.println(split_year[i]);
        }*/


    }

}
