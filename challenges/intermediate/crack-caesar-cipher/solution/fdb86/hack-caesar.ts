import {decode} from './caesar-cipher'

//string representing letters in order of statistic use in english alphabet
const frequencyLetters = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

function getShiftFactor (message: string) {


    let letterCount: any = {}
    const splitted: any = message.toUpperCase().split("")

    for (let letter of splitted) {
      if (letter.charCodeAt(0) >= 65 && letter.charCodeAt(0) <= 90) {
        if (letter in letterCount) { letterCount[letter] += 1}  else {letterCount[letter] = 1}
      }
    }

    const nums = Object.keys(letterCount).map(o => letterCount[o]);
    const max = Math.max(...nums);
    const char = Object.keys(letterCount).find(letter => letterCount[letter] === max)!;
    
    return (char.charCodeAt(0) - frequencyLetters.charCodeAt(0))

}

export function crackCaesar (message: string) {
  return decode(message, getShiftFactor(message))
}