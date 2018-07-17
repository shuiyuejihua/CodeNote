class Node(object):
	"""docstring for Node"""
	def __init__(self, value):
		self.value = value
		self.next = None

class LNode(object):
	"""docstring for LNode"""
	def __init__(self, head=None):
		self.head = head

	def append(self, value):
		if self.head:
			p = self.head
			while p.next:
				p = p.next
			p.next = Node(value)
		else:
			self.head = Node(value)

	def pop_last(self):
		if self.head == None:
			raise Exception('the LinkList is empty')
		else:
			p = self.head
			if p.next == None:
				e = p.next.value
				self.head = None
				return e
			while p.next.next:
				p = p.next
			e = p.next.value
			return e





		
		
		
