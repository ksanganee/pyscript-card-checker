def sum_digits(number):
	number_string = str(number)
	total = 0
	for letter in number_string:
		total += int(letter)
	return total