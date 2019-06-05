# -*- coding: utf-8 -*-

class Linked_Node:
	def __init__(self, value = None, next_node = None):
		self.value = value
		self.next_node = next_node

	def get_next(self):
		return self.next_node


class Stack:
	def __init__(self, element_list = []):
		self.__element_list = element_list

	def get_list(self):
		aux = []

		for x in self.__element_list:
			aux.append(x.value)

		return aux

	def get_nexts(self):
		aux = []

		for x in range(0, len(self.__element_list)):
			if x + 1 < len(self.__element_list):
				aux.append(self.__element_list[x].next_node.value)

		return aux

	def fix_list(self):
		for x in range(0, len(self.__element_list)):
			if x + 1 < len(self.__element_list):
				self.__element_list[x].next_node = self.__element_list[x + 1]

	def push(self, element):
		try:
			new_node = Linked_Node(element, self.__element_list[0])
			return element

		except TypeError:
			print("Invalid Push")

def main():
	node1 = Linked_Node(1)
	node2 = Linked_Node(2)
	node3 = Linked_Node(3)

	linked_list = [node1, node2, node3]
	stack = Stack(linked_list)
	stack.fix_list()

	print(stack.get_list())
	print(stack.get_nexts())


if __name__ == '__main__':
	main()