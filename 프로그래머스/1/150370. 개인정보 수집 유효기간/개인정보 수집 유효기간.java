import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        ArrayList<Integer> answer = new ArrayList<>();
        int t_year = 0;
        int t_month = 0;
        int t_day = 0;
        Map<String, Integer> map = new HashMap<>();
        
        String[] tdy = today.split("\\.");
        t_year = Integer.parseInt(tdy[0]);
        t_month = Integer.parseInt(tdy[1]);
        t_day = Integer.parseInt(tdy[2]);
        
        
        for(int i = 0; i < terms.length; i++) {
            String t[] = terms[i].split(" ");
            map.put(t[0], Integer.parseInt(t[1]));
        }
        
        
        
        for(int i = 0; i < privacies.length; i++) {
            String priv[] = privacies[i].split(" ");
            int tm = map.get(priv[1]);
            String[] date = priv[0].split("\\.");
            int year = Integer.parseInt(date[0]);
            int month = Integer.parseInt(date[1]);
            int day = Integer.parseInt(date[2]);
            
            year += tm / 12;
            month += tm % 12;
            
            // 12월이 넘어갈 경우 처리
            if(month > 12) {
                year += month / 12;
                month = month % 12;
            }
            
            day -= 1;
            if(day == 0) {
                day = 28;
                month -= 1;
            }
            
            // month가 0일 경우 처리
            if(month == 0) {
                year -= 1;
                month = 12;
            }
            
            
            
            if(t_year > year) {
                answer.add(i + 1);
                continue;
            } 
            else if(t_year < year) {
                continue;
            }
            else {
                if(t_month > month) {
                    answer.add(i + 1);
                    continue;
                }
                else if(t_month < month) {
                    continue;
                }
                else {
                    if(t_day > day) {
                        answer.add(i + 1);
                        continue;
                    }
                    else  {
                        continue;
                    }
                }
            }
            
        }
        
        int[] result = new int[answer.size()];
        for(int i = 0; i < answer.size(); i++) {
            result[i] = answer.get(i);
        }

        return result;
    }
}