// Lv.1 - 숫자 문자열과 영단어

function solution(s) {
    var answer = "";
    const number = ["zero", "one","two","three","four","five","six","seven","eight","nine"];
    let word = "";

    for(let i = 0; i < s.length; i++){
        if(isNaN(parseInt(s[i]))){
            word += s[i];
        }
        else{
            answer += s[i];
        }
        if(number.includes(word)){
            answer += number.indexOf(word);
            word = "";
        }
    }

    answer = parseInt(answer);
    return answer;
}

const s1 = "one4seveneight";
const s2 = "23four5six7";
const s3 = "2three45sixseven"
const s4 = "123"

console.log(solution(s1));
console.log(solution(s2));
console.log(solution(s3));
console.log(solution(s4));