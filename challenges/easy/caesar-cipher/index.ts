function encode(word: string, shift: number) {

  shift = shift % 26;
  let ascii: number;
  let new_code: number;
  
  return word.split("").map(caesar => {
    new_code = 0;
    ascii = caesar.charCodeAt(0);
    if (ascii >= 65 && ascii <= 90) {
      new_code = ascii + shift;
      if (new_code < 65) {new_code += 26}
      if (new_code > 90) {new_code -= 26}
      return String.fromCharCode(new_code)
    } else if (ascii >= 97 && ascii <= 122) {
      new_code = ascii + shift;
      if (new_code < 97) {new_code += 26}
      if (new_code > 122) {new_code -= 26}
      return String.fromCharCode(new_code)
    } else return caesar;
  }).join('');
}


function decode(word: string, shift: number) {return encode(word, -shift)}

console.log(encode('Hello, World!', 7));                       // => 'Olssv, Dvysk!'
console.log(encode('I love pizza.', -7));                      // => 'B ehox ibsst.'
console.log(encode('HytyQapgnr kyicq qclqc. Qmkcrgkcq.', 50)); // => 'HytyQapgnr kyicq qclqc. Qmkcrgkcq.'
console.log(encode('abc', 24));                                // => 'yza'
console.log('')
console.log(decode('CxvxaaxfMneb Axltb!', 9));                 // => 'TomorrowDevs Rocks!'
console.log(decode('Gtdflw Defotz Nzop td rcple!!!', -15));    // => 'Visual Studio Code is great!!!'
console.log(decode("Buj'i mhyju jxu syfxuh.", 120));           // => 'Let's write the cipher.'
console.log(decode('Vriwzduh Hqjlqhhulqj', 3));                // => 'Software Engineering'