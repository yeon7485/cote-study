function solution(park, routes) {
    let answer = [];
    let row = park.findIndex((s) => s.includes("S"))
    let col = park[row].indexOf("S")
    
    routes.forEach((position) => {
        const [d, n] = position.split(" ")
        
        let tempRow = row;
        let tempCol = col;
        let flag = true;
        
        for(let i = 0; i < Number(n); i++){
            if (d === "E") tempCol++;
            else if (d === "W") tempCol--;
            else if (d === "S") tempRow++;
            else if (d === "N") tempRow--;
        
            if(
                tempRow >= park.length ||
                tempRow < 0 || tempCol < 0 ||
                tempCol >= park[0].length ||
                park[tempRow][tempCol] === "X"){
                flag = false;
                break;
            }
        }
        
        if(flag) {
            col = tempCol;
            row = tempRow;
        }
        
    })
        return [row, col];
}