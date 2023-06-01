// Lv.1 - 두 정수 사이의 합

public class pro_12912 {
    public long solution(int a, int b) {
        long answer = 0;

        for(int i = Math.min(a, b); i <= Math.max(a, b); i++){
            answer += i;
        }
        
        return answer;
    }

    public static void main(String[] args) {
        pro_12912 bs = new pro_12912();
        System.out.println(bs.solution(3, 5));
        System.out.println(bs.solution(3, 3));
        System.out.println(bs.solution(5, 3));
    }
}
