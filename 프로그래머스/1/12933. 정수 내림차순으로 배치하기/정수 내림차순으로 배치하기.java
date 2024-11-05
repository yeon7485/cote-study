import java.util.Arrays;
import java.util.Collections;

class Solution {
    public long solution(long n) {
        String s = Long.toString(n);
        int[] arr = new int[s.length()];
        for(int i = 0; i < s.length(); i++) {
            arr[i] = s.charAt(i) - '0';
        }
        Arrays.sort(arr);
        
        String str = "";
        for(int i = s.length() - 1; i >= 0; i--) {
            str += arr[i];
        }
        
        return Long.valueOf(str);
    }
}