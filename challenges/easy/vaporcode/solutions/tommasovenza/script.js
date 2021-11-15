// Write a function that converts any sentence into a V A P O R W A V E sentence.
// A V A P O R W A V E sentence converts all the letters into uppercase, and adds 2
// spaces between each letter (or special character) to create this V A P O R W A V E
// effect.

// While this may seems like a very simple challenge, it will become a bit harder,
// 'cause you have to solve it by using a language that you've never seen before.

function vaporwaveReduce(string) {
  const array = []
  for (let index = 0; index < string.length; index++) {
    array.push(string[index])
  }
  const stringReduce = array.reduce((firstVal, currentVal) => {
    if (currentVal === " ") {
      return (firstVal += "")
    } else {
      return (firstVal += " " + currentVal + " ")
    }
  }, "")

  const result = stringReduce.substr(1, stringReduce.length - 2).toUpperCase()

  return result
}

function vaporwave(string) {
  let finalString = ""

  for (let index = 0; index < string.length; index++) {
    if (string[index] === " ") {
      finalString += ""
    } else {
      finalString += string[index].toUpperCase() + "  "
    }
  }
  // remove last two empty characters added before
  const result = finalString.substr(0, finalString.length - 2)

  return result
}

const resultVaporwave = vaporwave("I love JavaScript!")
const resultVaporwaveReduce = vaporwaveReduce("I love php!")
console.log(resultVaporwave)
console.log(resultVaporwaveReduce)
