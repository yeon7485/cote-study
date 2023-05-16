// Lv.1 - 약수의 개수와 덧셈
import java.util.HashMap;

public class pro_77884 {
    public int solution(int left, int right) {
        int answer = 0;
        int count = 0;
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i = left; i <= right; i++){
            for(int j = 1; j <= i; j++){
                count = (i % j == 0) ? count+1 : count; 
            }
            map.put(i, count);
            count = 0;
        }

        for(int key : map.keySet()){
            answer = (map.get(key) % 2 == 0) ? answer + key : answer - key;
        }

        return answer;
    }

    public static void main(String[] args) {
        pro_77884 p = new pro_77884();
        System.out.println(p.solution(13, 17));
        System.out.println(p.solution(24, 27));
    }
}
