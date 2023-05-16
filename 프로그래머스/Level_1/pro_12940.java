import java.util.Arrays;

public class pro_12940 {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        int a = n;
        int b = m;
        if (n > m) {
            a = m;
            b = n;
        }
        for (int i = a; i > 0; i--) {
            if ((a % i == 0) && (b % i == 0)) {
                answer[0] = i;
                break;
            }
        }

        answer[1] = (n / answer[0]) * (m / answer[0]) * answer[0];
        return answer;
    }

    public static void main(String[] args) {
        pro_12940 p = new pro_12940();
        System.out.println(Arrays.toString(p.solution(3, 12)));
        System.out.println(Arrays.toString(p.solution(2, 5)));
    }
}
