import string

# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as open_file:
        read_file = open_file.read()
        return read_file

dic = {}
def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    for line in text:
        line = text.strip()
        line = text.lower()
        line = text.translate(str.maketrans('', '', string.punctuation))
        line = line.replace('\n', ' ')
        words = line.rstrip("\n").split(" ")
        
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        return dic
        # print(sorted(dic.items()))

numbers = count_words()
print(numbers)

    # return {"as": 10, "would": 20}