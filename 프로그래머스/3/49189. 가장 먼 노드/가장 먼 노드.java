import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        boolean[] visited = new boolean[n + 1];
        int[] costs = new int[n + 1];
        
        Arrays.fill(visited, false);
        Arrays.fill(costs, Integer.MAX_VALUE);
        
        costs[1] = 0;
        while(true) {
            int min = -1;
            for(int i = 1; i < n + 1; i++) {
                if(!visited[i] && (min == -1 || costs[i] < costs[min])) {
                    min= i;
                }    
            }
            if(min == -1 ) {
                break;
            }
            
            visited[min] = true;
            
            for(int[] e: edge) {
                if(e[0] == min || e[1] == min) {
                    int neighbor = e[0] == min? e[1] : e[0];
                    if(!visited[neighbor]) {
                        int newCost = costs[min] + 1;
                        if(costs[neighbor] > newCost) {
                            costs[neighbor] = newCost;
                        }
                    }
                }
            }
        }
        
        int max = 0;
        for(int i = 2; i < n + 1; i++) {
            max = Math.max(max, costs[i]);
        } 
        
        for(int i = 2; i < n + 1; i++) {
            if(costs[i] == max) {
                answer++;
            }
        }
        
        return answer;
    }
}