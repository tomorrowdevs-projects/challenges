function find_palin_substr (string: string, start: number, low: number, high: number, length: number, max_length: number) {
    while (low >= 0 && high < length && (string[low] === string[high])) {
        low -= 1;
		high += 1;
    }

    low += 1;
	high -= 1;

    if ((string[low] === string[high]) && ((high - low + 1) > max_length)) {
        start = low;
		max_length = high - low + 1;
    }

    return [string.slice(start, start + max_length), start, max_length]
}

function find_long_palin_substr (string: string) {
    
    let max_length: number = 1;
    let start: number = 0;
    let length: number = string.length;
	let max_even_substr: string = string[0];
    let max_odd_substr: string = string[0];
    let even_substr: string;
    let odd_substr: string;
    let find_palin_return = [];

    for (let i = 1; i < length; i++) {
        // use i as index center for even subs
		find_palin_return = find_palin_substr(string, start, i-1, i, length, max_length);
        even_substr = find_palin_return[0].toString();
        start = Number(find_palin_return[1]);
        max_length = Number(find_palin_return[2]);
        
        // use i as index center for odd subs
        find_palin_return = find_palin_substr(string, start, i-1, i+1, length, max_length);
        odd_substr = find_palin_return[0].toString();
        start = Number(find_palin_return[1]);
        max_length = Number(find_palin_return[2]);

        if (even_substr.length > max_even_substr.length) {
            max_even_substr = even_substr
        }
        if (odd_substr.length > max_odd_substr.length) {
            max_odd_substr = odd_substr
        } 
    }

    if (max_even_substr.length > max_odd_substr.length) {
        return max_even_substr
    } else return max_odd_substr
}

console.log(find_long_palin_substr("cbbd"));
console.log(find_long_palin_substr("babad"));
console.log(find_long_palin_substr("a"));
console.log(find_long_palin_substr("ac"));