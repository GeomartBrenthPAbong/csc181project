import scripts.global_variables

class Content(object):
	def __init__(self):
		self.__m_title = ''
		self.__m_content = ''
		self.__m_page_template = 'default'
		self.__m_page = 'homepage'
		self.__m_before_content = ''
		self.__m_after_content = ''

	def setPage(self, p_page):
		self.__m_page = p_page

	def setTitle(self, p_title):
		self.__m_title = p_title

	def setContent(self, p_content):
		self.__m_content = p_content

	def setPageTemplate(self, p_page_template):
		self.__m_page_template = p_page_template

	def setGeneratedContent(self, p_content):
		self.__m_content = p_content

	def getTitle(self):
		return self.__m_title

	def getContent(self):
		return self.__m_content

	def getPageTemplate(self):
		return self.__m_page_template

	def generateContent(self):
		content = scripts.global_variables.g_locations.printContentsAtLocation('just_before_content_tag')
		content += self.__m_content
		content += scripts.global_variables.g_locations.printContentsAtLocation('just_after_content_tag')

		return content