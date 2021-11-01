const lowerAlpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
const upperAlpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];

function encode(original_sentence, shift){
    const sentence_array = Array.from(original_sentence)
    let encoded_sentence = []
    sentence_array.forEach(function (char) {
        if (lowerAlpha.includes(char)){
            let index = lowerAlpha.indexOf(char)
						new_shift = (index + (shift % 26)) + 26
            encoded_sentence.push(lowerAlpha[new_shift % 26]);
        }
        else if (upperAlpha.includes(char)){
            let index = upperAlpha.indexOf(char)
            new_shift = (index + (shift % 26)) + 26
            encoded_sentence.push(upperAlpha[new_shift % 26]);
        }
        else {
            encoded_sentence.push(char)
        };
    });
    return encoded_sentence.join('')
}

let result1 = encode('abc', 24);
console.log(result1);

function decode(original_sentence, shift){
    const sentence_array = Array.from(original_sentence)
    let encoded_sentence = []
    sentence_array.forEach(function (char) {
        if (lowerAlpha.includes(char)){
            let index = lowerAlpha.indexOf(char)
            new_shift = (index - (shift % 26)) + 26
            encoded_sentence.push(lowerAlpha[new_shift % 26]);
        }
        else if (upperAlpha.includes(char)){
            let index = upperAlpha.indexOf(char)
            new_shift = (index - (shift % 26)) + 26
            encoded_sentence.push(upperAlpha[new_shift % 26]);
        }
        else {
            encoded_sentence.push(char)
        }
    });
    return encoded_sentence.join('')
}

let result2 = decode('Vriwzduh Hqjlqhhulqj', 3);
console.log(result2);