const VALID_HEX_KEYS = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f'];
const VALID_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
const VALID_OPERATIONS = ['+', '-', '*', '/', '%', '=']

/**
 * We're going to use these functions all the time and we don't have to worry about binding, so they're all named 
 * TODO: Separate them from the actual controller because right now multiple instances of the calculator overwrite each others global functions
 * This makes no difference to the user but we could be more efficient.
 */

// Converts hexadecimal string to decimal
function strHexToDec(hexStr)  {
    let n = parseInt(hexStr, 16);
    return (isNaN(n) ? "" : n.toString(10));
}

// Converts decimal string to hexadecimal
function strDecToHex(decStr)  {
    let n = parseInt(decStr, 10);
    return (isNaN(n) ? "" : n.toString(16));
}

// Returns true if hexadecimal number is safe, else false
function isHexSafe(hexStr)  {
    // If string is empty or '0x' we just return true because we don't want to clamp
    if (hexStr.length == 0 || (hexStr.length == 2 && hexStr.startsWith("0x"))) return true;
    return Number.isSafeInteger(parseInt(hexStr, 16));
}

// Returns true if decimal number is safe, else false
function isDecSafe(decStr)  {
    // If string is empty we return true because we don't want to clamp
    if (decStr.length == 0) return true;
    return Number.isSafeInteger(parseInt(decStr, 10));
}

/**
 * Defines types of operation
 * Not an Enum but this sounds like the best we can do
 */
const Operation = {
    ADD: 0,
    SUB: 1,
    DIV: 10,
    MUL: 11,
    MOD: 21,
    /**
     * Room for exponents but hopefully they'll never be needed...
     * Just be sure to separate pemdas 'levels' by powers of ten
     */
    CLS: 10000,
    EQL: 20000,
    BAD: -1,
}

const CalculatorMode = {
    HEX: 0,
    DEC: 1
}

const KeyType = {
    DEC: 0,
    HEX: 1,
    OP: 2,
    CLS: 3
}

/**
 *  Controls how operations are performed
 */
class OperationController { 

    constructor(uuid) {
        this.overflow = false;
        this.uuid = uuid
        /**
         * An array of objects
         * Each object has fields { argument: (int), operation: (Operation)}
         */
        this.storedOperations = []
        this.computed = false;

        this.operationDisplay = document.getElementById(uuid('hex-opline'));

    }

    clear() {
        this.computed = false;
        this.storedOperations = [];
    }

    /**
     * Sends argument to operation list
     * argument: number - number to add to the operation
     * keycode: keycode for the operation to perform
     */
    send(arg, keyCode, mode) {
        let op = OperationController.operationToEnum(keyCode);
        if (this.computed === true) {
            if (op === Operation.EQL && this.storedOperations.length > 0) {
                return this.computeResult(mode);
            }
            this.storedOperations = [];
            this.computed = false;
        }
        if (op === Operation.EQL && (this.storedOperations.length == 0 || this.computed == true)) {
            return arg.toString(mode == CalculatorMode.HEX ? 16 : 10);
        }
        this.storedOperations.push({ argument: arg, operation: op })

        if (op === Operation.EQL) {
            let result = this.computeResult(mode);
            this.computed = true;
            return result;
        }

        return "0";
    }

