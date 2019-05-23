# -*- code: utf-8 -*-

"""

 The class that i made is a simple container, it has the basic functions of
 most of container type class. It can store elements, you can use the insert
 function to add multiple elements at time or one by one and, you can manipulate
 the existing elements inside of it, by using see function to search and the delete
 function to delete elements by index or name.

"""
# Iterative binary search, can import from my other file.
def binary_iterative(element, list_1):
	list_1.sort()
	lower = 0
	upper = len(list_1) - 1

	while lower <= upper:

		mid = int((upper + lower) / 2)

		if element == list_1[mid]:
			return mid

		elif element < list_1[mid]:
			upper = mid - 1

		else:
			lower = mid + 1

	return False

class Container:

	def __init__(self): # Default constructor
		self.elements_list = []

	def print(self): # Prints the whole lists, prints "Empty!" if the list is empty
		if len(self.elements_list) == 0:
			print("Empty! )=")

		else:
			print(self.elements_list)

	def insert(self, element): # Inserts the desired element on the list
		self.elements_list.append(element)

	def insert_many(self): # Inserts X elements on the list
		try:
			print("How many elements do you want to insert")
			quantity = int(input("--> "))
			print("Elements to insert: ")

			for element in range(0, quantity):
				element = input("--> ")
				self.elements_list.append(element)

		except (TypeError, ValueError):
			print("Please insert a number")

	def see(self, element): # Searchs an element on the list and returns it's index and what is it (If found)
		index = binary_iterative(element, self.elements_list)

		if index == False:
			print("Element not found")

		else:
			print("Element found at index: ", index)
			print("The element is: ", self.elements_list[index])

	def size(self): # Prints the size of the list
		print("This container have", len(self.elements_list), "elements")

	def delete_index(self, index): # Deletes an element based on the index
		try:
			self.elements_list.pop(index)

		except IndexError:
			print("Index out of range")

	def delete_element(self, element): # Deletes an element based on its name
		try:
			self.elements_list.remove(element)

		except ValueError:
			print("Element not found")

	def clear(self): # Erases the whole list
		self.elements_list.clear()


def main():
	container_test = Container()
	
	print("Which element you want to insert: ")
	element = input("--> " )
	container_test.insert(element)
	container_test.print()
	
	container_test.insert_many()
	container_test.print()
	container_test.size()
	
	container_test.delete_index(20)
	container_test.delete_index(5)

	container_test.delete_element("14284")
	container_test.delete_element("10")

	container_test.see("324")
	container_test.see("6")

	container_test.print()

	container_test.clear()
	container_test.print()


if __name__ == '__main__':
		main()	



