#!/usr/bin/python

from lxml import etree

class CppcheckData:

	scopes = []
	ast = []

	def xmlparseast(self, element):
		ret = []
		for child in element:
			if child.tag == 'token':
				token = {}
				token['text'] = token.get('text')
				varId = token.get('varId')
				if varId:
					token['varId'] = varId
				token['operands'] = self.xmlparseast(child)
				ret.append(token)
		return ret

	def __init__(self, filename):
		self.scopes = []
		self.ast = []

		data = etree.parse(filename)
		for element in data.getroot():
			if element.tag == 'scope':
				scope = {}
				scope['id'] = element.get('id')
				scope['nestedIn'] = element.get('nestedIn')
				className = element.get('className')
				if className:
					scope['className'] = className
				self.scopes.append(scope)

			elif element.tag == 'ast':
				self.ast.append(self.xmlparseast(element))


def parsedump(filename):
	return CppcheckData(filename)

