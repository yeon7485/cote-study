// Lv.2 - N개의 최소공배수

import java.util.Arrays;

public class LeastCommonMultiple {
    public int solution(int[] arr) {
        int answer = 0;
        boolean check = true;
        // 오름차순 정렬
        Arrays.sort(arr);
        answer = arr[arr.length - 1];

        while (true) {
            for (int a : arr) {
                if (answer % a != 0) {
                    check = false;
                    break;
                }
            }

            // 하나라도 0으로 나누어 떨어지지 않으면
            if (check == false) {
                check = true;
                answer++;
            }
            // 전부 다 0으로 나누어 떨어지면
            else
                break;
        }

        return answer;
    }

    public static void main(String[] args) {
        LeastCommonMultiple ncm = new LeastCommonMultiple();
        int[] arr1 = { 2, 6, 8, 14 };
        int[] arr2 = { 1, 2, 3 };

        System.out.println(ncm.solution(arr1));
        System.out.println(ncm.solution(arr2));
    }
}
