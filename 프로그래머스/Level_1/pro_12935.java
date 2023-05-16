import java.util.Arrays;

// Lv.1 - 제일 작은 수 제거하기

public class pro_12935 {

    public int[] solution(int[] arr) {
        int[] answer;
        if (arr.length == 1) {
            answer = new int[1];
            answer[0] = -1;
        } 
        else {
            answer = new int[arr.length - 1];
            int min = arr[0];
            int count = 0;
            for (int a : arr) {
                min = min > a ? a : min;
            }

            for (int i = 0; i < arr.length; i++) {
                if (min != arr[i]){
                    answer[count] = arr[i];
                    count++;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {

        pro_12935 p = new pro_12935();
        int[] arr1 = { 5, 1, 2, 6, 8 };
        int[] arr2 = { 10 };
        System.out.println(Arrays.toString(p.solution(arr1)));
        System.out.println(Arrays.toString(p.solution(arr2)));
    }

}
