import class_priority_queue


class Locations(object):
	def __init__(self):
		self.__m_locations = {}

	def registerLocation(self, p_location_name):
		self.__m_locations[p_location_name] = class_priority_queue.PriorityQueue()

	def addToLocation(self, p_location_name, p_location_content, p_priority_number = 10):
		if not p_location_name in self.__m_locations:
			self.registerLocation(p_location_name)
		self.__m_locations[p_location_name].enqueue((p_priority_number, p_location_content))

	def getContentsAtLocation(self, p_location_name):
		if not p_location_name in self.__m_locations:
			return None

		priority_queue = self.__m_locations[p_location_name]
		location_contents = class_priority_queue.PriorityQueue()

		contents = []
		while not self.__m_locations[p_location_name].isEmpty():
			(key, value) = priority_queue.findMin()
			contents.append(value)
			location_contents.enqueue((key, value))
			priority_queue.dequeue()

		self.__m_locations[p_location_name] = location_contents

		return contents

	def printContentsAtLocation(self, p_location_name):
		if not p_location_name in self.__m_locations or self.__m_locations[p_location_name] is None:
			return ''

		priority_queue = self.__m_locations[p_location_name]

		content = ''
		while not priority_queue.isEmpty():
			(_, value) = priority_queue.findMin()
			content += value.toString()
			priority_queue.dequeue()

		return content

	def clearLocation(self, p_location_name):
		if not p_location_name in self.__m_locations:
			return
		self.__m_locations[p_location_name].emptyQueue()