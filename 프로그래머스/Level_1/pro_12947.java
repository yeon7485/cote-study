// Lv.1 - 하샤드 수

public class HarshadNumber{
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
        HarshadNumber h = new HarshadNumber();
        System.out.println(h.solution(10));
        System.out.println(h.solution(12));
        System.out.println(h.solution(11));
        System.out.println(h.solution(13));
    }
}