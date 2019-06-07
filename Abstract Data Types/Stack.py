# -*- coding: utf-8 -*-
'''

This class is a simple Stack using a linked list to store the elements,
you can remove the top of the stack, add on element to the top of the stack
and look the top of the stack without removing it.

'''

# Class used to represent the stack nodes
class Linked_Node:
	def __init__(self, value = None, next_node = None):
		self.value = value
		self.next_node = next_node

	def get_next(self):
		return self.next_node


class Stack:
	def __init__(self, element_list = []): # Default constructor
		self.__element_list = element_list

	def get_list(self): # Return the value of each element on the stack
		aux = []

		for x in self.__element_list:
			aux.append(x.value)

		return aux

	# Return a list with the next_node of each element in the stack, mainly used to test if the push was working.
	def get_nexts(self):
		aux = []

		for x in range(0, len(self.__element_list)):
			if x + 1 < len(self.__element_list):
				aux.append(self.__element_list[x].next_node.value)

		return aux

	def fix_list(self): # Links the list if the set was constructed from another stack/list and not empty
		for x in range(0, len(self.__element_list)):
			if x + 1 < len(self.__element_list):
				self.__element_list[x].next_node = self.__element_list[x + 1]

	def push(self, element): # Adds an element on the top of the stack 
		try:
			new_node = Linked_Node(element, self.__element_list[0])
			self.__element_list.insert(0, new_node)
			return element

		except TypeError:
			print("Invalid Push")

	def pop(self): # Deletes the element on the top of the stack
		aux = self.__element_list[0]
		self.__element_list.pop(0)

		return aux

	def peek(self): # Returns the top of the stack without removing it
		return self.__element_list[0].value

def main():
	node1 = Linked_Node(1)
	node2 = Linked_Node(2)
	node3 = Linked_Node(3)

	linked_list = [node1, node2, node3]
	stack = Stack(linked_list)
	stack.fix_list()
	stack.push(4)

	print(stack.get_list())
	print(stack.get_nexts())

	stack.push(7)
	stack.push(123)
	stack.pop()
	print(stack.peek())

	print(stack.get_list())


if __name__ == '__main__':
	main()