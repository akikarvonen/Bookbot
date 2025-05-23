from stats import word_count, character_count, sorted_list_of_dicts
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    def main():
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print("Found", word_count(sys.argv[1]), "total words")
        print("--------- Character Count -------")    
        
        # report is a dictionary of characters
        report = character_count(sys.argv[1])
            
        sorted_list = sorted_list_of_dicts(report)
        for item in sorted_list:
            c = item['char']
            num = item['num']
            if c.isalpha():
                print(f"{c}: {num}")        
        print("============= END ===============")

main()
