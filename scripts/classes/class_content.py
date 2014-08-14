class Content(object):
	def __init__(self):
		self.__m_title = ''
		self.__m_content = ''
		self.__m_page_template = 'default'
		self.__m_page = 'homepage'
		self.__m_before_content = ''
		self.__m_after_content = ''

	def extractPage(self, p_page):
		self.__m_page = p_page

	def setTitle(self, p_title):
		self.__m_title = p_title

	def setContent(self, p_content):
		self.__m_content = p_content

	def setPageTemplate(self, p_page_template):
		self.__m_page_template = p_page_template

	def setGeneratedContent(self, p_content):
		self.__m_content = p_content

	def addBeforeContent(self, p_something_before_content):
		self.__m_before_content = p_something_before_content

	def addAfterContent(self, p_something_after_content):
		self.__m_after_content = p_something_after_content

	def getTitle(self):
		return self.__m_title

	def getContent(self):
		return self.__m_content

	def getPageTemplate(self):
		return self.__m_page_template

	def getBeforeContent(self):
		return self.__m_before_content

	def getAfterContent(self):
		return self.__m_after_content

	def generateContent(self):
		__import__('scripts.pages.' + self.__m_page)
		__import__('scripts.page_templates.' + self.__m_page_template)

		self.__m_content += self.__m_before_content
		self.__m_content += self.__m_after_content

		return self.__m_content