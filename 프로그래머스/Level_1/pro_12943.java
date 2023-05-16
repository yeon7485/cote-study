// LV.1 - 콜라츠 추측

public class pro_12943 {
    public int solution(long num) {
        int answer = 0;
        while(num > 1){
            if(answer == 500){
                answer = -1;
                break;
            }
            else{
                if(num % 2 == 0){
                    num = num / 2;
                }
                else{
                    num = num * 3 + 1;
                }
                answer += 1;
                
            }
        }
        return answer;
    }
    public static void main(String[] args) {
        pro_12943 p = new pro_12943();
        System.out.println(p.solution(6));
        System.out.println(p.solution(16));
        System.out.println(p.solution(626331));
    }
}
