import class_script_adder
import scripts.global_variables


class Footer(object):
	def __init__(self):
		self.__m_script_adder = class_script_adder.ScriptAdder()

	def getScriptAdder(self):
		return self.__m_script_adder

	def generateFooter(self):
		footer = ''
		footer += self.__m_script_adder.generateScript()
		footer += scripts.global_variables.g_locations.printContentsAtLocation('just_before_body_tag')
		footer += '</body></html>'

		return footer