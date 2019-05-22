# -*- coding: utf-8 -*-

"""

 This function is the basic binary search, it receives an element
 and a list where it will search for the desired element.
 The function returns if the element was found or not and
 the position of it (if it was found)

 TODO: Tests
"""

def binary_iterative(element, list):

	list.sort() # It sorts the list since binary search only works on ordered lists
	mid = len(list) / 2
	
	if element == list[mid]: # Checks if the desired element is in the middle of the list

		print("Element found in position"),
		print(list.index(mid))
		return

	elif element > mid:

		start = mid

		while element > mid: # Loop for searching the element on the upper part of the list
			mid = int((mid + len(list)) / 2)

			if element == list[mid]:
				print("Element found in position"),
				print(list.index(mid))
				return
	elif element < mid:

		end = mid

		while element < mid: # Loop for searching the element on the lower part of the list
			mid = int(mid / 2)

			if element == list[mid]:
				print("Element found in position"),
				print(list.index(mid))
				return
	else:
		print("Element not found")
		return