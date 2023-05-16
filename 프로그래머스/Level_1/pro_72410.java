
// Lv.1 - 신규 아이디 추천

public class pro_72410 {
    public String solution(String new_id) {
        String str = new_id.toLowerCase(); // 1단계
        str = str.replaceAll("[^-_.a-z0-9]", ""); // 2단계
        str = str.replaceAll("[.]{1,}+", "."); // 3단계
        str = str.replaceAll("^[.]|[.]$", ""); // 4단계
        str = str.equals("") ? "a" : str; // 5단계
        str = str.length() > 15 ? str.substring(0, 15) : str; // 6단계

        // 마지막 마침표 검사
        str = str.replaceAll("[.]$", "");

        // 7단계
        if (str.length() == 1) str += str;
        if (str.length() == 2) str += str.substring(1);

        return str;
    }

    public static void main(String[] args) {
        pro_72410 p = new pro_72410();

        System.out.println(p.solution("...!@BaT#*..y.abcdefghijklm"));
        System.out.println(p.solution("z-+.^."));
        System.out.println(p.solution("=.="));
        System.out.println(p.solution("123_.def"));
        System.out.println(p.solution("abcdefghijklmn.p"));
    }
}
