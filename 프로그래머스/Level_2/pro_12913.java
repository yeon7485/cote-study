// Lv.2 - 땅따먹기 

public class EatLand {
    int solution(int[][] land) {
        int answer = 0;
        int max = 0;
        
        for(int i = 1; i < land.length; i++) {
        	for(int j = 0; j < 4; j++) {
        		if(j == 0) {
        			max = Math.max(land[i-1][1], land[i-1][2]);
        			land[i][j] += Math.max(max, land[i-1][3]);
        		}
        		else if(j == 1) {
        			max = Math.max(land[i-1][0], land[i-1][2]);
        			land[i][j] += Math.max(max, land[i-1][3]);
        		}
        		else if(j == 2) {
        			max = Math.max(land[i-1][0], land[i-1][1]);
        			land[i][j] += Math.max(max, land[i-1][3]);
        		}
        		else if(j == 3) {
        			max = Math.max(land[i-1][0], land[i-1][1]);
        			land[i][j] += Math.max(max, land[i-1][2]);
        		}
        	}
        }
        
        for(int i = 0; i < 4; i++) {
        	answer = Math.max(answer, land[land.length-1][i]);
        }
  
        return answer;
    }

    public static void main(String[] args){
        EatLand el = new EatLand();
        int[][] arr1 = new int[][]{{1, 2, 3, 5}, {5, 6, 7, 8}, {4, 3, 2, 1}};
        int[][] arr2 = new int[][]{{1, 2, 3, 5}, {5, 6, 7, 100}, {4, 3, 2, 1}};
        System.out.println((el.solution(arr1)));
        System.out.println((el.solution(arr2)));
    }
}
