# Importing Libraries
import re


# Function "task_1"
def task_1():

	# List that stores word from text file
	word_list = []

	# Opening file for reading
	with open("ReaderFiles/read_file.txt", 'r') as read_file:
		
		for line in read_file:
			for word in line.split():

				# Extract word using regular expression and adding in list
				word = re.findall('[A-Za-z]+', word)
				if word:
					word_list.append(word[0].capitalize())

	read_file.close() # File close

	
	# Opening/Creating file for writing
	with open("WriterFiles/write_file_1.txt", 'w') as write_file:
		for word in word_list:

			# Writing content
			write_file.write(word+" ")

	write_file.close() # File close


# Main function
if __name__ == "__main__":
	task_1()