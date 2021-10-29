const letters = 26;

function encode(str, shift) {
  shift  = shift % letters

  return str.split("").map(character => {
      // if is a letter
      if ((character >= "a" && character <= "z") || (character >= "A" && character <= "Z")) {
        // if is lowercase
        if (character >= "a" && character <= "z") {
          ascii = 97
        }
        // if is uppercase
        else {
          ascii = 65
        }

        new_str = letters + character.charCodeAt(0) - ascii
        new_str = (new_str + shift) % letters
        encrypt = String.fromCharCode(new_str + ascii) 
        return encrypt
      }
      // don't encrypt if it's not a letter
      else return character;
  }).join("");
}


function decode(str, shift) {
  shift  = shift % letters

  return str.split("").map(character => {
      // if is a letter
      if ((character >= "a" && character <= "z") || (character >= "A" && character <= "Z")) {
        // if is lowercase
        if (character >= "a" && character <= "z") {
          ascii = 97
        }
        // if is uppercase
        else {
          ascii = 65
        }

        new_str = letters + character.charCodeAt(0) - ascii
        new_str = (new_str - shift) % letters
        decrypt = String.fromCharCode(new_str + ascii) 
        return decrypt
      }
      else return character;
  }).join("");
}


/*

// encode test
console.log(encode('Hello, World!', 7)); // => 'Olssv, Dvysk!'
console.log(encode('I love pizza.', -7)); // => 'B ehox ibsst.'
console.log(encode('HytyQapgnr kyicq qclqc. Qmkcrgkcq.', 50)); // => 'HytyQapgnr kyicq qclqc. Qmkcrgkcq.'
console.log(encode('abc', 24));  // => 'yza'


// decode test
console.log(decode('CxvxaaxfMneb Axltb!', 9)); // => 'TomorrowDevs Rocks!'
console.log(decode('Gtdflw Defotz Nzop td rcple!!!', -15)); // => 'Visual Studio Code is great!!!'
console.log(decode('Vriwzduh Hqjlqhhulqj', 3)); // => 'Software Engineering'
console.log(decode("Buj'i mhyju jxu syfxuh.", 120)); // => "Let's write the cipher."

*/