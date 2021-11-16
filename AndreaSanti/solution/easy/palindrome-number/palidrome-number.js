const reverseNumber = (num) => {
  const reverse = num.toString().split("").reverse().join("");

  return +reverse;
};

const palindromeNumber = (num) => {
  if (num < 0) return false;

  return num === reverseNumber(num);
};

//TESTS

const testNumber = Array.from(Array(10000), (_, i) => i + 1);

testNumber.forEach((num) => {
  if (!palindromeNumber(num)) return;
  console.log(palindromeNumber(num), num);
});
