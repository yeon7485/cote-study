// Lv.1 - 소수 만들기

public class pro_12977 {
    public int solution(int[] nums) {
        int answer = 0;

        for(int i = 0; i < nums.length; i++){
            for(int j = i + 1; j < nums.length; j++){
                for(int k = j + 1; k < nums.length; k++){
                    if(isPrime(nums[i] + nums[j] + nums[k])) {
                        answer += 1;
                    }
                }
            }
        }
        return answer;
    }

    public boolean isPrime(int n){
        for(int i = 2; i <= n/2; i++){
            if(n % i == 0){
                return false;
            }
        }
        return true;
    }



    public static void main(String[] args) {
        pro_12977 p = new pro_12977();
        int[] nums1 = {1,2,3,4};
        int[] nums2 = {1,2,7,6,4};
        System.out.println(p.solution(nums1));
        System.out.println(p.solution(nums2));
    }
}
