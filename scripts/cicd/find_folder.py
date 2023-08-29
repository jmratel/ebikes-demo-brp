import sys
import os

def main():
	for arg in sys.argv[1:]:
		arg = arg.split('/')[-1]
		for(root, dirs, files) in os.walk('manifest'):
			for d in dirs:
				if arg.lower() == d.lower():
					print(root.replace('\\', '/') + '/' + d + '/package.xml')
					return root.replace('\\', '/') + '/' + d + '/package.xml'
	return None

if __name__ == '__main__':
	main()