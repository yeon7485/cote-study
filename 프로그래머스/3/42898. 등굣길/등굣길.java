class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] dp = new int[n][m];
        dp[0][0] = 1;
            
        for(int[] pud : puddles) {
            dp[pud[1] - 1][pud[0] - 1] = -1;
        }
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(dp[i][j] == -1) {
                    continue;
                }
                
                if(i != 0 && dp[i - 1][j] != -1) {
                    dp[i][j] += dp[i - 1][j];
                }
                if(j != 0 && dp[i][j - 1] != -1) {
                    dp[i][j] += dp[i][j - 1];
                }
                dp[i][j] %= 1000000007;
            }
        }
        
        return dp[n-1][m-1];
    }
}