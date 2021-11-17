let alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",];
let alphabetCapital = alphabet.map((x) => x.toUpperCase());

const encode = (string, shift) => {
  // set empty array to push resulted encrypted letters or symbol
  let cypher = [];
  for (let i = 0; i < string.length; i++) {
    const letter = string[i];

    // if the shift coefficient plus the letter index are over 26 reduce them in the 0 - 25 range
    let num = (alphabet.indexOf(letter.toLowerCase()) + shift) % 26;

    // everything that is not a letter, push it in the encrypted solution as it is
    if (!alphabet.includes(letter.toLowerCase())) {
      cypher.push(letter);
    }
    // if the index of the letter summed with shift number provided is positive
    else if (num >= 0) {
      // finds in the alphabet the letter with the index of
      // the given letter plus the shift number.
      // the nested if statement is for taking care of capital letters
      if (alphabet.includes(letter)) {
        cypher.push(alphabet[num]);
      } else if (alphabetCapital.includes(letter)) {
        cypher.push(alphabetCapital[num]);
      }
    }
    // if the index of the letter minus the shift number provided is negative
    else if (num < 0) {
      if (alphabet.includes(letter)) {
        console.log(num);
        console.log(alphabet[alphabet.length + num]);
        cypher.push(alphabet[alphabet.length + num]);
      } else if (alphabetCapital.includes(letter)) {
        cypher.push(alphabetCapital[alphabet.length + num]);
      }
    }
  }
  return cypher.join("");
};

const decode = (string, shift) => {
  let flipShift = shift > 0 ? -shift : Math.abs(shift);
  return encode(string, flipShift);
};

console.log(encode("f", -10));
console.log(alphabet.indexOf("f"));
console.log(encode("Hello, world!", 7)); // => 'Olssv, Dvysk!'
encode("I love pizza.", -7); // => 'B ehox ibsst.'
encode("HytyQapgnr kyicq qclqc. Qmkcrgkcq.", 50);
// => 'HytyQapgnr kyicq qclqc. Qmkcrgkcq.'
encode("abc", 24); // => 'yza'

decode("CxvxaaxfMneb Axltb!", 9); // => 'TomorrowDevs Rocks!'
decode("Gtdflw Defotz Nzop td rcple!!!", -15); // => 'Visual Studio Code is great!!!'
decode("Buj'i mhyju jxu syfxuh.", 120); // => 'Let's write the cipher.'
decode("Vriwzduh Hqjlqhhulqj", 3); // => 'Software Engineering'
