import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


from stats import word_counter, char_counter, sort_dict

with open(sys.argv[1]) as f:
    contents_f = f.read()


def get_book_text(book):
    get_book = print(book)

    return get_book


def main():
    total_words = word_counter(contents_f)
    total_chars = char_counter(contents_f)
    total_sorted = sort_dict(total_chars) 
    message1 = print("============ BOOKBOT ============")
    message2 = print(f"Analyzing book found at", sys.argv[1], "...")
    message3 = print("----------- Word Count ----------")
    message4 = print(f"Found", total_words, "total words")
    message5 = print("--------- Character Count -------")
    message6 = ""
    for i in total_sorted:
        if i["char"].isalpha() == True:
            message6 = print(f"{i["char"]}: {i["count"]}")
            
            
    message7 = print("============= END ===============")




    return message1, message2, message3, message4, message5, message6, message7

main()



#e: 44538