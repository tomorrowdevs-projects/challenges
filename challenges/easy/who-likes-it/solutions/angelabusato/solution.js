const likes = (array) => {
    if (array.length === 0) {
        return "no one likes this";
    }
    if (array.length === 1) {
        return `${array[0]} likes this`;
    }
    if (array.length === 2) {
        return `${array[0]} and ${array[1]} like this`;
    }
    if (array.length === 3) {
        return `${array[0]}, ${array[1]} and ${array[2]} like this`;
    }
    if (array.length > 3) {
        return `${array[0]}, ${array[1]} and ${array.length - 2} others like this`;
    }
};