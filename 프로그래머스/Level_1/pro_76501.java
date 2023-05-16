// LV.1 - 음양 더하기

public class pro_76501 {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        for(int i = 0; i < absolutes.length; i++){
            answer += signs[i] ? absolutes[i] : absolutes[i]*(-1);
        }
        return answer;
    }
    public static void main(String[] args) {
        pro_76501 p = new pro_76501();
        int[] a1 = {4, 7, 12};
        boolean[] s1 = {true,false,true};
        int[] a2 = {1, 2, 3};
        boolean[] s2 = {false,false,true};
        System.out.println(p.solution(a1, s1));
        System.out.println(p.solution(a2, s2));
    }
}