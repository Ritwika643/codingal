var a = 'Hello, World!';
var b = 42;
var c = [50, 60, 70, 80];
var d = ['Apple', 'Banana', 'Cherry'];

console.log(c[1]); 
console.log(d[2]);

console.log(a);

 var e = c.join(' - ');
console.log(e);

d.push('watermelon');
console.log(d)

function sum(a,b,c){
    return a + b + c;
}

function average(a,b,c){
    return (a + b + c) / 3;
} 

var result = average(100, 200, 30);
console.log(result);