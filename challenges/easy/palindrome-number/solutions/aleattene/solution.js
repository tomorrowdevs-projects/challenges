/*
JS solution for challenge: "Palindrome Number"
To test the solution, type from CLI: npm test (required node.js and jest framework)
*/


function isPalindrome(number) {
    // From number to string
    let word = number.toString()
    // Shift indexes (left and right)
    let i = 0;
    let j = word.length - 1;
    // Returns false as soon as two different values are found
    while (i <= j) {
         if (word[i] !== word[j]) {
             // The number is not palindrome
             return false;
         }
         i++; j--;
    }
    // The number is palindrome
    return true;
}



// Exports for the tests
module.exports = {
    isPalindrome,
}
