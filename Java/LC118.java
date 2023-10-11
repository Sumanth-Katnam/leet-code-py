import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

public class LC118 {
    public List<List<Integer>> generate(int numRows) {
//        List<List<Integer>> res = new ArrayList<>();
//        res.add(new ArrayList<>(List.of(1)));
//
//        IntStream.range(1, numRows).forEach(i -> {
//            List<Integer> temp = new ArrayList<>();
//            temp.add(0);
//            temp.addAll(res.get(res.size() - 1));
//            temp.add(0);
//
//            List<Integer> row = new ArrayList<>();
//
//            IntStream.range(0, res.get(res.size() - 1).size() + 1).forEach(j -> {
//                row.add(temp.get(j));
//                row.add(temp.get(j + 1));
//            });
//
//            res.add(row);
//        });
//
//        return res;
        List<List<Integer>> result = new ArrayList<>();
        for(int i = 0; i < numRows; i++){
            List<Integer> row = new ArrayList<>();
            for(int j = 0; j <= i; j++){
                if(j == 0 || j == i)
                    row.add(1);
                else
                    row.add(result.get(i - 1).get(j - 1) + result.get(i - 1).get(j));
            }
            result.add(row);
        }
        return result;
    }
}
