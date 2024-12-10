class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        String color = board[h][w];
        
        for (int i = 0; i < 4; i++) {
            int nx = h + dx[i];
            int ny = w + dy[i];
            
            if (0 <= nx && nx < board.length && 0 <= ny && ny < board[0].length){
                if(board[nx][ny].equals(color)) {
                    answer += 1;
                }
            }
        }
        return answer;
    }
}