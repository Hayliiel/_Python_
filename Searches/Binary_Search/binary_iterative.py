# -*- coding: utf-8 -*-

"""

 This function is the iterative binary search, it receives an element
 and a list_1 where it will search for the desired element.
 The function returns if the element was found or not and
 the position of it (if it was found)

"""

def binary_iterative(element, list_1):

	list_1.sort() # It sorts the list_1 since binary search only works on ordered lists
	lower = 0
	upper = len(list_1) - 1

	while lower <= upper:

		mid = int((upper + lower) / 2)

		if element == list_1[mid]: # Checks if the element is on the middle of the list
			#print("Element found in position", mid)
			return mid
		
		elif element < list_1[mid]: # Checks if the element is lower than the middle of the list
			upper = mid - 1

		else: # If the element isn't lower or equal to the middle, its higher. (Or is not on the list)
			lower = mid + 1

	#print("Element not found")
	return -1



number_list = [1, 2, 3, 4, 5, 12, 8, 27, 30, 66, 34, 123]
word_list = ["something", "ohno", "wait", "something123", "test", "tesdcwe"]

binary_iterative(4, number_list)
binary_iterative(5, number_list)
binary_iterative(12, number_list)
binary_iterative(8, number_list)

binary_iterative(7, number_list)
binary_iterative(22, number_list)
binary_iterative(32, number_list)
binary_iterative(14, number_list)

binary_iterative("test", word_list)
binary_iterative("tesdcwe", word_list)
binary_iterative("ohno", word_list)
binary_iterative("something123", word_list)

binary_iterative("testt", word_list)
binary_iterative("nope", word_list)
binary_iterative("qscqwe", word_list)
binary_iterative("123", word_list)
