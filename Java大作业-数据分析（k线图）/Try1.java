import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Date;
import java.util.List;

public class Try1 {
    private static Date[] split_Date;
    private static Date[] allTime;
    private static double[][] allData;

    public static Date getTime(String t) throws ParseException {
        return new SimpleDateFormat("yyyy-MM-dd").parse(t);
    }

    public static void main(String[] args) throws IOException,ParseException {
        Path path = Paths.get("HSI.csv");
        List<String> s = Files.readAllLines(path, Charset.defaultCharset());
        s.remove(0);
//        String[] Data = s.stream().filter(x->!x.contains("null")).toArray(String[]::new);
//        Double[] D2 = Arrays.stream(Data).mapToDouble(t->
//                for ( int i=0 ; i < Data[0].split(",").length ; i++ )
//                    Double.parseDouble(t.split(",")[i]));
        Date[] allTime = s.stream()
                .filter(x)
                .toArray(Date[]::new);


        // the create of variable
//        allTime = new Date[Data.length];
//        allData = new double[Data.length][Data[0].split(",").length];
        // get time from Data to allTime
        for ( int i = 0 ; i < Data.length ; i++ ) {
            allTime[i] = getTime(Data[i].split(",")[0]);
            for ( int j = 1 ; j < Data[i].split(",").length ; j++ ) {
                allData[i][j-1] = Double.parseDouble(Data[i].split(",")[j]);
            }
        }
        StdArrayIO.print(allData);







    }

}
