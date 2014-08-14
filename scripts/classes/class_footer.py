import class_script_adder
class Footer(object):
	__m_script_adder = class_script_adder.ScriptAdder()

	def __init__(self):
		self.__m_before_body = ''

	def getScriptAdder(self):
		return self.__m_script_adder

	def addSomethingBeforeBody(self, p_something_before_body):
		self.__m_before_body = p_something_before_body

	def generateFooter(self):
		footer = ''
		footer += self.__m_script_adder.generateScript()
		footer += self.__m_before_body
		footer += '</body></html>'

		return footer