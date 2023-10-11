import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;

public class LC1199 {
    public int minBuildTime(int[] blocks, int split){
//        Arrays.sort(blocks);

//        return calcRecursive(blocks, split, blocks.length -1 , 1, 0);
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for(int i: blocks){
            pq.add(i);
        }
        while(pq.size() != 1){
            pq.poll();
            pq.offer(split + pq.poll());
        }
        return pq.poll();
    }

//    private int calcRecursive(int[] blocks, int split, int idx, int workers, int cost){
//        if(workers == 0 && idx != -1){
//            return Integer.MAX_VALUE;
//        }
//
//        if(workers >= idx + 1){
//            return cost + blocks[idx];
//        }
//        return Math.min(
//                calcRecursive(blocks, split, idx -1, workers - 1, cost + blocks[idx] - blocks[idx -1]),
//                calcRecursive(blocks, split, idx, workers * 2, cost + split)
//        );
//    }

    public static void main(String[] args) {
        LC1199 sol = new LC1199();
        System.out.println(sol.minBuildTime(new int[] {3, 2, 1}, 1)); //4
        System.out.println(sol.minBuildTime(new int[] {1, 1, 1, 1}, 100)); // 201
        System.out.println(sol.minBuildTime(new int[] {94961,39414,41263,7809,41473}, 90)); //95051

    }
}
