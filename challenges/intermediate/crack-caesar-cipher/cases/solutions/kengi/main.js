let alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",];
let alphabetCapital = alphabet.map((x) => x.toUpperCase());

// Requiring fs module in which
// readFile function is defined.
const fs = require('fs')
import {decode} from "./solutionWithProxy.js"  

let text = []
const readFileLines = filename =>
   fs.readFileSync(filename)
   .toString('UTF8')
   .toLowerCase()
   .split("");

// Calling the readFiles function with file name
// let words = readFileLines('../../Shakespeare-Macbeth.txt'); // key = 4
// let words = readFileLines('../../Shakespeare-Romeo-And-Juliet.txt'); // key = 12
let words = readFileLines('../../Shakespeare-Hamlet.txt'); // key = 20



// Printing the response array
let occurrences = {};
for (let i = 0; i < words.length; i++) {
    const word = words[i];
    if (alphabet.includes(word)){
    if(occurrences[word]) {
        occurrences[word] += 1
    }
    else {
        occurrences[word] = 1
    }}
}

// FROM DIFFERENT RESOURCES LETTER "E" IS THE ONE THAT APPEARS THE MOST ON AVERAGE IN A LONG ENGLISH TEXT

let mostFrequentLetterInEnglish = "e"

//TAKE ALL THE LETTERS AND THEIR OCCURENCIES, SORT THEM AND GRAB THE LETTER THAT OCCURS THE MOST

const topLetterInText = Object.entries(occurrences).sort((a,b) => b[1] - a[1])[0][0]

console.log(topLetterInText);

// THE DIFFERENCE BETWEEN THE POSITION OF THE MOST FREQUENT LETTER IN TEXT WITH THE POSITION
// OF THE MOST FREQUENT LETTER IN ENGLISH IS OUR KEY TO DECODE THE TEXT

let key = alphabet.indexOf(topLetterInText) - alphabet.indexOf(mostFrequentLetterInEnglish)

console.log(key)
console.log(decode(words, key))





