# -*- coding: utf-8 -*-

class Dynamic_Set:
	def __init__(self, ele_list = []):
		self.__element_list = ele_list

	def get_list(self):
		return self.__element_list

	def union(self, secondary_set):
		try:
			aux = []

			for x in range(0, len(self.__element_list)):
				if self.__element_list[x] not in secondary_set:
					aux.append(self.__element_list[x])

			return aux + secondary_set

		except TypeError:
			print("The operation can only be done with two sets")

	def intersection(self, secondary_set):
		try:
			aux = []

			for x in range(0, len(self.__element_list)):
				if self.__element_list[x] in secondary_set:
					aux.append(self.__element_list[x])

			return aux

		except TypeError:
			print("The operation can only be done with two sets")

	def difference(self, secondary_set):
		try:
			aux = []

			for x in range(0,len(secondary_set)):
				if secondary_set[x] not in self.__element_list:
					aux.append(secondary_set[x])

			return aux

		except TypeError:
			print("The operation can only be done with two sets")

	def subset(self, secondary_set):
		try:
			if all(x in secondary_set for x in self.__element_list):
				return True

			else:
				return False

		except TypeError:
			print("The operation can only be done with two sets")

	def add(self, element):
		if element in self.__element_list:
			print("Element already on the set")

		else:
			self.__element_list.append(element)

	def remove(self, element):
		try:
			self.__element_list.remove(element)

		except ValueError:
			print("The element is not on the set")

	def clear(self):
		self.__element_list.clear()

def main():
	list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5, 6, 7, 8 ,9]
	list3 = [11, 22, 33, 44, 55, 66]
	test_list = Dynamic_Set(list1)
	
	print(test_list.union(list2))
	test_list.union(12345)

	print(test_list.intersection(list2))
	test_list.intersection(12345)

	print(test_list.difference(list2))
	test_list.difference(12345)

	print(test_list.subset(list2))
	print(test_list.subset(list3))
	test_list.subset(12345)


	test_list.add(123)

	test_list.remove(1)
	test_list.remove(4531542)

	print(test_list.get_list())
	test_list.clear()
	print(test_list.get_list())

if __name__ == '__main__':
	main()