book='file.txt'
x=open(book, 'r') 
    items = x.read().split()
def empty(word):
    empties = ''
    for char in word:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            cleansed += char.lower()
    return cleansed
        
print("{} has {} 'words'".format(book, len([clean(word) for word in words])))

