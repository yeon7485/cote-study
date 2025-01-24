import java.util.Arrays;

class Solution {
    public boolean[][] floydWarshall(int n, int[][] graph) {
        boolean[][] fight = new boolean[n + 1][n + 1];
        
        for(int i = 1; i < n + 1; i++) {
            for(int j = 1; j < n + 1; j++) {
                if(i == j) {
                    fight[i][j] = true;
                }
                else{
                    fight[i][j] = false;
                }
            }
        }
        for(int[] edge: graph) {
            fight[edge[0]][edge[1]] = true;
        }
        
        for(int k = 1; k < n + 1; k++) {
            for(int i = 1; i < n + 1; i++) {
                for(int j = 1; j < n + 1; j++) {
                    fight[i][j] = fight[i][k] && fight[k][j] || fight[i][j];
                    
                }
            }
        }

        return fight;
    }
    
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        boolean[][] fight = floydWarshall(n, results);
        
        for(int i = 1; i < n + 1; i++) {
            boolean check = true;
            for(int j = 1; j < n + 1; j++) {
                check = check && (fight[i][j] || fight[j][i]);
            }
            if(check) answer++;
        }


        return answer;
    }
}