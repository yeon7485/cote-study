// Lv.1 - 행렬의 덧셈

import java.util.Arrays;

public class SumMatrix {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = {};
        answer = new int[arr1.length][arr1[0].length];
        
        for(int i = 0; i < answer.length; i++){
            for(int j = 0; j < answer[i].length; j++){
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        return answer;
    }

    public static void main(String[] args){
        SumMatrix sm = new SumMatrix();
        int[][] arr1 = new int[][]{{1, 2}, {2, 3}};
        int[][] arr2 = new int[][]{{3, 4}, {5, 6}};
        
        System.out.println(Arrays.deepToString(sm.solution(arr1, arr2)));

    }
}