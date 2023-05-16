// Lv.1 - 없는 숫자 더하기

public class pro_86051 {
    public int solution(int[] numbers) {
        int answer = 0;
        int[] num = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        
        for(int i = 0; i < num.length; i++){
            for(int j = 0; j < numbers.length; j++){
                if(num[i] == numbers[j]) num[i] = 0;
            }
            answer += num[i];
        }
        return answer;
    }

    public static void main(String[] args) {
        pro_86051 p = new pro_86051();
        int[] numbers1 = {1,2,3,4,6,7,8,0};
        int[] numbers2 = {5,8,4,0,6,7,9};

        System.out.println(p.solution(numbers1));
        System.out.println(p.solution(numbers2));
    }
}
