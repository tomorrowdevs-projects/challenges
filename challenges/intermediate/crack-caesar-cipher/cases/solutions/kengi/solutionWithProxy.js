let alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",];
let alphabetCapital = alphabet.map((x) => x.toUpperCase());


// https://medium.com/uncaught-exception/javascript-array-negative-index-using-proxies-ed096dc84416
// create a proxy for the properties of alphabet, check if the prop is negative and transform it
// in a valid array index value
const proxy = new Proxy(alphabet, {
    get(target, prop) {
        if (!isNaN(prop)) {
//converts in number as prop is passed as a string
            prop = parseInt(prop, 10);
            if (prop < 0) {
                prop += target.length;
            }
        }
        return target[prop];
    }
});

const encode = (string, shift) => {
  // set empty array to push resulted encrypted letters or symbol
  let cypher = [];
  for (letter of string) {
    
    // if the shift coefficient plus the letter index are over 26 reduce them in the 0 - 25 range
    let num = (alphabet.indexOf(letter.toLowerCase()) + shift) % 26;

    // everything that is not a letter, push it in the encrypted solution as it is
    if (!alphabet.includes(letter.toLowerCase())) {
      cypher.push(letter);
    }
    // lowercase
    else if (alphabet.includes(letter)) {
        cypher.push(proxy[num]);
    }   
    // uppercase
    else if (alphabetCapital.includes(letter)) {
        cypher.push(proxy[num].toUpperCase());
      }
  }
  return cypher.join("");
};

// flip sign at the shift parameter to use encode() to decode
const decode = (string, shift) => {
  let flipShift = shift > 0 ? -shift : Math.abs(shift);
  return encode(string, flipShift);
};



console.log(encode("abcdefghiABCDEFGHI", -10));
console.log(encode("Hello, World!", 7)); // => 'Olssv, Dvysk!'
encode("I love pizza.", -7); // => 'B ehox ibsst.'
console.log(decode("HytyQapgnr kyicq qclqc. Qmkcrgkcq.", 50))
// => 'JavaScript makes sense. Sometimes.'
encode("abc", 24); // => 'yza'

decode("CxvxaaxfMneb Axltb!", 9); // => 'TomorrowDevs Rocks!'
decode("Gtdflw Defotz Nzop td rcple!!!", -15); // => 'Visual Studio Code is great!!!'
decode("Buj'i mhyju jxu syfxuh.", 120); // => 'Let's write the cipher.'
decode("Vriwzduh Hqjlqhhulqj", 3); // => 'Software Engineering'
