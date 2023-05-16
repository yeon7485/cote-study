// Lv.1 - 숫자 문자열과 영단어

import java.util.HashMap;

public class pro_81301 {
    public int solution(String s) {
        int answer = 0;
        String[] engWord = {"zero", "one", "two", "three","four","five","six","seven","eight","nine"};
        String a = "";
        String word = "";
        char ch;
        
        HashMap<String, String> map = new HashMap<String, String>();
        for(int i = 0; i < 10; i++){
            map.put(engWord[i], Integer.toString(i));
        }
        
        for(int i = 0; i < s.length(); i++){
            ch = s.charAt(i);
            if(ch >= 48 && ch <= 57){
                a += ch;
            }
            else{
                word += ch;
            }
            if(map.containsKey(word)){
                a += map.get(word); 
                word = "";
            }
        }
        
        answer = Integer.parseInt(a);
        return answer;
    }

    public static void main(String[] args){
        pro_81301 ne = new pro_81301();

        System.out.println(ne.solution("one4seveneight"));
        System.out.println(ne.solution("23four5six7"));
        System.out.println(ne.solution("2three45sixseven"));
        System.out.println(ne.solution("123"));
    }
}
