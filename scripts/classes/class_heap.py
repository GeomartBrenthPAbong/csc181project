class Heap(object):

	def __init__(self, p_type = True):
		self.__m_size = 0
		self.__m_list = []
		self.__m_type = p_type

	# tuple p_tuple a tuple which consists of key and data
	#				key is the one used for comparison
	def insert(self, p_tuple):
		self.__m_list.append(p_tuple)
		self.__shiftUp(self.__m_size)
		self.__m_size += 1

	def peak(self):
		if self.isEmpty():
			return None
		return self.__m_list[0]

	def deletePeak(self):
		if self.isEmpty():
			return
		self.__m_size -= 1
		self.__m_list[0] = self.__m_list[self.__m_size]
		del self.__m_list[self.__m_size]
		self.__shiftDown(0)

	def isEmpty(self):
		return self.__m_size == 0

	def size(self):
		return self.__m_size

	def __shiftUp(self, p_target):
		if p_target <= 0:
			return

		parent_node = p_target // 2

		# If min heap
		if self.__m_type:
			if self.__m_list[parent_node][0] > self.__m_list[p_target][0]:
				self.__swap(parent_node, p_target)
				self.__shiftUp(parent_node)
		# If max heap
		else:
			if self.__m_list[parent_node][0] < self.__m_list[p_target][0]:
				self.__swap(parent_node, p_target)
				self.__shiftUp(parent_node)

	def __shiftDown(self, p_target):
		if p_target >= self.__m_size:
			return

		left_node = p_target * 2
		right_node = left_node + 1

		if left_node >= self.__m_size or right_node >= self.__m_size :
			return

		# If min heap
		if self.__m_type:
			if right_node < self.__m_size:
				min_node = self.__min(left_node, right_node)
			else:
				min_node = left_node

			if self.__m_list[p_target][0] > self.__m_list[min_node][0]:
				self.__swap(p_target, min_node)
				self.__shiftDown(min_node)
		# If max heap
		else:
			if right_node < self.__m_size:
				max_node = self.__max(left_node, right_node)
			else:
				max_node = left_node

			if self.__m_list[p_target][0] < self.__m_list[max_node][0]:
				self.__swap(p_target, max_node)
				self.__shiftDown(max_node)

	def __swap(self, p_index_one, p_index_two):
		temp = self.__m_list[p_index_one]
		self.__m_list[p_index_one] = self.__m_list[p_index_two]
		self.__m_list[p_index_two] = temp

	def __min(self, p_index_one, p_index_two):
		if self.__m_list[p_index_one][0] <= self.__m_list[p_index_two][0]:
			return p_index_one
		else:
			return p_index_two

	def __max(self, p_index_one, p_index_two):
		if self.__m_list[p_index_one][0] >= self.__m_list[p_index_two][0]:
			return p_index_one
		else:
			return p_index_two