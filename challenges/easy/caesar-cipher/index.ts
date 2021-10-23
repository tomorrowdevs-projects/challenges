const lower_array = ['a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n',  'o',  'p',  'q',  'r',  's',  't',  'u',  'v',  'w',  'x',  'y',  'z'];
const upper_array = ['A',  'B',  'C',  'D',  'E',  'F',  'G',  'H',  'I',  'J',  'K',  'L',  'M',  'N',  'O',  'P',  'Q',  'R',  'S',  'T',  'U',  'V',  'W',  'X',  'Y',  'Z'];


function encode(word: string, shift: number) {
  let caesar: string = '';
  for (let i: number=0, new_code: number; i<word.length; i++) {
    if (upper_array.includes(word[i])) {
      new_code = (upper_array.indexOf(word[i]) + shift + 26) % 26;
      if (new_code < 0) {new_code += 26}
      caesar += upper_array[new_code];
    } else if (lower_array.includes(word[i])) {
      new_code = (lower_array.indexOf(word[i]) + shift + 26) % 26;
      if (new_code < 0) {new_code += 26}
      caesar += lower_array[new_code];
    } else {
      caesar += word[i];
    }
  }
  return caesar;
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