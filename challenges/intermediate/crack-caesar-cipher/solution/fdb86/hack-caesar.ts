import {encode} from './caesar-cipher'
import {decode} from './caesar-cipher'

const englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
                           'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
                           'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
                           'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
                           'Q': 0.10, 'Z': 0.07}

const ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

function getShiftFactor (message: string) {


    var letterCount: any = {}
    const splitted: any = message.toUpperCase().split("")

    for (let letter of splitted) {
      if (letter.charCodeAt(0) >= 65 && letter.charCodeAt(0) <= 90) {
        if (letter in letterCount) { letterCount[letter] += 1}  else {letterCount[letter] = 1}
      }
    }

    const nums = Object.keys(letterCount).map(o => letterCount[o]);
    const max = Math.max(...nums);
    const char = Object.keys(letterCount).find(letter => letterCount[letter] === max)!;
    
    return (char.charCodeAt(0) - ETAOIN.charCodeAt(0))

}

export function crackCaesar (message: string) {
  return decode(message, getShiftFactor(message))
}