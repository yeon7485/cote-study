import java.util.*; 

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String, Integer> map = new HashMap<>();
        
        for(String p : participant) {
            if(map.containsKey(p)) {
                map.replace(p, map.get(p) + 1);
            }
            else {
                map.put(p, 1);
            }
        }
        
        for(String c : completion) {
            if(map.get(c) > 0) {
                map.replace(c, map.get(c) - 1);
            }
        }
        
        for(String key : map.keySet()) {
            if(map.get(key) > 0) {
                return key;
            }
        }
        
        return answer;
    }
}