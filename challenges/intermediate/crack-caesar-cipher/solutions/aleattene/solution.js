/*
JS solution for challenge: "Crack Caesar Cipher"
To test the solution, type from CLI: node solution.js (required node.js)
*/


const {decode} = require("./encode_decode.js");
fs = require('fs');

// Name of the files to crack
files = ["Shakespeare-Hamlet.txt", "Shakespeare-Macbeth.txt", "Shakespeare-Romeo-And-Juliet.txt"];

// Theoretical frequency of characters present in a text written in English
let theoreticalFrequency = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094,
    'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406,  'n': 6.749, 'o': 7.507, 'p': 1.929,
    'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758,  'v': 0.978, 'w': 2.360, 'x': 0.150,
    'y': 1.974, 'z': 0.074
};

let i = 0;
while (i < files.length) {

    // Data Structures for the occurrence of characters and their real frequency in the analyzed text
    let occurrences = {}, realFrequency = {}

    // Current file to be cracked
    let file =  files[i]

    // File reading
    fs.readFile('../../cases/' + file, 'utf8',
        function (err, data) {
            // Error checking
            if (err) {
                return console.log(err);
            }
            // Successful file reading
            else {
                let numChars = 0;
                let j = 0;
                while (j < data.length) {
                    let current_char = data[j].toLowerCase()
                    if (current_char in theoreticalFrequency) {
                        numChars += 1;
                        if (current_char in realFrequency) {
                            occurrences[current_char] += 1
                        } else {
                            occurrences[current_char] = 1
                        }
                        realFrequency[current_char] = occurrences[current_char] / numChars
                    }
                    j++;
                }

                // Array of the frequency values
                let values = Object.keys(realFrequency).map(key => realFrequency[key]);

                // Value of the frequency max
                let value = Math.max.apply(Math, values);

                // Character corresponding to the maximum frequency value
                let char = (getKeyByValue(realFrequency, value));

                // Difference between more frequent char in the text and char "e" (most frequent in English texts)
                let shift = char.charCodeAt(0) - "e".charCodeAt(0)

                // Writes the cracked text to a new file
                fs.writeFile("./cracked-files/Cracked-" + file , decode(data, shift), 'utf-8',
                    function (err) {
                        // Error checking
                        if (err) {
                            return console.log(err);
                        }
                        // Writing confirmation successful
                        console.log("File " + file + " : cracked successfully!");
                    })
            }
        });
    i++;
}


// This function acts on an object, returning the specific key corresponding to a certain value
function getKeyByValue(object, value) {
    return Object.keys(object).find(key => object[key] === value);
}