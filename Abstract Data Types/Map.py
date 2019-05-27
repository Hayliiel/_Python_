# -*- coding: utf-8 -*-

class Mapping:
	def __init__(self, key, element):
		self.key = key
		self.__element = element

	def get_value(self):
		return self.element

	def set_value(self, element):
		self.__element = element

class Map:
	def __init__(self):
		self.element_list = []

	def add(self, key, element):
		result = Mapping(key, element)
		self.element_list.append(result)

	def add_many(self):
		print("How many elements do you want to add")
		quantity = input("--> ")

		for x in (range(0, quantity)):
			print("Add the element")
			key = input("Key: ")
			value = input("Value: ")
			
			element = Mapping(key,value)
			self.element_list.apped(element)

	def reassign(self, key, element):
		try:
			self.element_list[key].set_value(element)

		except (IndexError,ValueError):
			print("Key not found")

	def delete(self, key, element):
		try:
			del self.element_list[key]

		except IndexError:
			print("Key not found")

	def lookup(self, key):
		try:
			return self.element_list[key].get_value()

		except IndexError:
			print("Key not found")


def main():
	


if __name__ == '__main__':
	main()

