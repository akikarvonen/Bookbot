#Assignment: CH2: Data analysis L4: Count words
def word_count(filepath):
    with open(filepath) as f:
        book = f.read()
    
    list_of_words = book.split()
    count = len(list_of_words)

    return count


def character_count(filepath):
    book = None
    
    # open the book as a string
    with open(filepath) as f:
        book = f.read()
    # lowercase every letter in the book
    book = book.lower()
    
    # create the dictionary of characters
    character_dict = {}
    
    # insert characters as keys and their frequencies as values
    for character in book:
        
        if character in character_dict:
            character_dict[character] += 1

        else:
            character_dict[character] = 1            
 
    return character_dict


def sorted_list_of_dicts(dictionary_of_characters):
    the_list = []
    
    for entry in dictionary_of_characters:
        count = dictionary_of_characters[entry]
        the_list.append({"char":entry,"num":count})        

        # key for the sorting
        def sort_on(dict):
            return dict["num"]
        
        # sort the list
        the_list.sort(reverse=True, key=sort_on)
    
    return the_list
