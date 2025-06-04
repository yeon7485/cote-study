import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    public String solution(String s) {
        String answer = "";
        PriorityQueue<Character> queue = new PriorityQueue<>(Collections.reverseOrder());
        for(int i = 0; i < s.length(); i++) {
            queue.offer(s.charAt(i));
        }
        
        for(int i = 0; i < s.length(); i++) {
            answer += Character.toString(queue.poll());
        }
        return answer;
    }
}