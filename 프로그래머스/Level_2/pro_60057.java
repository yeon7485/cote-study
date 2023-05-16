// Lv.2 - 문자열 압축

public class StringCompression {
    public int solution(String s) {
        int answer = s.length();
        int n = 0; // 반복 횟수 
        String str = ""; // 압축한 문자열
        String com = ""; // 비교할 단위
        String current = ""; // 현재 단위랑 비교해줄 문자열

        for(int i = 1; i <= s.length() / 2; i++){
            com = s.substring(0, i);
            n = 1;
            for(int j = i; j < s.length(); j = j + i){
                // 비교할 범위가 넘어가지 않으면 비교 시작
                if(j + i <= s.length()){
                    current = s.substring(j, j + i); 
                    // 비교할 단위와 현재 문자열이 같으면
                    if(com.equals(current)){
                        n++;
                    }
                    // 비교할 단위와 현재 문자열이 같지 않고, 반복 횟수가 1보다 크면
                    else if(n > 1){
                        str += n + com;
                        n = 1;
                    }
                    else{
                        str += com;
                    }
                    // 비교할 단위를 현재 문자열로 바꿈
                    com = current;
                }
            }

            // 문자열 끝까지 비교했을 때, 반복 횟수가 1보다 크면 저장
            if(n > 1) str += n + com;
            else str += com;

            //비교하는 단위로 나누어 떨어지지 않을 때 
            if(s.length() % i != 0){
                // 남은 길이만큼 압축한 문자열에 저장
                str += s.substring(s.length() - s.length() % i);
            }
            answer = Math.min(answer, str.length());
            str = "";
        }
        return answer;
    }


    public static void main(String[] args) {
        StringCompression sc = new StringCompression();

        System.out.println(sc.solution("aabbaccc"));
        System.out.println(sc.solution("ababcdcdababcdcd"));
        System.out.println(sc.solution("abcabcdede"));
        System.out.println(sc.solution("abcabcabcabcdededededede"));
        System.out.println(sc.solution("xababcdcdababcdcd"));
        System.out.println(sc.solution("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxz"));// 100xz
        
    }    
}
