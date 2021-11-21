def find_long_palin_substr(string: str) -> str:
	max_length: int = 1

	start = 0
	length = len(string)
	max_even_substr, max_odd_substr = string[0], string[0]

	for i in range(1, length):
		# use i as index center for even subs
		low = i - 1
		high = i
		even_substr, start, max_length = find_palin_substr(string, start, low, high, length, max_length)

		# use i as index center for odd subs
		low = i - 1
		high = i + 1
		odd_substr, start, max_length = find_palin_substr(string, start, low, high, length, max_length)

		if len(even_substr) > len(max_even_substr):
			max_even_substr = even_substr
		if len(odd_substr) > len(max_odd_substr):
			max_odd_substr = odd_substr

	return max_even_substr if len(max_even_substr) >= len(max_odd_substr) else max_odd_substr


def find_palin_substr(string: str, start: int, low: int, high: int, length: int, max_length: int) -> tuple:

	while low >= 0 and high < length and string[low] == string[high]:
		low -= 1
		high += 1

	low += 1
	high -= 1
	if (string[low] == string[high]) and ((high - low + 1) > max_length):
		start = low
		max_length = high - low + 1

	return string[start:start + max_length], start, max_length


if __name__ == "__main__":
	stringList = ["babad", "cbbd", "a", "ac"]
	for s in stringList:
		print("String:\t{}\nPalindromic substring:\t{}\n".format(s, find_long_palin_substr(s)))
