class Solution {
    public int answer = 0;
    
    public void dfs(int i, int sum, int[] numbers, int target) {
        if(i == numbers.length) {
            if(sum == target) {
                answer += 1;
            }
            return;
        }
        dfs(i + 1, sum + numbers[i], numbers, target);
        dfs(i + 1, sum - numbers[i], numbers, target);
    }
    
    public int solution(int[] numbers, int target) {
    
        dfs(0, 0, numbers, target);
        return answer;
    }
    
}