    computeResult(mode) {
        let base = mode === CalculatorMode.HEX ? 16 : 10;
        let result =  OperationController.recursiveComputeResult(this.storedOperations);
        let uuid = this.uuid;
        const overflowIcon = document.getElementById(uuid('hex-overflow-icon'));

        let safeString = "";

        if (result > Number.MAX_SAFE_INTEGER) {
            safeString = "\nThe result was larger than the maximum safe integer number. Results may be innacurate";
        }

        if (result < Number.MIN_SAFE_INTEGER) {
            safeString = "\nThe result was smaller than the minimum safe integer number. Results may be innacurate";
        }

        /* Overflow checks */
        /* Checks are based on number of allowed symbols */
        if (mode === CalculatorMode.HEX) {
            // 12 symbols allowed
            if (result >= Math.pow(16, 12)) {
                overflowIcon.classList.remove(uuid('hex-icon-hidden'));
                $(uuid('#hex-overflow-icon')).attr("data-content", "The result of the operation is bigger than 12 hex digits or 14 decimal digits. Overflow ocurred." + safeString);
                $(uuid('#hex-overflow-icon')).popover("enable");
                result = result % Math.pow(16, 12);
            } else if (result < 0) {
                overflowIcon.classList.remove(uuid('hex-icon-hidden'));
                $(uuid('#hex-overflow-icon')).attr("data-content", "The result of the operation is negative. Underflow ocurred." + safeString);
                $(uuid('#hex-overflow-icon')).popover("enable");
                result = Math.pow(16, 12) + result;
            }
        } else if (mode === CalculatorMode.DEC) {
            // 14 symbols allowed
            if (result >= Math.pow(10, 14)) {
                overflowIcon.classList.remove(uuid('hex-icon-hidden'));
                $(uuid('#hex-overflow-icon')).attr("data-content", "The result of the operation is bigger than 12 hex digits or 14 decimal digits. Overflow ocurred." + safeString);
                $(uuid('#hex-overflow-icon')).popover("enable");
                result = result % Math.pow(10, 14);
            } else if (result < 0) {
                overflowIcon.classList.remove(uuid('hex-icon-hidden'));
                $(uuid('#hex-overflow-icon')).attr("data-content", "The result of the operation is negative. Underflow ocurred." + safeString);
                $(uuid('#hex-overflow-icon')).popover("enable");
                result = Math.pow(10, 14) + result;
            }
        }

        return result.toString(base);
    }

    /**
     * Computes operation with two arguments
     */
    static computeWithTwoArguments(argA, argB, op) {
        switch (op) {
            case Operation.ADD:
                return argA + argB;
            case Operation.SUB:
                return argA - argB;
            case Operation.DIV:
                return Math.floor(argA / argB);
            case Operation.MUL:
                return argA * argB;
            case Operation.MOD:
                return argA % argB;
            default:
                console.error("computeWithTwoArguments(): Invalid operation " + op.toString(10));
                return 0;
        }
    }

    /**
     * Recursive function to compute array of operations
     */
    static recursiveComputeResult(array, carryover = null) {
        const length = array.length;
        if (length == 0)
            console.error("recursiveComputeResult(): Reached end of array without equals (=) operator. Maybe called in the wrong context?");

        if (length == 1)
            return carryover;

        if (carryover === null) {
            carryover = array[0].argument;
        }
        carryover = this.computeWithTwoArguments(carryover, array[1].argument, array[0].operation);
        return this.recursiveComputeResult(array.slice(1), carryover);
    }

    render(mode) {
        let base = mode === CalculatorMode.HEX ? 16 : 10;
        this.operationDisplay.innerText = OperationController.recursiveRender(this.storedOperations, base);
    }

    /**
     * Recursive helper function to enforce PEMDAS
     */
    static recursiveRender(array, base) {

        const length = array.length;
        if (length == 0) 
            return "";
        const id = length - 1;
        if (length == 1)
            return array[id].argument.toString(base) + ' ' + OperationController.enumToSymbol(array[id].operation);
        
        const prev_op = array[id-1].operation;
        const cur_op = array[id].operation;

        /**
         * The funny enum indices are for use here. If the first operation has lower precedence we print parentheses to clarify.
         */
        if (Math.floor(prev_op / 10) < Math.floor(cur_op / 10) && cur_op != Operation.EQL) {
            return "(" + this.recursiveRender(array.slice(0, -1), base) + ' ' + array[id].argument.toString(base) + ") " + OperationController.enumToSymbol(array[id].operation);
        } else {
            return this.recursiveRender(array.slice(0, -1), base) + ' ' + array[id].argument.toString(base) + ' ' + OperationController.enumToSymbol(array[id].operation);
        }  
    }


    /**
     * Converts enum to operation symbol for display
     * Do not use this outside of render functions - it will break
     */
    static enumToSymbol(operationEnum) {

        switch (operationEnum) {
            case Operation.ADD:
                return '+';
            case Operation.SUB:
                return '-';
            case Operation.DIV:
                return '÷';
            case Operation.MUL:
                return '×';
            case Operation.MOD:
                return '%';
            case Operation.EQL:
                return '=';
            default:
                console.error("enumToSymbol(): Invalid operation");
                return '';
        }

    }

