// Lv.1 - 키패드 누르기

public class PressKeypad {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        String h = "";
        int left = 10;
        int right = 12;
        String c = "";

        h = (hand.equals("left")) ? "L":"R";

        for (int n : numbers) {
            // 가운데 열일 때
            if (n == 0 || n % 3 == 2) {
                // 더 가까운 손가락 구해주기
                c = closer(left, right, n, h);
                answer += c;

                if (c.equals("L"))
                    left = n;
                else
                    right = n;
            }
            // 왼쪽 열일 때
            else if (n % 3 == 1) {
                answer += "L";
                left = n;
            }
            // 오른쪽 열일 때
            else if (n % 3 == 0) {
                answer += "R";
                right = n;
            }

        }

        return answer;
    }

    // 가운데 열일 때 거리 구해서 어느 손가락으로 누를지 구하기
    public String closer(int left, int right, int n, String h) {
        String hand = "";

        int num; // 누르려는 버튼
        int l, r, dl, dr;

        num = (n == 0) ? 11 : n;

        // 누르려는 버튼과의 차이
        l = Math.abs(left - num);
        r = Math.abs(right - num);

        // 0일 때 11로 처리해주기
        if (left == 0) {
            l = Math.abs(11 - num);
        } else if (right == 0) {
            r = Math.abs(11 - num);
        }

        // 몇 칸 가야되는지 거리 구해주기
        dl = (l / 3) + (l % 3); 
        dr = (r / 3) + (r % 3); 

        if (dl > dr)
            hand = "R";
        else if (dl < dr)
            hand = "L";
        else
            hand = h;

        return hand;
    }

    public static void main(String[] args) {
        PressKeypad pk = new PressKeypad();
        int[] n1 = { 1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5 };
        int[] n2 = { 7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2 };
        int[] n3 = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 };

        System.out.println(pk.solution(n1, "right"));
        System.out.println(pk.solution(n2, "left"));
        System.out.println(pk.solution(n3, "right"));
    }
}
