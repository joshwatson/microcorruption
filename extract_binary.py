import sys

def main():
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	with open(output_file, 'wb') as outF:
		with open(input_file, 'r') as inF:
			for line in inF:
				outF.write(line[11:31])
					
			

if __name__ == "__main__":
    main()