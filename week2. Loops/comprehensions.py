def main():
    words = get_words("address,txt") #opens file
    lowercase_words = [word.lower() for word in words if len(word) > 4]

    counts = {word: words.count(word) for word in lowercase_words}

        
    save_counts(counts) #another file .csv

main()