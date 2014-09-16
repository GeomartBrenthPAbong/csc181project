import class_script_adder
import class_style_adder
import scripts.global_variables as g


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
		header += '<meta charset="utf-8"/>'
		header += '<meta http-equiv="X-UA-Compatible" content="IE=edge">'
		header += '<meta name="viewport" content="width=device-width, initial-scale=1">'
		header += '<meta name="description" content="">'
		header += '<meta name="author" content="">'
		header += '<link rel="icon" href="' + g.g_locations.printContentsAtLocation('icon_path') +'">'
		header += '<title>'+ g.g_locations.printContentsAtLocation('head_title') +'</title>'
		header += self.__m_script_adder.generateScript()
		header += self.__m_style_adder.generateStyle()
		header += '</head><body>'
		header += g.g_locations.printContentsAtLocation('just_after_body_tag')

		return header
