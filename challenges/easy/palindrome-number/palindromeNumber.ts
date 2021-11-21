function is_palindrome_int (int: number) {
    
    let i: number = 0;
    let j: number = int.toString().length - 1;

    while (j >= 0) {
        if (int.toString()[i] !== int.toString()[j]) {
            return false
        }
        i += 1;
        j -= 1;
    }

    return true
}

console.log(is_palindrome_int(1010101));     // True
console.log(is_palindrome_int(101));         // True
console.log(is_palindrome_int(1101));        // False
console.log(is_palindrome_int(122));         // False
console.log(is_palindrome_int(-1101));       // False