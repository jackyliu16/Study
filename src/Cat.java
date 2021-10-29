public class Cat {
    public static void main(String[] args){
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
        double[] high_collect = new double[a.length];
        double[] low_collect = new double[a.length];
        for( int i = 0 ; i < a.length; i++){
            high_collect[i] = a[i][2];
            low_collect[i] = a[i][3];
        }
        double[] answer = {StdStats.min(low_collect),StdStats.max(high_collect)};
        return answer;
    }
    static void Draw(double[][] a){
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
        }
    }

}
