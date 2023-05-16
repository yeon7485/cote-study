// Lv.1 - 핸드폰 번호 가리기

public class Phone_Number{
    public String solution(String phone_number) {
        String answer = "";
        int num = phone_number.length() - 4;
        
        for(int i = 0; i < num; i++)
            answer += "*";

        answer += phone_number.substring(num);
        return answer;
    }

    public static void main(String[] args) {
        Phone_Number pn = new Phone_Number();
        System.out.println(pn.solution("01033334444"));
        System.out.println(pn.solution("027778888"));
    }
}