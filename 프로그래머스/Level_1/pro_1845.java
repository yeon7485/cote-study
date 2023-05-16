// Lv.1 - 폰켓몬

import java.util.HashSet;

public class Phonekatmon {
    int solution(int[] nums) {
        int answer = nums.length / 2;
        HashSet<Integer> set = new HashSet<Integer>();
        
        for(int i = 0; i < nums.length; i++){
            if(!set.contains(nums[i])){
                set.add(nums[i]);
            }
        }

        answer = (answer < set.size()) ? answer : set.size();
        
        return answer;
    }

    public static void main(String[] args){
        Phonekatmon p = new Phonekatmon();
        int[] arr1 = {3, 1, 2, 3};
        int[] arr2 = {3, 3, 3, 2, 2, 4};
        int[] arr3 = {3, 3, 3, 2, 2, 2};

        System.out.println(p.solution(arr1));
        System.out.println(p.solution(arr2));
        System.out.println(p.solution(arr3));
    }
}
