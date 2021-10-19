# Caesar Cipher

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of `3`, `D` would be replaced by `A`, `E` would become `B`, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

## Constraints

- The cipher should maintain both lowercase and uppercase letters
- The cipher should only shift alphabet letters. Spaces, special characters and numbers should remain the same.
- The solution should provide two functions: `encode` and `decode`.

## Example

```js
encode('Hello, World!', 7);                       // => 'Olssv, Dvysk!'
encode('I love pizza.', -7);                      // => 'B ehox ibsst.'
encode('HytyQapgnr kyicq qclqc. Qmkcrgkcq.', 50); // => 'HytyQapgnr kyicq qclqc. Qmkcrgkcq.'
encode('abc', 24);                                // => 'yza'

decode('CxvxaaxfMneb Axltb!', 9);                 // => 'TomorrowDevs Rocks!'
decode('Gtdflw Defotz Nzop td rcple!!!', -15);    // => 'Visual Studio Code is great!!!'
decode("Buj'i mhyju jxu syfxuh.", 120);           // => 'Let's write the cipher.'
decode('Vriwzduh Hqjlqhhulqj', 3);                // => 'Software Engineering'
```