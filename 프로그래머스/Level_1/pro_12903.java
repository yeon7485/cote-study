// Lv.1 - 가운데 글자 가져오기

public class MidWord{
    public String solution(String s) {
        String answer = "";
        int mid = s.length()/2;
        if(s.length() % 2 == 0){
            answer = s.substring(mid - 1, mid + 1);
        }
        else{
            answer = s.substring(mid, mid + 1);
        }
        return answer;
    }


    public static void main(String[] args) {
        MidWord mw = new MidWord();
        System.out.println(mw.solution("abcde"));
        System.out.println(mw.solution("qwer"));
    }
}