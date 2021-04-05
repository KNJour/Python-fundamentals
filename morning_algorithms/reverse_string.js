
function reverseIt(str) {
var result = "";

for (var i = str.length - 1; i >= 0 ; i--) {
    result += str[i];
}
return result;
}

var answer = reverseIt("creature");
console.log(answer);
