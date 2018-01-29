import time
public_num =  0
def read_words(words_file_name):
    '''
    This piece of code is from professor Jan pearce
    This function opens a file with the name in 'words_file', reads in
    the contents and returns a list of the words, stripped of whitespace.
    pre: none, as this function handles IOError for when the file is not there gracefully
    post: returns the list of words in the file, which is empty on an open fail.
    '''
    words_list =[]
    try:
        open_file = open(words_file_name, 'r')
        contents = open_file.readlines()

        # replace punctuation with a blank space
        punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
        for i in punctuation:
            for j in range(len(contents)):
                contents[j] = contents[j].replace(i,"")

        for i in range(len(contents)):
            contents[i].lower()
            words_list.extend((contents[i].lower()).split()) # puts words into list
        open_file.close()
    except IOError:
        print ("File does not exist! Try again.")
    return words_list

def linear_search(search):
    '''
    this function runs through the text linearly.
    :param search: this is the word that is being looked for
    :return: this returns a dictionary that consists of the time it took to run the linear function and the amout of times the word was found
    '''
    lSearch =time.clock()
    number=0
    for i in read_words("text.txt"):
        if(i == search):
            number+=1
    return {"time":(time.clock()-lSearch), "amount":number}


# this section of the code is largly enspired by a youtuber that goes by fedmich
def binary_search(key):
    '''
    this function runs through the text binarily.
    :param key: this is the word that is being looked for
    :return: this returns a dictionary that consists of the time it took to run the binary function
    and the amount of times the word was found, it also tells how long it took to run with/without the sorted function
    '''
    bSearch = time.clock()
    array = sorted(read_words("text.txt"))
    search_time = time.clock()-bSearch
    number = 0
    low = 0
    high = len(array) - 1

    sTime = time.clock()
    while high >= low:
        mid = (low + high) // 2
        midval = array[mid]
        if midval < key:
            low = mid + 1
        elif midval > key:
            high = mid - 1
        else:
            while midval == array[mid]:
                mid+=1
            mid-=1
            while midval == array[mid]:
                mid-=1
                number+=1
            return {"time":(time.clock()-sTime), "amount":number, "full time": search_time}


def main():

    #input_words = read_words("text.txt")
    key = input("what word are you serching for ")
    print ("it took the linear search ",linear_search(key)["time"],"seconds to find",key,linear_search(key)["amount"],"times")
    print ("it took the binary search and sort",binary_search(key)["full time"] + binary_search(key)["time"],"seconds to find",key,binary_search(key)["amount"],"times")
    print ("it took the binary search ",binary_search(key)["time"],"seconds to find",key,binary_search(key)["amount"],"times")
if __name__ == '__main__':
    main()
