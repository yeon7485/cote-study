// Lv.1 - 크레인 인형뽑기 게임

import java.util.*;

public class ClawMachineGame {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int m = 0;
        Stack<Integer> stack = new Stack<>();

        for(int i = 0; i < moves.length; i++){
            for(int j = 0; j < board.length; j++){
                m = moves[i] - 1;
                
                if(board[j][m] > 0) {
                    // 스택이 비어있지 않으면서 맨 위의 인형이 뽑은 인형이랑 같으면
                    if(!stack.empty() && stack.peek() == board[j][m]) {
                        stack.pop();
                        answer += 2;
                    }
                    else stack.push(board[j][m]);
                    board[j][m] = 0;
                    break;
                }
            }
        }
        return answer;
    }
    
    public static void main(String[] args) {
        ClawMachineGame cmg = new ClawMachineGame();
        int[][] board = {
            {0, 0, 0, 0, 0}, 
            {0, 0, 1, 0, 3}, 
            {0, 2, 5, 0, 1}, 
            {4, 2, 4, 4, 2}, 
            {3, 5, 1, 3, 1}
        };
        int[] moves = {1, 5, 3, 5, 1, 2, 1, 4};


        System.out.println(cmg.solution(board, moves));
    }
}