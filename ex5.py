import string
import random
import bisect_left
def process_file(item):
	h = dict()
	y= open(item)
	for line in y:
		process_file(line, h)
	return h
hist = process_file('emma.txt')
def cum_sum(list_of_numbers):
	cum_list = []
	for i, elem in enumerate(list_of_numbers):
		if i == 0:
			cum_list.append(elem)
		else:
			cum_list.append(cum_list[i-1] + elem)
	return cum_list
def random_word(h):
	word_list = list(h.keys())
	num_list = []
	for word in word_list:
		num_list.append(h[word])
	cum_list = cum_sum(num_list)
	i = randint(1, cum_list[-1])
	pos = bisect_left(cum_list, i)
	return word_list[pos]
print(random_word(hist))
