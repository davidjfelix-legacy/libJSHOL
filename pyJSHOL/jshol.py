#!/usr/bin/env python
import json
from html.parser import HTMLParser


class InvalidJSHOLError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)


class JSHOLDecoder(JSONDecoder):
	pass


class JSHOLEncoder(JSONEncoder, HTMLParser):
	pass


def main():
	#TODO: add useage, parse parsables, action actionables, etc etcables
	pass


def parseAttrs(obj):
	if type(obj) is list:
		attr_string = ""
		content = ""
		for each in obj:
			content += parseTag(each)
		
	elif type(obj) is dict:
		attr_string = ""
		content = ""
		for each in obj.keys():
			if each == "content":
				if type(obj[each]) == list:
					for each2 in obj[each]:
						content += parseTag(each2)
				
				elif type(obj[each]) == dict:
					content = parseTag(obj[each])
					
				else: #FIXME steamroll it like it's a string
					content = str(obj[each])
			else:
				attr_string = attr_string + " " + each + '="' + obj[each] + '"'

	else: #FIXME: steamroll it like it's a string
		attr_string = ""
		content = str(obj)
		
	return (attr_string, content)


def parseTag(obj):
	# If you're giving me a tag with multiple definitions, this won't work
	if len(obj.keys()) != 1:
		raise InvalidJSHOLError("Can only have key per tag")
	
	# The first and only definition is the tag type
	tag = obj.keys()[0]
	tag_attrs = obj.get(key)
	tag_string = "<" + tag + "{0}>{1}</" + tag + ">" #FIXME: not all tags have end tags
	attrs_pair = parseAttrs(tag_attrs)
	return tag_string.format(attrs_pair)
	


def dumpsHTML(obj):
	html_string = "<!DOCTYPE html>\n{0}"
	HTML = parseTag(obj)
	return html_string.format(HTML)
	

def json2HTML(json_string):
	"""API function to load JSON and convert it to HTML"""
	obj = json.loads(json_string)
	return dumpsHTML(obj)


if __name__ == "__main__":
	main()
