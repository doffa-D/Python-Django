
class Text(str):
	def __str__(self):
		result = super().__str__().replace('>', '&gt;').replace('<', '&lt;')
		if result == '"':
			result = result.replace('"', '&quot;')
		return result.replace('\n', '\n<br />\n')


class Elem():
	class ValidationError(Exception):
		def __init__(self, msg= "This content is not a Text or a elem."):
			Exception.__init__(self, msg)

	def __init__(self,tag = "div",attr = None,content=None,tag_type="double"):
		self.tag = tag
		self.attr = attr
		self.content = []
		if content:
			self.add_content(content)
		elif content != None:
			if not isinstance(content,Text):
				raise Elem.ValidationError("this content is not valid")
		self.tag_type = tag_type

	def __str__(self):
		atrr = ""
		if self.attr is not None:
			for key,value in self.attr.items():
				atrr += f" {key}=\"{value}\""
			print(atrr)
		if self.tag_type == "double":
			return "<{}{}>{}</{}>".format(self.tag,atrr,self.__make_content(),self.tag)
		elif self.tag_type == "simple":
			return "<{}{} />".format(self.tag,atrr)
		else:
			raise Elem.ValidationError("not a valid tag_type")

		return self.content

	def add_content(self,content):
		if not Elem.check_type(content):
			raise Elem.ValidationError("not a valid tag_type")
		if isinstance(content,list):
			for elem in content:
				if elem != Text(''):
					self.content.append(elem)
		elif content != Text(''):
			self.content.append(content)
				
	def __make_content(self):
		if len(self.content) == 0:
			return ''
		result = '\n'
		for elem in self.content:
			elem = str(elem).replace('\n', '\n  ')
			result += '  ' + elem + '\n'
		return result
	
	def check_type(content):
		# Check if content is an instance of Elem
		if isinstance(content, Elem):
			return True

		# Check if content is a Text object
		if type(content) == Text:
			return True

		# Check if content is a list containing only Text and Elem objects
		if type(content) == list:
			for elem in content:
				if not isinstance(elem, Elem) and not type(elem) == Text:
					return False
			return True

		# If none of the above checks pass, return False
		return False
