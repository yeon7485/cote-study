import java.util.Stack;

class Solution {
    boolean solution(String s) {
        Stack<String> stack = new Stack<>();
        
        for(int i = 0; i < s.length(); i++) {
            String str = Character.toString(s.charAt(i));
            if(str.equals("(")) {
                stack.push(str);
            }
            else if(str.equals(")")) {
                if(stack.empty() || stack.peek().equals(str)) {
                    return false;
                }
                else {
                    stack.pop();
                }
            }
            else {
                return false;
            }
        }
        
        return stack.empty() ? true : false;
    }
}