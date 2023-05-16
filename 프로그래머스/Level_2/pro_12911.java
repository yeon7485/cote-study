// Lv.2 - 다음 큰 숫자

public class NextBigNumber {
    public int solution(int n) {
        int answer = n + 1;
        while(true){
            if(checkOne(n) == checkOne(answer)){
                break;
            }
            answer++;
        }
        return answer;
    }

    public int checkOne(int n){
        int one = 0;
        while(n > 0){
            if(n % 2 == 1) one++;
            n /= 2;
        }
        return one;
    }

    public static void main(String[] args) {
        NextBigNumber n = new NextBigNumber();
        System.out.println(n.solution(78));
        System.out.println(n.solution(15));
    }
}
