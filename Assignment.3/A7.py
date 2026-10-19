def make_acronym(phrase):
    words = phrase.split()
    acronym = "".join(word[0].upper() for word in words)
    
    return acronym
if __name__ == "__main__":
    text = input("Nhập cụm từ: ")
    result = make_acronym(text)
    print("Viết tắt:", result)