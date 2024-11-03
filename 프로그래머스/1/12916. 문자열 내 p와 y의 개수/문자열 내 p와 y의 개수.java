class Solution {
    boolean solution(String s) {
        int count = 0;
        String str = s.toLowerCase();
        for(int i = 0; i < str.length(); i++) {
            if(str.charAt(i) == 'p') count++;
            else if(str.charAt(i) == 'y') count--;
        }
        
        return count == 0 ? true : false;
    }
}