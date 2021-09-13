function isPrime(num) {
  if (num < 2) return false;
  for (let i = 2; i < num; i++) {
    if (num % i == 0) return false;
  }
  return true;
}

function solve(a, b) {
  let result = 0;
  const primes = [];

  for (let i = a; i < b; i++) {
    if (isPrime(i)) primes.push(i);
  }

  for (let i = 0; i < primes.length; i++) {
    for (let j = i; j < primes.length; j++) {
      let sum = (primes[i] * primes[j])
        .toString()
        .split("")
        .reduce((a, b) => a + +b, 0);
      if (isPrime(sum)) result++;
    }
  }

  return result;
}

console.log(solve(0, 20));
console.log(solve(2, 200));
console.log(solve(2, 300));
console.log(solve(100, 200));
