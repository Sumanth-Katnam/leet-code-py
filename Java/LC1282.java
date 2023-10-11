import java.util.*;
import java.util.stream.IntStream;

public class LC1282 {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        Map<Integer, List<List<Integer>>> size_map = new HashMap<>();

        IntStream.range(0, groupSizes.length).forEach(idx -> {
            if(!size_map.containsKey(groupSizes[idx])){
                List<List<Integer>> listOfLists = new ArrayList<>(new ArrayList<>());
                List<Integer> subList = new ArrayList<>();
                subList.add(idx);
                listOfLists.add(subList);
                size_map.put(groupSizes[idx], listOfLists);
            } else {
                List<List<Integer>> curr_list = size_map.get(groupSizes[idx]);
                if(curr_list.get(curr_list.size() - 1).size() < groupSizes[idx]){
                    curr_list.get(curr_list.size() - 1).add(idx);
                } else {
                    List<Integer> subList = new ArrayList<>();
                    subList.add(idx);
                    size_map.get(groupSizes[idx]).add(subList);
                }
            }
        });

        List<List<Integer>> res = new ArrayList<>();
        for(List<List<Integer>> i : size_map.values()){
            res.addAll(i);
        }
        return res;
    }

    public static void main(String[] args) {
        LC1282 sol = new LC1282();
        System.out.println(sol.groupThePeople(new int[] {3,3,3,3,3,1,3})); // [[5],[0,1,2],[3,4,6]]
        System.out.println(sol.groupThePeople(new int[] {2,1,3,3,3,2})); // [[1],[0,5],[2,3,4]]
    }
}
