/*
JS solution for challenge: "Divisors of a Number"
To test the solution, type from CLI: node solution.js
*/

function divisors(number) {
    // Variables declarations
    let divisor = 1;
    let count = 0;
    let quotient = number;
    while (divisor <= quotient) {
        // The number is divisible by the divisor
        if (number % divisor == 0) {
            // If the quotient is greater than the divisor both must be counted otherwise only the divisor
            quotient > divisor ? count += 2 : count += 1
        }
        // New divisor and new quotient to consider for the next iteration
        divisor += 1;
        quotient = number / divisor;
    }
    return count
}


// TEST CASES
console.log("\nExpected sequence: 1 2 2 3 2 2 6 8 8 6 8 10 4 2:")
sequence = ""
console.log("     divisors(1) = " + divisors(1) + " | | | | | | | | | | || | |")      // expected 1 (1)
sequence += divisors(1)
console.log("       divisors(2) = " + divisors(2) + " | | | | | | | | | || | |")      // expected 2 (1,2)
sequence += divisors(2)
console.log("         divisors(3) = " + divisors(3) + " | | | | | | | | || | |")      // expected 2 (1,3)
sequence += divisors(3)
console.log("           divisors(4) = " + divisors(4) + " | | | | | | | || | |")      // expected 3 (1,2,4)
sequence += divisors(4)
console.log("             divisors(5) = " + divisors(5) + " | | | | | | || | |")      // expected 2 (1,5)
sequence += divisors(5)
console.log("               divisors(7) = " + divisors(7) + " | | | | | || | |")      // expected 2 (1,7)
sequence += divisors(7)
console.log("                divisors(12) = " + divisors(12) + " | | | | || | |")     // expected 6 (1,2,3,4,6,12)
sequence += divisors(12)
console.log("                  divisors(24) = " + divisors(24) + " | | | || | |")     // expected 8 (1,2,3,4,6,8,12,24)
sequence += divisors(24)
console.log("                    divisors(30) = " + divisors(30) + " | | || | |")     // expected 8 (1,2,3,5,6,10,15,30)
sequence += divisors(30)
console.log("                      divisors(99) = " + divisors(99) +  " | || | |")    // expected 6 (1,3,9,11,33,99)
sequence += divisors(99)
console.log("                       divisors(130) = " + divisors(130) +  " || | |")   // expected 8 (1,2,5,10,13,26,65,130)
sequence += divisors(130)
console.log("                        divisors(1875) = " + divisors(1875) +  " | |")   // expected 10 (1,3,5,15,25,75,125,375,625,1875)
sequence += divisors(1875)
console.log("                           divisors(4997) = " + divisors(4997) + " |")   // expected 4 (1,19,263,4997)
sequence += divisors(4997)
console.log("                            divisors(10589) = " + divisors(10589))       // expected 2 (1,10589)
sequence += divisors(10589)
sequence === '122322688681042' ? console.log('\nCongratulations, all tests have been passed.') : console.log('\nAttention, tests failed.')