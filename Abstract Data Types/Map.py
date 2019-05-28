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
		quantity = input("--> ")

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
			self.keys_list.pop(key)

		except IndexError:
			print("Key not found")

	def lookup(self, key): # Acess any element on the map based on given key
		try:
			return self.element_list[self.keys_list.index(key)].get_value()

		except IndexError:
			print("Key not found")

	def clear(self): # Erases the whole list
		self.element_list.clear()
		self.keys_list.clear()



def main():
	test_map = Map()
	test_map.add("numero", 1234)
	test_map.lookup("numero")
	


if __name__ == '__main__':
	main()

