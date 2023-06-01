// Lv.1 - 예산
import java.util.Arrays;

public class pro_12982 {
    public int solution(int[] d, int budget) {
        int answer = 0;

        Arrays.sort(d);
        for(int i: d){
            budget -= i;
            if(budget < 0) break;
            else answer++;
        }

        return answer;
    }

    public static void main(String[] args) {
        pro_12982 b = new pro_12982();
        int[] d1 = {1, 3, 2, 5, 4};
        int[] d2 = {2, 2, 3, 3};

        System.out.println(b.solution(d1, 9));
        System.out.println(b.solution(d2, 10));
    }
}
