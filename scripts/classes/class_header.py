import class_script_adder
import class_style_adder
import scripts.global_variables


class Header(object):
	def __init__(self):
		self.__m_script_adder = class_script_adder.ScriptAdder()
		self.__m_style_adder = class_style_adder.StyleAdder()

	def getScriptAdder(self):
		return self.__m_script_adder

	def getStyleAdder(self):
		return self.__m_style_adder

	def generateHeader(self):
		header = '<!DOCTYPE html><head>'
		header += self.__m_script_adder.generateScript()
		header += self.__m_style_adder.generateStyle()
		header += '</head><body>'
		header += scripts.global_variables.g_locations.printContentsAtLocation('just_after_body_tag')

		return header
