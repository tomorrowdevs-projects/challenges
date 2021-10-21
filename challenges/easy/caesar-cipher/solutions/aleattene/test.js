/*
To start the tests, type from CLI: npm test (required node.js and jest framework)
*/

// Import Functions
const {encode, decode} = require("./solution.js");

// Tests for Encode Function
test('Caesar\'s Cipher -  Encode Function - Unit Tests', () => {
    expect(encode('Hello, World!', 7)).toBe('Olssv, Dvysk!');
    expect(encode('I love pizza.', -7)).toBe('B ehox ibsst.');
    expect(encode('HytyQapgnr kyicq qclqc. Qmkcrgkcq.', 50)).toBe('FwrwOynelp iwgao oajoa. Okiapeiao.');
    expect(encode('abc', 24)).toBe('yza');
});

// Tests for Decode Function
test('Caesar\'s Cipher -  Decode Function - Unit Tests', () => {
    expect(decode('CxvxaaxfMneb Axltb!', 9)).toBe('TomorrowDevs Rocks!');
    expect(decode('Gtdflw Defotz Nzop td rcple!!!', -15)).toBe('Visual Studio Code is great!!!');
    expect(decode('Buj\'i mhyju jxu syfxuh.', 120)).toBe('Let\'s write the cipher.');
    expect(decode('Vriwzduh Hqjlqhhulqj', 3)).toBe('Software Engineering');
});