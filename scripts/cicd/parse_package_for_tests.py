from logging import exception
import os
import sys
import traceback
import re
import xml.etree.ElementTree as ET

def namespace(element):
	m = re.match(r'\{.*\}', element.tag)
	return m.group(0) if m else ''

def main():
	if len(sys.argv) != 2:
		return None

	try:
		tree = ET.parse(sys.argv[1])
		root = tree.getroot()
		ns = namespace(root)
		classlist = []
		for el in root:
			apexclass_node = None
			for el2 in el:
				if el2.text != None and el2.text.lower() == 'apexclass':
					apexclass_node = el
			if apexclass_node != None:
				for m in apexclass_node.findall(ns + 'members'):
					#print(m.text)
					if m.text and m.text[-4:].lower() == 'test':
						classlist.append(m.text)
		print(str.join(', ', classlist))
	except ET.ParseError as e:
		print(traceback.format_exc())



if __name__ == '__main__':
	main()