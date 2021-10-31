export function encode(word: string, shift: number) {

  shift = shift % 26;
  
  return word.split("").map(caesar => {
    const ascii: number = caesar.charCodeAt(0);
    const new_code: number = ascii + shift;
    if (ascii >= 65 && ascii <= 90) {
      if (new_code < 65) {return String.fromCharCode(new_code + 26)}
      if (new_code > 90) {return String.fromCharCode(new_code - 26)}
      else return String.fromCharCode(new_code)
    } else if (ascii >= 97 && ascii <= 122) {
      if (new_code < 97) {return String.fromCharCode(new_code + 26)}
      if (new_code > 122) {return String.fromCharCode(new_code - 26)}
      return String.fromCharCode(new_code)
    } else return caesar;
  }).join('');
}


export function decode(word: string, shift: number) {return encode(word, -shift)}