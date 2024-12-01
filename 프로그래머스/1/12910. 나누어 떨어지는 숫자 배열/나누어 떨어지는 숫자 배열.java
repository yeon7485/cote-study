import java.util.ArrayList;

class Solution {
    public ArrayList solution(int[] arr, int divisor) {
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i =0; i < arr.length; i++){
            if(arr[i] % divisor == 0) {
                
                answer.add(arr[i]);
            }
        }
        
        if(answer.size() == 0) {
            answer.add(-1);
        }
        else {
            answer.sort((a, b) -> a - b);
        }
        return answer;
    }
}