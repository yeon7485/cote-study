import java.util.HashMap;


// Lv.1 - 완주하지 못한 선수

public class NotFinishPlayer {
    public String solution(String[] participant, String[] completion) {
        String answer = "";

        HashMap<String, Integer> map = new HashMap<String, Integer>();
        
        // map에 참여한 선수들 넣어주기
        for(String p : participant){
            // 동명이인이면 1씩 추가
            if(map.containsKey(p)){
                map.replace(p, map.get(p) + 1);
            }
            else{
                map.put(p, 1);
            }
        }

        // 완주한 선수 -1 해주기
        for(String c : completion){
            if(map.get(c) > 0){
                map.replace(c, map.get(c) - 1);
            }
        }
        
        for(String key : map.keySet()){
            if(map.get(key) > 0){
                answer = key;
            }
        } 
        return answer;
    }

    public static void main(String[] args) {
        NotFinishPlayer nfp = new NotFinishPlayer();

        String[] p1 = {"leo", "kiki", "eden"};
        String[] c1 = {"eden", "kiki"};
        String[] p2 = {"marina", "josipa", "nikola", "vinko", "filipa"};
        String[] c2 = {"josipa", "filipa", "marina", "nikola"};
        String[] p3 = {"mislav", "stanko", "mislav", "ana"};
        String[] c3 = {"stanko", "ana", "mislav"};

        System.out.println(nfp.solution(p1, c1));
        System.out.println(nfp.solution(p2, c2));
        System.out.println(nfp.solution(p3, c3));
    }
}