# -*- coding: utf-8 -*-

"""
 This function is the recursive binary search, it receives an element
 and a list_1 where it will search for the desired element.
 The function returns if the element was found or not and
 the position of it (if it was found)

 After doing some testing i reached a error of python interrupting the
 program because the recursion limit was reached, it happens only when
 the element is not on the list for some reason, i've searched a bit
 and it seems that python do not optimize tail recursion and that limit
 is to prevent stack overflows.

 It seems recursion is not worth it on python.

"""

def binary_recursive(element,list_1,lower, upper):

	list_1.sort() # It sorts the list_1 since binary search only works on ordered lists

	mid = int((upper + lower) / 2)
	
	if element == list_1[mid]: # Checks if the element is on the middle of the list
		print("Element found in position", mid)
		return mid

	elif element < list_1[mid]: # Checks if the element is lower than the middle of the list
		binary_recursive(element, list_1, lower, mid - 1)

	else: # If the element isn't lower or equal to the middle, its higher. (Or is not on the list)
		binary_recursive(element, list_1, mid + 1, upper)

	#print("Element not found")
	return -1

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
word_list = ["something", "ohno", "wait", "something123", "test", "tesdcwe"]

binary_recursive(1, number_list, 0, len(number_list))
binary_recursive(6, number_list, 0, len(number_list))
binary_recursive(15, number_list, 0, len(number_list))
binary_recursive(20, number_list, 0, len(number_list))

binary_recursive("something", word_list, 0, len(word_list))
binary_recursive("wait", word_list, 0, len(word_list))
binary_recursive("test", word_list, 0, len(word_list))
binary_recursive("tesdcwe", word_list, 0, len(word_list))




