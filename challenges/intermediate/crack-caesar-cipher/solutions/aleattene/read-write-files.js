

// Import modules and functions
const {crackCaesarCipher} = require("./crack-caesar-cipher.js");
fs = require('fs');

// Name of the files to read and write
files = ["Shakespeare-Hamlet.txt", "Shakespeare-Macbeth.txt", "Shakespeare-Romeo-And-Juliet.txt"];

// Start reading and writing files
let i = 0;
while (i < files.length) {

    // Current file to be read and write
    let file =  files[i];

    // File reading
    fs.readFile('../../cases/' + file, 'utf8',
        function (err, data) {
        // Error checking
        if (err) {
            return console.log(err);
        }
        // Successful file reading
        let data_decrypted = crackCaesarCipher(data);

        // Writes the cracked text to a new file
        fs.writeFile("./cracked-files/Cracked-" + file , data_decrypted, 'utf-8',
            function (err) {
            // Error checking
            if (err) {
                return console.log(err);
            }
            // Writing confirmation successful
            console.log("File " + file + " : cracked successfully!");
        })
    });
    i++;
}