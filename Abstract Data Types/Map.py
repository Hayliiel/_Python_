# -*- coding: utf-8 -*-

'''

 This class is a basic map made by myself, it stores elements based on keys that
 represent those elements. The class allows the user to add, remove, reassign and
 lookup the elements on the map using it's key.

'''
class Mapping: # Class used to represent each element on the main map list
	def __init__(self, key, element):
		self.key = key
		self.__element = element

	def get_value(self):
		return self.__element

	def set_value(self, element):
		self.__element = element

class Map: # Class used to represent the map
	def __init__(self): # Default cosntructor
		self.element_list = []
		self.keys_list = []

	def add(self, key, element): # Adds one element to the map
		result = Mapping(key, element)
		self.element_list.append(result)
		self.keys_list.append(key)

	def add_many(self): # Adds X elements to the map
		print("How many elements do you want to add")
		quantity = int(input("--> "))

		for x in (range(0, quantity)):
			print("Add the element")
			key = input("Key: ")
			value = input("Value: ")
			
			element = Mapping(key,value)
			self.element_list.append(element)
			self.keys_list.append(key)

	def reassign(self, key, element): # Reassigns an existing key to a new element
		try:
			self.element_list[self.keys_list.index(key)].set_value(element)

		except (IndexError,ValueError):
			print("Key not found")

	def delete(self, key): # Deletes an element from the map based on given key
		try:
			self.element_list.pop(self.keys_list.index(key))
			self.keys_list.pop(self.keys_list.index(key))

		except (ValueError, IndexError):
			print("Key not found")

	def lookup(self, key): # Acess any element on the map based on given key, returns the searched element(If found)
		try:
			return self.element_list[self.keys_list.index(key)].get_value()

		except (ValueError, IndexError):
			print("Key not found")

	def print(self): # Prints all keys stored within the map
		if not self.keys_list:
			print("Empty!")
		else:
			print(self.keys_list)

	def size(self): # Prints the size of the map, returns the size
		print("This map have", len(self.element_list), "keys")
		return len(self.element_list)

	def clear(self): # Erases the whole list
		self.element_list.clear()
		self.keys_list.clear()


def main():
	test_map = Map()
	test_map.add("number", 998652254)
	print(test_map.lookup("number"))
	print(test_map.lookup("numberr"))

	test_map.add("regions", 9)
	test_map.add("people", 2000000)
	test_map.add("cities", 27)

	test_map.add_many()

	test_map.size()
	test_map.print()

	test_map.reassign("regions", 4)
	test_map.reassign("people", 2005367)

	test_map.reassign("ciities", 20)
	test_map.reassign("none", 1230)

	print(test_map.lookup("regions"))
	print(test_map.lookup("people"))
	test_map.print()

	test_map.delete("number")
	test_map.delete("people")

	test_map.delete("something")
	test_map.delete("SoMeThInG")
	test_map.print()

	test_map.clear()
	test_map.print()

if __name__ == '__main__':
	main()

