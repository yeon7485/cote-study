import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        
        Deque<int[]> deque = new LinkedList<>();
    
        deque.add(new int[]{0,0});
        
        while(!deque.isEmpty()) {
            int[] n = deque.pop();
            for(int i = 0; i < 4; i++) {
                int nx = dx[i] + n[0];
                int ny = dy[i] + n[1];
                
                if(nx < 0 || nx >= maps.length || ny < 0 || ny >= maps[0].length){
                    continue;
                }
                if(maps[nx][ny] == 0) {
                    continue;
                }
                if(maps[nx][ny] == 1) {
                    maps[nx][ny] = maps[n[0]][n[1]] + 1;
                    deque.add(new int[]{nx, ny});
                }
            }
        }
        
        answer = maps[maps.length - 1][maps[0].length - 1];
        
        return answer > 1 ? answer : -1;

    }
}