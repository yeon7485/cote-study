// LV.2 - JadenCase 문자열 만들기

public class JadenCase{
    public String solution(String s) {
        String answer = "";
        int idx = 0;

        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);

            if(idx == 0 && ch != ' '){
                answer += String.valueOf(ch).toUpperCase();
                idx++;
            }
            else if(ch == ' '){
                idx = 0;
                answer += ch;
            }
            else{
                answer += String.valueOf(ch).toLowerCase();
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        JadenCase j = new JadenCase();
        System.out.println(j.solution("3people unFollowed me"));
        System.out.println(j.solution("for the last week"));
        System.out.println(j.solution("a   bcd  hello"));
    }
}