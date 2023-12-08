import re
from collections import defaultdict

def process_text(text):
    # Splitting the text into pages based on the page number pattern
    #we should ignore page numbers that start with the nubmer 3
    #pages = re.split(r'\n\d+\n', text)
    pages = re.split(r'\n[5-7]\d+\n', text)

    # Sanity check
#    for i, page in enumerate(pages, start=505):  # Assuming 505 is the first page number
#        if str(i) not in page:
#            print(i)
#            raise ValueError('Page numbers are not in order')

    
    # Dictionary to store the words with their respective page numbers
    word_dict = defaultdict(set)

    # Process each page
    for i, page in enumerate(pages, start=505):  # Assuming 505 is the first page number
        # Extract words from the page
        words = re.findall(r'\b\w+\b', page)
        for word in words:
            word_dict[word.lower()].add(i)

    # Convert sets to sorted lists
    word_dict = {word: sorted(list(pages)) for word, pages in word_dict.items()}

    return word_dict

# Example text input (shortened for demonstration purposes)
text = """
506
○ Copyright protection = qualified good with some deadweight loss. Goal is
optimal, not maximum, creative output
...
507
○ Cons: narrow group determines innovation; biased; taxpayer costs
...
"""

#read the text from the file ipnotes.txt
actual_text = open("ipnotes.txt", "r")

# Process the text and create the dictionary
#word_dict = process_text(text)
word_dict = process_text(actual_text.read())


# Output the dictionary
word_dict_output = {word: pages for word, pages in word_dict.items()}
#print(word_dict_output)

#format the output sort the dictionary by word, and make it so that each word and its pages are on a separate line when we write it to the file

#sort the dictionary by word
sorted_dict = sorted(word_dict_output.items(), key=lambda x: x[0])

#write the dictionary to a file
with open("output.txt", "w") as f:
    for key, value in sorted_dict:
        f.write('%s:%s\n' % (key, value))


