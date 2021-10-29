/*
import java.util.Arrays;

public class candle {
    static double step(double y){
        return y + (Math.random() - 0.5) * 0.05;
    }
   */
/* static double minMax(int n, double y, double a[]) {
        a[2] = Math.min(a);
        a[1] = Math.max(a);
    }*//*

    public static void main(String[] args){
        String str =
                "1987-01-02,2540.100098,2540.100098,2540.100098,2540.100098,2540.100098,0\n" +
                "1987-01-05,2552.399902,2552.399902,2552.399902,2552.399902,2552.399902,0\n" +
                "1987-01-06,2583.899902,2583.899902,2583.899902,2583.899902,2583.899902,0\n" +
                "1987-01-07,2607.100098,2607.100098,2607.100098,2607.100098,2607.100098,0\n" +
                "1987-01-08,2603.300049,2603.300049,2603.300049,2603.300049,2603.300049,0\n" +
                "1987-01-09,2561.699951,2561.699951,2561.699951,2561.699951,2561.699951,0";
        String[] a = str.split("\n");
        String[][] b = new String[a.length][6];
        for(int i = 0; i < a.length ; i ++){
            b[i] = a[i].split(",");
        }

        double[] open  = new double[b[0].length];
        double[] close = new double[b[0].length];
        double[] max   = new double[b[0].length];
        double[] min   = new double[b[0].length];
        int[] x     = {2,5,6,7,8,9};

        for ( int row = 0; row < b.length ; row++){
            open[row] = Double.parseDouble(b[row][1]);
            close[row] = Double.parseDouble(b[row][2]);
            min[row] = Double.parseDouble(b[row][3]);
            max[row] = Double.parseDouble(b[row][4]);
        }
//        StdArrayIO.print(open);




    }
}
*/