    static operationToEnum(operationSymbol) {

        switch (operationSymbol) {
            case '+':
                return Operation.ADD;
            case '-':
                return Operation.SUB;
            case '/':
                return Operation.DIV;
            case '*':
                return Operation.MUL;
            case '%':
                return Operation.MOD;
            case '=':
                return Operation.EQL;
            default:
                console.error("operationToEnum(): Invalid Symbol");
                return Operation.BAD;
        }
    }

    static init(uuid) {
        if (uuid == undefined || uuid === "" || uuid === null) {
            alert("Couldn't fetch uuid... This may be because the question was updated after you opened this variant, so the calculator might not work. Trying a new variant will probably fix this!");
            return;
        }
        if (ready) {
            new CalculatorController(uuid)
        } else {
            window.addEventListener('DOMContentLoaded', (e) => {
                new CalculatorController(uuid)
            }, 'once');
        }
    }
}

/**
 *  Controls the appearance and validation of the input bar, keypad, and translation containers
 */
class InputController {
    /* uuid: function(str) => str + '-' + uuid */
    constructor(uuid) {
        this.firstInput = true
        this.uuid = uuid;
        this.mode = CalculatorMode.HEX;
        this.input = document.getElementById(uuid('hex-calculator-input'));
        this.modeLabels = {
            hex: document.getElementById(uuid('hex-mode-label')),
            dec: document.getElementById(uuid('dec-mode-label'))
        }
        this.modeButtons = {
            hex: document.getElementById(uuid('hex-mode-button')),
            dec: document.getElementById(uuid('dec-mode-button'))
        }
        this.hexOnlyDigits = document.querySelectorAll(uuid('.hex-exclusive-digit'))

        // Event listeners
        this.modeButtons.hex.addEventListener("click", (e) => this.toggleMode(CalculatorMode.HEX));
        this.modeButtons.dec.addEventListener("click", (e) => this.toggleMode(CalculatorMode.DEC));

        // Conversion labels
        let translationLabels = document.querySelectorAll(uuid('.hex-dec-translation-container'))
        this.translationLabels = {
            hex: translationLabels[0],
            dec: translationLabels[1]
        }
        console.log(this.translationLabels)

        /* Input validation */
        this.input.addEventListener('paste', (e) => this.validatePastedInput(e));
        this.input.addEventListener('keypress', (e) => this.validateKeypress(e));
        this.input.addEventListener('input', (e) => this.formatInput(e));
        /* Fix caret in position */
        this.input.addEventListener('click', (e) => {
            const end = this.input.value.length;
            this.input.setSelectionRange(end, end);
            this.input.focus();
        })

        /* Initialize Keypad Listeners */
        this.initializeKeypadListeners();

        /* Initialize overflow popover */
        $(uuid('#hex-overflow-icon')).popover();
        $(uuid('#hex-overflow-icon')).attr("data-content",  "The result of the sum is bigger than 12 hex digits or 14 decimal digits. Overflow ocurred.");
        $(uuid('#hex-overflow-icon')).popover("disable");

        /* Copy button */
        this.copy = document.getElementById(uuid("hex-copy-btn"));
        this.copy.addEventListener('click', (e) => {
            navigator.clipboard.writeText(this.input.value);
        });

        /* Operation Controller */
        this.operationController = new OperationController(this.uuid);
    }

    // Toggles calculator mode, if different
    toggleMode(mode) {
        if (mode === this.mode) return;
        
        let uuid = this.uuid

        switch (mode) {
            case CalculatorMode.HEX:
                this.modeLabels.hex.classList.add(uuid('hex-base-visible'));
                this.modeLabels.dec.classList.remove(uuid('hex-base-visible'));
                for (let digit of this.hexOnlyDigits) {
                    digit.classList.remove(uuid('hex-faded'));
                }
                this.mode = CalculatorMode.HEX;
                this.input.value = strDecToHex(this.input.value);
                break
            case CalculatorMode.DEC:
                this.modeLabels.dec.classList.add(uuid('hex-base-visible'));
                this.modeLabels.hex.classList.remove(uuid('hex-base-visible'));
                for (let digit of this.hexOnlyDigits) {
                    digit.classList.add(uuid('hex-faded'));
                }
                this.mode = CalculatorMode.DEC;
                this.input.value = strHexToDec(this.input.value);
                break
        }
        
        // TODO: Render opline update
        this.operationController.render(this.mode);
    }

