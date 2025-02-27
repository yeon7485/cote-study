import java.util.*;

class Solution {

    public int solution(int alp, int cop, int[][] problems) {
        int max_alp = 0;
        int max_cop = 0;

        // 문제를 모두 풀 수 있는 최대 alp와 cop 구하기
        for(int[] problem : problems) {
            max_alp = Math.max(max_alp, problem[0]);
            max_cop = Math.max(max_cop, problem[1]);
        }
        
        // dp 배열 초기화
        int[][] dp = new int[152][152];
        for (int[] r : dp) {
            Arrays.fill(r, Integer.MAX_VALUE);
        }
        
        // alp, cop가 max_alp, max_cop보다 더 클 수 있기 때문에 초기화 
        alp = Math.min(alp, max_alp);
        cop = Math.min(cop, max_cop);
        
        // 초기값 0
        dp[alp][cop] = 0;
        
                
        for(int i = alp; i <= max_alp; i++) {
            for(int j = cop; j <= max_cop; j++) {
                
                // 알고력 높이기
                dp[i + 1][j] = Math.min(dp[i + 1][j], dp[i][j] + 1);
                // 코딩력 높이기
                dp[i][j + 1] = Math.min(dp[i][j + 1], dp[i][j] + 1);
                
                // 문제 반복
                for(int[] p : problems) {
                    // 문제를 풀 수 있다면
                    if(i >= p[0] && j >= p[1]) {
                        // 문제를 풀고 난 후의 alp, cop 계산
                        int ni = Math.min(i + p[2], max_alp);
                        int nj = Math.min(j + p[3], max_cop);
                        // 현재 시간과 문제를 풀고 난 후 시간 중 작은 걸 저장
                        dp[ni][nj] = Math.min(dp[ni][nj], dp[i][j] + p[4]);
                    }
                }
          
            }
            
        }
        
        return dp[max_alp][max_cop];
    }
}