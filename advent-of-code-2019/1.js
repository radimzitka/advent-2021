const fs = require('fs');

let numbers = fs.readFileSync('1.input').toString().trim().split('\n');

let sum = 0;
numbers.forEach(number => sum += Math.floor(number / 3) - 2);
console.log("Part one: " + sum);

sum = 0
let ans = 0
numbers.forEach(number => {
    while(true){
        ans = Math.floor(number / 3) - 2;
        if(ans > 0){
            sum += ans;
            number = ans;
        } else{
            break
        }
    }
})

console.log("Part two: " + sum);



