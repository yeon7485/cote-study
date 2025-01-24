import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        boolean[] visited = new boolean[N + 1];
        int[] costs = new int[N + 1];
        
        Arrays.fill(visited, false);
        Arrays.fill(costs, Integer.MAX_VALUE);
        
        costs[1] = 0;
        while(true) {
            int min = -1;
            for(int i = 1; i < N + 1; i++) {
                if(!visited[i] && (min == -1 || costs[min] > costs[i])) {
                    min = i;
                }
            }
            if(min == -1) {
                break;
            }
            visited[min] = true;
            
            
            for(int[] edge: road) {
                if(edge[0] == min || edge[1] == min) {
                    int neighbor = edge[0] == min ? edge[1] : edge[0];
                    if(!visited[neighbor]) {
                        int newCost = costs[min] + edge[2];
                        if(newCost < costs[neighbor]) {
                            costs[neighbor] = newCost;
                        }
                    }
                }
            }
        }
        
        for(int cost: costs) {
            if(cost <= K) {
                answer++;
            }
        }

        return answer;
    }
}