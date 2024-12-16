class Solution {
    public int[] solution(int[] arr) {
        int len = 0;
        for(int a: arr) {
            len += a;
        }
        
        int[] answer = new int[len];
        int index = 0;
        for(int a: arr) {
            for(int i = 0; i < a; i++) {
                answer[index] = a;
                index++;
            }
        }
        
        return answer;
    }
}