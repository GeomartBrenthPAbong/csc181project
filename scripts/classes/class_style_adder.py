from class_scriptstyle_adder import ScriptStyleAdder

class StyleAdder(ScriptStyleAdder):
	def generateStyle(self):
		if not self._m_path_list:
			return ''
		import scripts.global_variables

		style = ''
		for path in self._m_path_list:
			style += '<link rel="stylesheet" href="' +  scripts.global_variables.g_root_path + '/css/' + path + '.css" />'
		return style