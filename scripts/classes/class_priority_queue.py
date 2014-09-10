import class_heap


class PriorityQueue(object):
	def __init__(self):
		self.__m_heap = class_heap.Heap()

	def enqueue(self, p_tuple):
		self.__m_heap.insert(p_tuple)

	def findMin(self):
		return self.__m_heap.peak()

	def dequeue(self):
		self.__m_heap.deletePeak()

	def isEmpty(self):
		return self.__m_heap.isEmpty()

	def emptyQueue(self):
		while not self.__m_heap.isEmpty():
			self.__m_heap.deletePeak()