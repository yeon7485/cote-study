// Lv.1 - 2016년

public class pro_12901 {
    public String solution(int a, int b) {
        String answer = "";
        int days = b;
        int[] month = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String[] day = {"THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"};
        while(a > 1){
            days += month[a-2]; 
            a--; 
        }
        answer = day[days % 7];
        return answer;
    }
    public static void main(String[] args) {
        pro_12901 y = new pro_12901();
        System.out.println(y.solution(5, 24));
    }
}
