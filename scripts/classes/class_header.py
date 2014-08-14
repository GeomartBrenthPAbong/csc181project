import class_script_adder
import class_style_adder

class Header(object):
	__m_script_adder = class_script_adder.ScriptAdder()
	__m_style_adder = class_style_adder.StyleAdder()

	def __init__(self):
		self.__m_after_body = ''

	def getScriptAdder(self):
		return self.__m_script_adder

	def getStyleAdder(self):
		return self.__m_style_adder

	def addAfterBody(self, p_something_after_body):
		self.__m_after_body = p_something_after_body

	def generateHeader(self):
		header = '<!DOCTYPE html><head>'
		header += self.__m_script_adder.generateScript()
		header += self.__m_style_adder.generateStyle()

		header += '</head><body>'
		header += self.__m_after_body

		return header
