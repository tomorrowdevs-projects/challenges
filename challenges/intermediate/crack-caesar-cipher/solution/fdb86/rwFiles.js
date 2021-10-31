"use strict";
exports.__esModule = true;
var hack_caesar_1 = require("./hack-caesar");
var fs = require('fs');
var folder = '../../cases/';
var books = ['Shakespeare-Hamlet.txt', 'Shakespeare-Macbeth.txt', 'Shakespeare-Romeo-And-Juliet.txt'];
function decryptFiles(path) {
    fs.readFile(path, 'utf8', function (err, data) {
        if (err) {
            console.error(err);
            return;
        }
        var decrypted_data = (0, hack_caesar_1.crackCaesar)(data);
        fs.writeFile(path.slice(0, -4) + '-decrypted.txt', decrypted_data, function (err) {
            if (err) {
                console.error(err);
                return;
            }
            console.log('file written successfully');
        });
    });
}
for (var i in books) {
    decryptFiles(folder + books[i]);
}
