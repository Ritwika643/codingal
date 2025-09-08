const numberButtons = document.querySelectorAll('.number');
const operatorButtons = document.querySelectorAll('.operator');
const display = document.querySelector('.display');

console.log(numberButtons);
console.log(operatorButtons);

let currentInput = '';
let previousInput = '';
let operator = null;

const updateDisplay = (v) => {
    display.innerHTML = v;
}
numberButtons.forEach(b=> {
     b.addEventListener('click', () => {
        currentInput = currentInput + b.id;
        updateDisplay(currentInput);
     }
    )}
)
   