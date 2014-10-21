from class_scriptstyle_adder import ScriptStyleAdder

class ScriptAdder(ScriptStyleAdder):
	def __init__(self):
		super(ScriptAdder, self).__init__()
		self._m_type = 'js'
		self._m_folder = 'javascript'

	def generateScript(self):
		if not self._m_path_list:
			return ''
		import scripts.global_variables

		script = ''
		for path in self._m_path_list:
			script += '<script src=" ' + scripts.global_variables.g_root_path + '/javascript/' + path + '.js "></script>'
		return script
