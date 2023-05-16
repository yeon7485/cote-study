// Lv.2 - 전화번호 목록
import java.util.*;

public class PhoneNumList {
    public boolean solution(String[] phone_book) {
        HashMap<String, Integer> map = new HashMap<>();
        for(int i = 0; i < phone_book.length; i++){
            map.put(phone_book[i], i);
        }
        for(int i = 0; i < phone_book.length; i++){
            for(int j = 1; j < phone_book[i].length(); j++){
                if(map.containsKey(phone_book[i].substring(0, j))) {
                    return false;
                }
            }
            
        }
        return true;
    }
    public static void main(String[] args) {
        PhoneNumList pl = new PhoneNumList();
        String[] arr1 = {"119", "97674223", "1195524421"};
        String[] arr2 = {"123","456","789"};
        String[] arr3 = {"12","123","1235","567","88"};
        System.out.println(pl.solution(arr1));
        System.out.println(pl.solution(arr2));
        System.out.println(pl.solution(arr3));
    }
}
