def my_list(file):
    file = open(file)
    x = open('items.txt')
    dictionary = [line.rstrip('\r\n') for line in allWords] 
    for line in file.readlines():
        line = line.strip()
        words = line.split()
        for word in items:
            word = word[0:word.find(",")]
            found = False
            index = 0
            for element in dictionary:
                if found:
                    break
                if word == element:
                    found = True
                    break
                elif word != element and index < len(dictionary)-1:
                    index = index + 1
                else:
                    print("The word " + word + " is not in the dictionary"break)
