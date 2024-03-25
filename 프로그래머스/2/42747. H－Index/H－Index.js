function solution(citations) {
    let answer = 0;
    for(let i = 1; i <= citations.length; i++){
        let rst = citations.filter((v) => v >= i)
        if(i <= rst.length){
            answer = i
        }
    }
    return answer;
}