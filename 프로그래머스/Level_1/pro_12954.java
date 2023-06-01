// Lv.1 - x만큼 간격이 있는 n개의 숫자

import java.util.Arrays;

public class pro_12954{
    public long[] solution(long x, int n){
        long[] answer = {};
        answer = new long[n];
        answer[0] = x;
        for (int i = 1; i < n; i++){
            answer[i] = answer[i - 1] + x;
        }
        return answer;
    }

    public static void main(String[] args){
        pro_12954 x = new pro_12954();
        System.out.println(Arrays.toString(x.solution(3, 5)));
        System.out.println(Arrays.toString(x.solution(4, 3)));
        System.out.println(Arrays.toString(x.solution(-4, 2)));
    }
}