var a  = [ 20, 8 , 30, 55 , 64 , 140 , 0 , 1 , 5 , 35 , 43]

console.log(a)

// ascending order

a.sort((x, y) => x - y)

console.log(a)

// descending order

a.sort((x, y) => y - x)

console.log(a)

var b = a.map(x => x * 2)

console.log(b)