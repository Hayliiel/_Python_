# -*- coding: utf-8 -*-

class Dynamic_Set:
	def __init__(self, ele_list):
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
			print("The union can only be done with two sets")

	def intersection(self, secondary_set):
		try:
			aux = []

			for x in range(0, len(self.__element_list)):
				if self.__element_list[x] in secondary_set:
					aux.append(self.__element_list[x])

			return aux

		except TypeError:
			print("The intersection can only be done with two sets")

def main():
	list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5, 6, 7]
	test_list = Dynamic_Set(list1)
	print(test_list.union(list2))
	#print(test_list.intersection(list2))

if __name__ == '__main__':
	main()