// Lv.1 - 이상한 문자 만들기

public class pro_12930 {
    public String solution(String s) {
        String answer = "";
        int idx = 0;

        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(ch == ' '){
                idx = 0;
                answer += ch;
            }
            else{
                answer += (idx % 2 == 0) ? String.valueOf(ch).toUpperCase() : String.valueOf(ch).toLowerCase();
                idx++;
            } 
        }
        return answer;
    }

    public static void main(String[] args) {
        pro_12930 s = new pro_12930();
        System.out.println(s.solution("try  hello  world"));
    }
}