var a = {username:' xyz', password: '1234'}
console.log(a)

var b = JSON.stringify(a);
console.log(b)

var c = JSON.parse(b);
console.log(c)

function klm () {
    console.log('klm function called');
}
const p = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('Promise resolved');
    }, 2000);
}
pconst p = new Promise(function(resolve, reject){

setTimeout(function(){

resolve("finally ferrari bought")

}, 4000)

})

p.then((m)=>{

console.log("then block")

console.log(m)

}).catch((er)=>{

console.log("catch block")

console.log(er)

})
function abc () { 
    console.log('this is fun');
    klm();
    console.log('hello world')
}
abc();