// Lv.1 - 하샤드 수

public class pro_12947{
    public boolean solution(int x) {
        boolean answer = true;
        int num = x;
        int sum = 0;
        while(num > 0){
            sum += num % 10;
            num /= 10;
        }
        answer = (x % sum == 0) ? true : false;
        return answer;
    }

    public static void main(String[] args) {
        pro_12947 h = new pro_12947();
        System.out.println(h.solution(10));
        System.out.println(h.solution(12));
        System.out.println(h.solution(11));
        System.out.println(h.solution(13));
    }
}