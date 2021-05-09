# Importing Libraries
import re


# Function "task_2"
def task_2():

	# Word list that store each word of file
	word_list = []

	# Word set that store unique word of file
	word_list_set = set()

	# Dictionary for word frequency counting
	word_frequency = dict()

	# Opening file for reading
	with open("ReaderFiles/read_file.txt", 'r') as read_file:
		
		for line in read_file:
			for word in line.split():
				
				# Extracting word using regular expression
				word = re.findall('[A-Za-z]+', word)
				if word:

					# Adding word to list and set
					word_list.append(word[0].lower())
					word_list_set.add(word[0].lower())
					
					# Increment the frequency of word
					if word[0].lower() not in word_frequency:
						word_frequency[word[0].lower()] = 0
						word_frequency[word[0].lower()] = word_frequency[word[0].lower()] + 1
					
					else:
						word_frequency[word[0].lower()] = word_frequency[word[0].lower()] + 1

	read_file.close() # File close


	# Opening/Create file for writing
	with open("WriterFiles/write_file_2.txt", 'w') as write_file:
		
		# Writing content in form of [WORD --> FREQUENCY of that WORD]
		for word in word_list_set:
			write_file.write(word+" --> ")
			write_file.write(str(word_frequency[word]))
			write_file.write("\n")

	write_file.close() # Close file


# Main function
if __name__ == "__main__":
	task_2()