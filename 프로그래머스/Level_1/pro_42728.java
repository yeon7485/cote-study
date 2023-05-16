// Lv.1 - K번째 수

import java.util.Arrays;

public class Kth_Number {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int n = 0;
        for(int[] c : commands){
            int[] a = new int[c[1]-c[0]+1];
            for(int i = c[0] - 1, j = 0; i < c[1]; i++, j++){
                a[j] = array[i];
            }
            
            Arrays.sort(a);
            answer[n++] = a[c[2] - 1];
        }

        return answer;
    }

    public static void main(String[] args) {
        Kth_Number kn = new Kth_Number();
        int[] array = {1, 5, 2, 6, 3, 7, 4};
        int[][] commands = {   
            {2, 5, 3},
            {4, 4, 1},
            {1, 7, 3}
        };

        System.out.println(Arrays.toString(kn.solution(array, commands)));
    }
}
