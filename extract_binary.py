import sys

def main():
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	with open(output_file, 'wb') as outF:
		with open(input_file, 'r') as inF:
			for line in inF:
				for i in xrange(11,26,5):
					bytes = ''.join(map(chr, [int(line[i+2:i+4], 16), int(line[i:i+2], 16)]))
					outF.write(bytes)
					
			

if __name__ == "__main__":
    main()