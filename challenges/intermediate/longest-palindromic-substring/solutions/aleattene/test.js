/*
To start the tests, type from CLI: npm test (required node.js and jest framework)
*/

// Import Function to test
const {find_longest_palindromic_substring} = require("./solution.js");

// Tests
test('Longest Palindromic Substring -  Unit Tests', () => {
    expect(find_longest_palindromic_substring('babad')).toBe('bab');
    expect(find_longest_palindromic_substring('cbbd')).toBe('bb');
    expect(find_longest_palindromic_substring('a')).toBe('a');
    expect(find_longest_palindromic_substring('ac')).toBe('a');
    expect(find_longest_palindromic_substring('ale')).toBe('a');
    expect(find_longest_palindromic_substring('1234321')).toBe('1234321');
    expect(find_longest_palindromic_substring('')).toBe('Sorry, you have entered an empty string.');
});