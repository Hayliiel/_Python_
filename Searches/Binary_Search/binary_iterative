# -*- coding: utf-8 -*-

def binary_iterative(element, list):

	list.sort()
	mid = len(list) / 2
	
	if element == list[mid]:

		print("Element found in position"),
		print(list.index(mid))
		return

	elif element > mid:

		start = mid

		while element > mid:
			mid = int((mid + len(list)) / 2)

			if element == list[mid]:
				print("Element found in position"),
				print(list.index(mid))
				return
	elif element < mid:

		end = mid

		while element < mid:
			mid = int(mid / 2)

			if element == list[mid]:
				print("Element found in position"),
				print(list.index(mid))
				return