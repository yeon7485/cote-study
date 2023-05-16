import java.util.*;

// Lv.2 - 가장 큰 수

public class BiggestNumber {
    public String solution(int[] numbers) {
        String answer = "";
        String[] num = new String[numbers.length];
    
        for(int i = 0; i < num.length; i++){
            num[i] = String.valueOf(numbers[i]);
        }
    
        Arrays.sort(num, new Comparator<String>(){
            @Override
            public int compare(String o1, String o2) {
                return (o2+o1).compareTo(o1+o2);
            }
        });
    
        for(int i = 0; i < num.length; i++){
            if(num[0].equals("0")) return "0";
            else answer += num[i];
        }
    
        return answer;
    }
    public static void main(String[] args) {
        BiggestNumber bn = new BiggestNumber();
        int[] arr1 = {6, 10, 2};
        int[] arr2 = {3, 30, 34, 5, 9};
        int[] arr3 = {23, 232, 21, 212};
        System.out.println(bn.solution(arr1));
        System.out.println(bn.solution(arr2));
        System.out.println(bn.solution(arr3));
    }
}
