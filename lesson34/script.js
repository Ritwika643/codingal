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
const calculate = (p, c, op) => {
    switch(op) {
        case 'addition':
            return p + c;
            case 'subtract':
                return p - c;
                case 'multiply':
                    return p * c;
                    case 'divide':
                        return p / c;
    }
}


operatorButtons.forEach(button => {
    button.addEventListener('click', () => {
   const id = button.id;
    switch(id) { 
        case 'clear':
            currentInput = '';
            previousInput = '';
            operator = null;
            updateDisplay('');
            break;
        case 'backspace':
            currentInput = currentInput.slice(0, -1);
            updateDisplay(currentInput);
        case 'divide':
        case 'multiply':
        case 'subtract':
        case 'addition':
            if (currentInput){
                if (previousInput && operator) {
                    const result = calculate(parseFloat(previousInput), 
                   parseFloat(currentInput), operator);

                   previousInput = result.tostring();
                   updateDisplay(result);
                }else {
                    previousInput = currentInput;

            }
            currentInput = '';
            operator = id;
            }
            break;
        case 'equals':
            if (previousInput && currentInput && operator) {
                const result = calculate(parseFloat(previousInput),
                parseFloat(currentInput), operator);
                updateDisplay(result.toString());
                currentInput = result.toString();
                previousInput = '';
                operator = null;
            }
            break;

    }
})
})