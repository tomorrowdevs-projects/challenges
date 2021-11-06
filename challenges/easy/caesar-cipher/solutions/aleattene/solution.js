/*
JS solution for challenge: "Caesar Cipher"
To test the solution, type from CLI: npm test (required node.js and jest framework)
*/


function encode(originalMessage, shift) {
    // This function returns the message encrypted according to the Caesar cipher
    let CHARS = 26;
    return originalMessage.split("").map(char => {
        // Lowercase char to encrypt
        if (char >= "a" && char <= "z") {
            return String.fromCharCode(97 + (((char.charCodeAt(0) - 97) + (CHARS + (shift % CHARS))) % CHARS));
        }
        // Uppercase char to encrypt
        else if (char >= "A" && char <= "Z") {
            return String.fromCharCode(65 + (((char.charCodeAt(0) - 65) + (CHARS + (shift % CHARS))) % CHARS));
        }
        // Special char (not to be encrypted)
        else return char;
    }).join("");
}


function decode(encryptedMessage, shift) {
    // This function returns the decrypted (original) message according to the Caesar cipher
    return(encode(encryptedMessage, -shift));
}


// Exports for the tests
module.exports = {
    encode,
    decode
}
