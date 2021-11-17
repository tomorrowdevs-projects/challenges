/*
To start the tests, type from CLI: npm test (required node.js and jest framework)
*/

// Import Functions
const {isPalindrome} = require("./solution.js");

// Tests for isPalindrome Function
test('Palindrome Number - Unit Tests', () => {
    expect(isPalindrome(121)).toBe(true);
    expect(isPalindrome(-121)).toBe(false);
    expect(isPalindrome(10)).toBe(false);
    expect(isPalindrome(-101)).toBe(false);
    expect(isPalindrome(12321)).toBe(true);
    expect(isPalindrome(123456)).toBe(false);
    expect(isPalindrome(0)).toBe(true);
    expect(isPalindrome(1111111111111111)).toBe(true);
});