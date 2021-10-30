public class Cat {
    public static void main(String[] args){
        //            top       bottom      high        low
        double[] a = {2603.300049,2590.800049,2614.899902,2561.699951};
        double[] b = {2578.199951,2533.899902,2578.199951,2449.899902};
        double[] c = {2536.899902,2524.0,2536.899902,2484.399902};
        double[][] A = {a,b,c};


//        for (double[] strings : A) {
//            for (int j = 0; j < A[0].length; j++) {
//                System.out.print(strings[j]);
//                System.out.print("|");
//            }
//            System.out.println();
//        }

        Draw(A);

    }
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
    /*static void Draw(double[][] a){
        final double[] temp = findScale(a);
        StdDraw.setXscale(0,1);
        StdDraw.setYscale(temp[0],temp[1]);

//        final double WIDTH =
//        final double SPAREWIDTH = (1/5)*WIDTH;
        double t = 1.0/ a.length;
        final double WIDTH = (3/4.0) * t;
        final double SPAREWIDTH = (1/4.0) * t;

        for(int i = 0 ; i < a.length ; i++){
            double x = SPAREWIDTH+(WIDTH + SPAREWIDTH) * (i);
            double y0 = a[i][0];
            double y1 = a[i][1];
            StdDraw.setPenRadius(WIDTH);
            StdDraw.line(x,y0,x,y1);
        }*/
//
//    }

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
            StdDraw.line(x,a[i][0],x,a[i][1]);
        }
        //pen radius = 1/4 * width

        /*for ( int i = 0; i < a.length; i++){
            double x = (1/2) * sp + WIDTH_Total * i;
            StdDraw.setPenRadius((1.0/2) * wSquare);
            StdDraw.line(x,a[i][0],x,a[i][1]);
        }*/


    }
    /*static void Draw(double[][] a) {
        final double sp = 1;
        final double wSquare    = 4;
        final double wLine      = 2;
        final double[] temp = findScale(a);
        StdDraw.setXscale(0,(a.length + 1) * (sp + 0.5 * wSquare));
        StdDraw.setYscale(temp[0],temp[1]);

        for ( int i = 0 ; i < a.length ; i++) {
            double x = (sp + 0.5 * wSquare) * (i + 1);
            StdDraw.setPenRadius(wLine);
            StdDraw.line(x,a[i][0],x,a[i][1]);


        }
    }*/
    /*static void Draw(double[][] a) {
        final double sp     = 1.0;
        final double wSquare= 4.0;
        final double wLine  = 2.0;
        final double[] temp = findScale(a);
        StdDraw.setXscale(0,(a.length + 1) * ());
        StdDraw.setYscale(temp[0],temp[1]);
    }*/
}
