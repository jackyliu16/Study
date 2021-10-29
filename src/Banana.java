public class Banana {
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
    public static void main(String[] args){
        String a = "1987-02-12";
        String b = "1987-02-12";
        //  如果 a < b = -1 ;  a > b = 1 ; a == b = 0
        System.out.println(compare(a,b));
    }
}
