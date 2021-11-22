/*
JS solution for challenge: "Longest Palindromic Substring"
To test the solution, type from CLI: npm test (required node.js and jest framework)
*/


function isPalindrome(word) {
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


function generateCombinations(word) {
    // Array that will contain the combinations of characters/substrings
    let combinations = [];
    // Recursive function
    let func = (prefix, word) => {
        for (let i = 0; i < word.length; i++) {
            combinations.push(prefix + word[i]);
            // Recursive call
            func(prefix + word[i], word.slice(i + 1));
        }
    }
    // First call
    func('', word);
    return combinations;
}


function find_longest_palindromic_substring(word){
    // Empty string
    if (word === "") return "Sorry, you have entered an empty string."
    // List of all combinations of characters present in the string, sorted by length (the longest at the top)
    let combinations = generateCombinations(word).sort((w1, w2) => w2.length - w1.length);
    // Start of search for the first longest palindrome string
    let i = 0;
    while (i < combinations.length) {
        if (isPalindrome(combinations[i])) {
            // palindrome substring found
            return combinations[i]
        }
        i++;
    }
    // Check for a possible error
    return "Warning, something went wrong."
}



// Exports for the tests
module.exports = {
    find_longest_palindromic_substring,
}


