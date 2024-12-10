class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        
        char[] dart = dartResult.toCharArray();
        int[] score = new int[3];
        
        int index = -1;
        
        for (int i = 0; i < dart.length; i++) {
            if('0' <= dart[i] && dart[i] <= '9') {
                index++;
                score[index] = Character.getNumericValue(dart[i]);
                
                if(dart[i + 1] == '0') {
                    score[index] = 10;
                    i++;
                }
                
            }
            else if(dart[i] == 'D') {
                score[index] = (int)Math.pow(score[index], 2);
            }
            else if(dart[i] == 'T') {
                score[index] = (int)Math.pow(score[index], 3);
            }
            else if(dart[i] == '*') {
                score[index] *= 2;
                if(index > 0) {
                    score[index - 1] *= 2;
                }
            }
            else if(dart[i] == '#') {
                score[index] *= -1;
            }
        }
        
        for(int s : score) {
            answer += s;
        }
        
        return answer;
    }
}