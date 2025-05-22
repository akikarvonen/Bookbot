from stats import word_count #returns an integer
from stats import character_count # retuns a dictionary of characters and their frequencies in the text
from stats import sorted_list_of_dicts #retirns a list of dictionaries
def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", word_count("books/frankenstein.txt"), "total words")
    print("--------- Character Count -------")    
    
    # report is a dictionary of characters
    report = character_count("books/frankenstein.txt")
        
    sorted_list = sorted_list_of_dicts(report)
    for item in sorted_list:
        c = item['char']
        num = item['num']
        if c.isalpha():
            print(f"{c}: {num}")        
    print("============= END ===============")
    
main()
