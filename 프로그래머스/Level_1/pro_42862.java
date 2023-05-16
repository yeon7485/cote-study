// Lv.1 - 체육복

import java.util.*;

public class GymSuit {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int i = 1; i <= n; i++){
            if(contains(lost, i) && contains(reserve, i)) map.put(i, 1);
            else if(contains(lost, i)) map.put(i, 0);
            else if(contains(reserve, i)) map.put(i, 2);
            else map.put(i, 1);
        }

        for(int i = 1; i <= n; i++){
            if(map.get(i) == 0){
                if(i > 1 && map.get(i-1) == 2){
                    map.put(i, 1);
                    map.put(i - 1, 1);
                }
                else if(i < n && map.get(i + 1) == 2){
                    map.put(i, 1);
                    map.put(i + 1, 1);
                }
            }
        }

        for(int i : map.keySet()){
            if(map.get(i) > 0) answer++;
        }

        return answer;
    }

    public static boolean contains(final int[] arr, final int key) {
        return Arrays.stream(arr).anyMatch(i -> i == key);
    }


    public static void main(String[] args){
        GymSuit gs = new GymSuit();

        int[] lost1 = {2, 4};
        int[] reserve1 = {1, 3, 5};

        int[] lost2 = {2, 4};
        int[] reserve2 = {3};

        int[] lost3 = {3};
        int[] reserve3 = {1};
        System.out.println(gs.solution(5, lost1, reserve1));
        System.out.println(gs.solution(5, lost2, reserve2));
        System.out.println(gs.solution(3, lost3, reserve3));
    }
}
