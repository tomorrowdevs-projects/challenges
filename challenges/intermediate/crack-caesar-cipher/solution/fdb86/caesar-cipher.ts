function encode(word: string, shift: number) {

  const alphabetLength = 26;
  // reduce the shift factor to real position to shift if the shift factor is more than 26, else the result is the same of starting shift.
  const moduleShift = shift % alphabetLength;
  
  return word.split("").map(caesar => {
    const ascii = caesar.charCodeAt(0);
    const new_code = ascii + moduleShift;

    //range of values for upper and lower letters in ASCII code
    const minimumUpper = 65; const maximumUpper = 90;
    const minimumLower = 97; const maximumLower = 122;

    if (ascii >= minimumUpper && ascii <= maximumUpper) {
      if (new_code < minimumUpper) {return String.fromCharCode(new_code + alphabetLength)}
      if (new_code > maximumUpper) {return String.fromCharCode(new_code - alphabetLength)}
      else return String.fromCharCode(new_code)
    } else if (ascii >= minimumLower && ascii <= maximumLower) {
      if (new_code < minimumLower) {return String.fromCharCode(new_code + alphabetLength)}
      if (new_code > maximumLower) {return String.fromCharCode(new_code - alphabetLength)}
      return String.fromCharCode(new_code)  
    } else return caesar;
  }).join('');
}


export function decode(word: string, shift: number) {return encode(word, -shift)}