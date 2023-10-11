import java.util.*;
import java.util.stream.IntStream;

public class LC1337 {
    public int[] kWeakestRows_old(int[][] mat, int k) {
        List<List<Integer>> count_list = new ArrayList<>();

        IntStream.range(0, mat.length).forEach(i -> {
            List<Integer> idx_val = new ArrayList<>();
            idx_val.add(i);
            int sol_count = (int) Arrays.stream(mat[i]).filter(j -> j == 1).count();
            idx_val.add(sol_count);
            count_list.add(idx_val);
        });


        count_list.sort(Comparator.comparingInt(p -> p.get(1)));
        int[] res = new int[k];
        IntStream.range(0, k).forEach(i -> {
                res[i] = count_list.get(i).get(0);
        });
        return res;
    }

    public int[] kWeakestRows(int[][] mat, int k) {
        Map<Integer, List<Integer>> count_list = new TreeMap<>();

        IntStream.range(0, mat.length).forEach(i -> {
            int sol_count = (int) Arrays.stream(mat[i]).filter(j -> j == 1).count();

            if(!count_list.containsKey(sol_count)){
                count_list.put(sol_count, new ArrayList<>());
            }
            count_list.get(sol_count).add(i);
        });

        int[] res = new int[k];
        int i = 0;
        for(int sol_count:count_list.keySet()){
            for(int idx:count_list.get(sol_count)){
                res[i] = idx;
                i++;
                if(i == k) break;
            }
            if(i == k) break;
        }
        return res;
    }
}