    /* Renders the base conversions for each base */
    renderBaseConversions(value) {
        this.translationLabels.hex.firstChild.innerText = "0x" + (isNaN(value) ? "" : value.toString(16));
        this.translationLabels.dec.firstChild.innerText = isNaN(value) ? "" : value.toString(10);
    }

    /* Validates pasted input */
    validatePastedInput(e)  {
        let paste = (e.clipboardData || window.clipboardData).getData('text');
        const hexRegex = new RegExp('[^0123456789AaBbCcDdEeFf]');
        const decRegex = new RegExp('[^0123456789]');
        e.preventDefault();

        /* Strip hex prefix if we paste something */
        if (this.mode == CalculatorMode.HEX && paste.startsWith('0x')) {
            paste = paste.slice(2);
        }
        /* Disallow pasting phrases with bad characters */
        if (this.mode == CalculatorMode.HEX && hexRegex.test(paste) == true)
            return;
        else if (this.mode == CalculatorMode.DEC && decRegex.test(paste) == true)
            return;
        e.target.value = paste;
        /* Dispatch input event to handle different CSS methods */
        this.input.dispatchEvent(new Event('input', {'target': e.target}))
    }

    /* Validates keypress input */
    validateKeypress(e) {
        e.preventDefault();
        let uuid = this.uuid;
        if (VALID_DIGITS.includes(e.key) || (VALID_HEX_KEYS.includes(e.key) && this.mode == CalculatorMode.HEX)) {
            /* Valid input */
            
            /* Prevent hex inputs > 12 */
            if (this.mode == CalculatorMode.HEX && this.input.value.length >= 12)
                return;
            
            /* ...or dec inputs > 14 */
            if (this.mode == CalculatorMode.DEC && this.input.value.length >= 14)
                return;

            if (this.firstInput == true) {
                this.input.value = "";
                $(uuid('#hex-overflow-icon')).addClass(uuid('hex-icon-hidden'));
                $(uuid('#hex-overflow-icon')).popover('disable');
                this.firstInput = false;
            }
            this.input.value += e.key;
            this.input.dispatchEvent(new Event('input', { 'target': this.input }))
        } else if (VALID_OPERATIONS.includes(e.key) || e.key == 'Enter') {
            let argument = parseInt(this.input.value, this.mode == CalculatorMode.HEX ? 16 : 10);
            let operation = e.key == 'Enter' ? '=' : e.key;
            if (operation == '=') this.firstInput = true;
            this.input.value = this.operationController.send(argument, operation, this.mode);
            /* Dispatch input event to trigger conversion recalculation */
            this.input.dispatchEvent(new Event('input', {'target': this.input }));
            this.operationController.render(this.mode)
        }
    }

    /* Confirms input is correct and removes leading zeros */
    formatInput(e) {
        let uuid = this.uuid;
        let base = this.mode == CalculatorMode.HEX ? 16 : 10;
        let inputNumber = parseInt(e.target.value, base);

        /* Reset if backspace pressed until length is zero */
        if (isNaN(inputNumber)) {
            inputNumber = 0;
            this.firstInput = true;
        }

        /* Fade single zero */
        if (inputNumber == 0) {
            if (this.input.classList.contains(uuid('hex-text-fade')) == false) this.input.classList.add(uuid('hex-text-fade'));
        } else {
            if (this.input.classList.contains(uuid('hex-text-fade')) == true) this.input.classList.remove(uuid('hex-text-fade'));
        }

        if (inputNumber > Number.MAX_SAFE_INTEGER)
            inputNumber = Number.MAX_SAFE_INTEGER;

        e.target.value = inputNumber.toString(base); // we do this to remove leading zeroes
        this.renderBaseConversions(inputNumber);
    }

