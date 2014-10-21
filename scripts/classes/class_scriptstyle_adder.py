class ScriptStyleAdder(object):

	def __init__(self):
		self._m_path_list = []
		self._m_type = None
		self._m_folder = None

	def add(self, p_path):
		self._m_path_list.append(p_path)

	def getList(self, p_exclude = []):
		if not self._m_path_list:
			return []

		import scripts.global_variables as g

		fullpath_list = []

		for path in self._m_path_list:
			if p_exclude and path in p_exclude:
				continue
			fullpath_list.append(g.g_root_path + '/' + self._m_folder + '/' + path + '.' + self._m_type)
		return fullpath_list