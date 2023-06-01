// LV.1 - 평균 구하기

public class pro_12944 {
    public double solution(int[] arr) {
        double answer = 0;
        for(int a: arr){
            answer += a;
        }
        answer /= arr.length;
        return answer;
    }
    public static void main(String[] args) {
        pro_12944 a = new pro_12944();
        int[] arr1 = {1, 2, 3, 4};
        int[] arr2 = {5, 5};
        System.out.println(a.solution(arr1));
        System.out.println(a.solution(arr2));
    }
}
