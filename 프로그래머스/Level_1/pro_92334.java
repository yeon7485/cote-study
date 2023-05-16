// Lv.1 - 신고 결과 받기

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class pro_92334 {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        HashMap<String, ArrayList<String>> map = new HashMap<>();
        HashMap<String, Integer> countMap = new HashMap<>();
        ArrayList<String> stop = new ArrayList<>();

        for(String id: id_list){
            ArrayList<String> list = new ArrayList<>();
            map.put(id, list);
            countMap.put(id, 0);
        }

        // 유저가 신고한 아이디, 신고 당한 횟수 저장
        for(String r: report){
            String[] rep = r.split(" ");
            ArrayList<String> list = map.get(rep[0]);
            if(!list.contains(rep[1])){
                list.add(rep[1]);
                countMap.put(rep[1], countMap.get(rep[1])+1);
            }
            map.put(rep[0], list);
        }

        // k번 이상 신고 당한 아이디 저장
        for(String id: id_list){
            if(countMap.get(id) >= k){
                stop.add(id);
            }
        }

        // 메일 보낼 횟수 
        for(int i = 0; i < id_list.length; i++){
            answer[i] = 0;
            ArrayList<String> list = map.get(id_list[i]);
            for(String s: stop){
                if(list.contains(s)){
                    answer[i] += 1;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        pro_92334 p = new pro_92334();
        String[] id1 = {"muzi", "frodo", "apeach", "neo"};
        String[] report1 = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
        String[] id2 = {"con", "ryan"};
        String[] report2 = {"ryan con", "ryan con", "ryan con", "ryan con"};
        System.out.println(Arrays.toString(p.solution(id1, report1, 2)));
        System.out.println(Arrays.toString(p.solution(id2, report2, 3)));
    }
}
