import sys
import json

def main():
	job_json = json.loads(sys.argv[1])
	job_id = job_json["result"]["id"]
	return job_id

if __name__ == '__main__':
	main()