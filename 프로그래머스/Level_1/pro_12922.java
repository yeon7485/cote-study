// Lv.1 - 수박수박수박수박수박수?

public class Watermelon {
    String solution(int n) {
        String answer = "";
        for(int i = 0; i < n/2; i++){
            answer += "수박";
        }
        if(n % 2 == 1){
            answer += "수";
        }
        return answer;
    }

    public static void main(String[] args){
        Watermelon w = new Watermelon();

        System.out.println(w.solution(3));
        System.out.println(w.solution(8));
    }
}