    initializeKeypadListeners() {
        let uuid = this.uuid;

        let clickables = document.querySelectorAll(uuid('.hex-clickable'))
        for (let clickable of clickables) {
            let value = clickable.getAttribute('value');
            /* Digits always accessible */
            if (VALID_DIGITS.includes(value)) {
                clickable.addEventListener('click', this.keypadPressCallback(KeyType.DEC, value));
            } else if (VALID_HEX_KEYS.includes(value)) {
                clickable.addEventListener('click', this.keypadPressCallback(KeyType.HEX, value));
            } else if (VALID_OPERATIONS.includes(value)) {
                clickable.addEventListener('click', this.keypadPressCallback(KeyType.OP, value));
            } else if (value == 'ce') {
                clickable.addEventListener('click', this.keypadPressCallback(KeyType.CLS, value));
            }
        }
    }   
    
    /**
     * Generates callbacks based on keytype
     * An attempt at simplifying the huge block of code we had before
     */
    keypadPressCallback(keytype, value) {
        let uuid = this.uuid;

        switch (keytype) {
            case KeyType.DEC:
                return (e) => {
                    if (this.firstInput == true) {
                        this.input.value = "";
                        $(uuid('#hex-overflow-icon')).addClass(uuid('hex-icon-hidden'));
                        $(uuid('#hex-overflow-icon')).popover("disable");
                        this.firstInput = false;
                    }

                    if ((this.mode == CalculatorMode.HEX && this.input.value.length >= 12) || (this.mode == CalculatorMode.DEC && this.input.value.length >= 14)) {
                        return;
                    }

                    this.input.value += value;
                    /* Dispatch input event to trigger conversion recalculation */
                    this.input.dispatchEvent(new Event('input', {'target': this.input }));
                }
            case KeyType.HEX:
                return (e) => {
                    if (this.mode == CalculatorMode.HEX) {
                        if (this.firstInput == true) {
                            this.input.value = "";
                            $(uuid('#hex-overflow-icon')).addClass(uuid('hex-icon-hidden-'));
                            $(uuid('#hex-overflow-icon')).popover("disable");
                            this.firstInput = false;
                        }

                        if (this.input.value.length >= 12) {
                            return;
                        }

                        this.input.value += value;
                        /* Dispatch input event to trigger conversion recalculation */
                        this.input.dispatchEvent(new Event('input', {'target': this.input }));
                    }
                }
            case KeyType.OP:
                return (e) => {
                    let argument = parseInt(this.input.value, this.mode == CalculatorMode.HEX ? 16 : 10);
                    this.input.value = this.operationController.send(argument, value, this.mode);
                    if (value == '=') this.firstInput = true;
                    this.operationController.render(this.mode);
                    /* Dispatch input event to trigger conversion recalculation */
                    this.input.dispatchEvent(new Event('input', {'target': this.input }));
                }
            case KeyType.CLS:
                return (e) => {
                    this.input.value = "";
                    this.input.dispatchEvent(new Event('input', {'target': this.input}));
                    // TODO: Reset opline
                    // TODO: Re-render operation board
                    this.operationController.clear();
                    this.operationController.render(this.mode);
                    // Hide over/underflow
                    $(uuid('#hex-overflow-icon')).popover("disable");
                    $(uuid('#hex-overflow-icon')).addClass(uuid("hex-icon-hidden"));
                }
        }
    }
    
}


/**
 *  Describes a hex calculator controller
 *  TODO: Probably create some instance constants for attributes with uuid... this got out of hand FAST
 */
class CalculatorController {
    // Takes in the this.uuid, supplied by calculator 
    constructor(uuid) {
        this.uuid = (attr) => attr + '-' + uuid;
        /* Base switch controller */
        this.inputController = new InputController(this.uuid)
    }

    static init(uuid) {
        if (uuid == undefined || uuid === "" || uuid === null) {
            alert("Couldn't fetch uuid... This may be because the question was updated after you opened this variant, so the calculator might not work. Trying a new variant will probably fix this!");
            return;
        }
        if (ready) {
            new CalculatorController(uuid)
        } else {
            // Initialize calculator as soon as everything we need is loaded
            window.addEventListener('DOMContentLoaded', (e) => {
                new CalculatorController(uuid)
            }, 'once');
        }
    }
}

var ready = false;

// Safeguard for when somehow the dom content loads before the init metod

window.addEventListener('DOMContentLoaded', (e) => {
    ready = true
}, 'once');
