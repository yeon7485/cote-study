import java.util.*;

class Solution {
    public int[] findPath(int n, int[][]fares, int start) {
        boolean[] visited = new boolean[n + 1];
        int[] costs = new int[n + 1];
     
        Arrays.fill(visited, false);
        Arrays.fill(costs, Integer.MAX_VALUE);
        
        costs[start] = 0;
        
        while(true) {
            int min = -1;
            for(int i = 1; i < n + 1; i++) {
                if(!visited[i] && (min == -1 || costs[i] < costs[min])) {
                    min = i;
                }
            }
            
            if(min == -1) {
                break;
            }
            
            visited[min] = true;
            
            for(int[] edge: fares) {
                if(edge[0] == min || edge[1] == min) {
                    int neighbor = edge[0] == min ? edge[1]:edge[0];
                    
                    if(!visited[neighbor] ) {
                        int newCost = costs[min] + edge[2];
                        if(costs[neighbor] > newCost) {
                            costs[neighbor] = newCost;
                        }
                    }
                }
            } 
        }
        
        return costs;
    }
    
    
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = Integer.MAX_VALUE;
        
        int[] costS = findPath(n, fares, s);
        int[] costA = findPath(n, fares, a);
        int[] costB = findPath(n, fares, b);
        
        
        for(int i = 1; i < n + 1; i++) {
            int cost = costS[i] + costA[i] + costB[i];
            if(cost > 0 && answer > cost) {
                answer = cost;
            }
        }
        
        return answer;
    }
}