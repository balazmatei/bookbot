def word_counter(book):
    num_words = 0

    words = book.split()
    for word in range(len(words)):
        num_words += 1
           
    return num_words


def char_counter(book):
    counted = {}

    for char in book.lower():
        #key = book.lower[char]
        if char not in counted:
            counted[char] = +1
        else:
            counted[char] += 1
    
    return counted

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    sorted = [] #list of 2pair dictionaries [ {"char: a", "count: 20"}, etc.. ]
    temp_dict = {}

    for char in dict:
        count = dict[char]
        temp_dict = {"char": char, "count": count}
        sorted.append(temp_dict)
        

    sorted.sort(reverse=True, key=sort_on)

#okkkkkk        
    return sorted
    
    
    