import java.util.HashMap;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length] ;
        
        HashMap<Character, Integer> min_index = new HashMap<>();
        
        for (String key : keymap) {
            for (int i = 0; i < key.length(); i++) {
                char ch = key.charAt(i); 
                if (!min_index.containsKey(ch) || i < min_index.get(ch)) {
                    min_index.put(ch, i + 1);
                }
            }
        }
        
        
        for (int i = 0; i < targets.length; i++) {
            char[] arr = targets[i].toCharArray();
            for(char ch : arr) {
                if(min_index.containsKey(ch)) {
                    answer[i] += min_index.get(ch);
                }
                else {
                    answer[i] = -1;
                    break;
                }
            }
        } 
        
        return answer;
    }
}