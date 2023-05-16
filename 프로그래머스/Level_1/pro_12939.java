// Lv.2 - 최댓값과 최솟값

public class pro_12939{
    public String solution(String s) {
        String answer = "";
        String[] arr = s.split(" ");
        int min = Integer.parseInt(arr[0]);
        int max = Integer.parseInt(arr[0]);
        for(String a : arr){
            int x = Integer.parseInt(a);
            if(x > max){
                max = x;
            }
            if(x < min){
                min = x;    
            }
        }
        
        answer = String.valueOf(min) + " " + String.valueOf(max);
        return answer;
    }

    public static void main(String[] args) {
        pro_12939 p = new pro_12939();
        System.out.println(p.solution("1 2 3 4"));
        System.out.println(p.solution("-1 -2 -3 -4"));
        System.out.println(p.solution("-1 -1"));
    }
}