import java.util.*;

class Solution {
    
    int timeToInt(String time) {
        String[] t = time.split(":");
        int i = Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
        return i;
    }
    
    
    public int solution(String[][] book_time) {
        int[][] bookTime = new int[book_time.length][2];
        
        // 퇴실 시간 기준 오름차순 정렬
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)-> a[1] - b[1]);

        for(int i = 0; i < book_time.length; i++) {
            bookTime[i][0] = timeToInt(book_time[i][0]);
            bookTime[i][1] = timeToInt(book_time[i][1]) + 10;
        }
        
        Arrays.sort(bookTime, (a, b) -> a[0] - b[0]);

        for(int[] book: bookTime) {
            if(pq.isEmpty()) {
                pq.add(book);
            }
            else {
                // 가장 빠른 종료 시간 확인 (삭제 x)
                int[] time = pq.peek();
                // 시작 시간이 종료 시간보다 크거나 같다면 입실 처리
                if(book[0] >= time[1]) {
                    pq.poll();
                }
                pq.add(book);
                
                
            }
        }
        return pq.size();
    }
}