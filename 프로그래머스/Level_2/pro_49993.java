// Lv.2 - 스킬트리

public class SkillTree {
    public int solution(String skill, String[] skill_trees){
        int answer = 0;
        String[] st = new String[skill_trees.length];

        // 배열 깊은 복사
        for(int i = 0; i < skill_trees.length; i++){
            st[i] = skill_trees[i];
        }
        
        boolean tf = true;
        
        for(int i = 0; i < skill_trees.length; i++){
            // skill에 들어가지 않는 스킬들 ""로 replace 해주기
            for(int j = 0; j < skill_trees[i].length(); j++){
                String s = Character.toString(skill_trees[i].charAt(j));
                if(!skill.contains(s)){
                    st[i] = st[i].replace(s, "");
                }
            }
            
            // 스킬트리 순서 확인
            for(int k = 0; k < st[i].length(); k++){
                String s = Character.toString(st[i].charAt(k));
                if(skill.indexOf(s) != k) {
                    tf = false;
                    break;
                }
            }

            if(tf == true) answer++;
            else if(st[i].equals("")) answer++;

            // 변수 초기화
            tf = true;
        }
        return answer;
    }

    public static void main(String[] args){
        SkillTree st = new SkillTree();
        
        String skill1 = "CBD";
        String[] skill_trees1 = {"BACDE", "CBADF", "AECB", "BDA"};

        String skill2 = "CBDK";
        String[] skill_trees2 = {"CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"};

        System.out.println(st.solution(skill1, skill_trees1));
        System.out.println(st.solution(skill2, skill_trees2));

    }
}
