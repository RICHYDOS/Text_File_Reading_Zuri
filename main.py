# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from nbformat import read

def read_file_content(filename):
    #Open a file and read data from it
    new_file = open(filename, "r")

    #Store the read data in a new varaiable
    read_file = new_file.read()
    new_file.close()
    return read_file

def count_words():
    text = read_file_content("story.txt")

    #Split the contents of this file into a list
    list_file = text.split()
    our_count = dict()

    #Iterate over the list
    for word in list_file:
        count = 0
        for test in list_file:
            if word == test:
                count +=1

        # Add data to our dictionary        
        our_count[word] = count
    
    print(our_count)

count_words()


    



    
    
        
            
    

