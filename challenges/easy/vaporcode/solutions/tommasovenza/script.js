// Write a function that converts any sentence into a V A P O R W A V E sentence.
// A V A P O R W A V E sentence converts all the letters into uppercase, and adds 2
// spaces between each letter (or special character) to create this V A P O R W A V E
// effect.

// While this may seems like a very simple challenge, it will become a bit harder,
// 'cause you have to solve it by using a language that you've never seen before.

function vaporwave(string) {
  let finalString = ""

  for (let index = 0; index < string.length; index++) {
    finalString += string[index].toUpperCase() + " "
  }
  return finalString
}

console.log(vaporwave("I love JavaScript!"))
