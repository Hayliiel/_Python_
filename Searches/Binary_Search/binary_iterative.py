# -*- coding: utf-8 -*-

"""

 This function is the basic binary search, it receives an element
 and a list_1 where it will search for the desired element.
 The function returns if the element was found or not and
 the position of it (if it was found)

 TODO: Tests
"""

def binary_iterative(element, list_1):

	list_1.sort() # It sorts the list_1 since binary search only works on ordered lists
	print(list_1)
	lower = 0
	upper = len(list_1)

	while lower <= upper:

		mid = int((upper - lower) / 2)

		if element == list_1[mid]: # Checks if the element is on the middle of the list
			print("Element found in position", mid)
			return
		
		elif element < list_1[mid]: # Checks if the element is lower than the middle of the list
			upper = mid - 1

		else: # If the element isn't lower or equal to the middle, its higher. (Or is not on the list)
			lower = mid + 1

	print("Element not found")
	return

