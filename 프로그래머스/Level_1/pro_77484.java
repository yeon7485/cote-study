// Lv.1 - 로또의 최고 순위와 최저 순위

import java.util.Arrays;

public class pro_77484 {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int max = 0;
        int min = 0;

        for(int w: win_nums){
            if(Arrays.stream(lottos).anyMatch(i -> i == w)){
                max++;
                min++;
            }
        }
        for(int l : lottos){
            if(l == 0){
                max++;
            }
        }

        if(max < 2) answer[0] = 6;
        else answer[0] = 7 - max; 

        if(min < 2) answer[1] = 6;
        else answer[1] = 7 - min;

        return answer;
    }

    public static void main(String[] args) {
        pro_77484 p = new pro_77484();
        int[] l1 = {44, 1, 0, 0, 31, 25};
        int[] w1 = { 31, 10, 45, 1, 6, 19};
        int[] l2 = {0, 0, 0, 0, 0, 0};
        int[] w2 = {38, 19, 20, 40, 15, 25};
        int[] l3 = {45, 4, 35, 20, 3, 9};
        int[] w3 = {20, 9, 3, 45, 4, 35};
        
        System.out.println(Arrays.toString(p.solution(l1, w1)));
        System.out.println(Arrays.toString(p.solution(l2, w2)));
        System.out.println(Arrays.toString(p.solution(l3, w3)));
    }
}
