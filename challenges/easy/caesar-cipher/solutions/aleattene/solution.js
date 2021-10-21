/*
JS solution for challenge: "Caesar Cipher"
To test the solution, type from CLI: npm test (required node.js and jest framework)
*/


function encode(originalMessage, shift) {
    let ALPHABET = 26;
    // Ascii Code Lower and Upper Chars
    let LOWER_MIN = 65, LOWER_MAX = 90, UPPER_MIN = 97, UPPER_MAX = 122;
    // Shift normalization (based on the number of characters of the alphabet)
    shift %= ALPHABET;
    // Blank encrypted message
    let encryptedMessage = "";
    // Start encryption
    for (let i = 0; i < originalMessage.length; i++) {
        // Single char of the message
        let char = originalMessage[i];
        // Uppercase char to encrypt
        if ((/[A-Z]/).test(char)) {
            encryptedMessage += charEncryption(char, shift, LOWER_MIN, LOWER_MAX, ALPHABET);
        }
        // Lowercase char to encrypt
        else if ((/[a-z]/).test(char)) {
            encryptedMessage += charEncryption(char, shift, UPPER_MIN, UPPER_MAX, ALPHABET);
        }
        // Special char (not to be encrypted)
        else encryptedMessage += char;
    }
    // Returns the message encrypted according to the Caesar cipher
    return encryptedMessage;
}


function decode(encryptedMessage, shift) {
    // Returns the decrypted (original) message according to the Caesar cipher
    return(encode(encryptedMessage, -shift));
}


function charEncryption(char, shift, limit_min, limit_max, alphabet) {
        // Ascii code of the shifted char
        let shiftedCharAsciiCode = char.charCodeAt(0) + shift;
        // By default the resulting ASCII code is assumed to be within the allowed range
        let asciiCodeRepositioning = 0
        // Checks if the resulting ASCII code is within the allowed range
        if (shiftedCharAsciiCode < limit_min) {
            asciiCodeRepositioning = alphabet;
        }
        else if (shiftedCharAsciiCode > limit_max) {
            asciiCodeRepositioning = -alphabet;
        }
        // Returns the shifted character
        return String.fromCharCode(shiftedCharAsciiCode + asciiCodeRepositioning);
}


// Exports for the tests
module.exports = {
    encode,
    decode
}