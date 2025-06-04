class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
        for(long i = 1; i <= count; i++) {
            answer += price * i;
        }
        answer = answer - money;
        if(answer < 0) return 0;
        return answer;
    }
}