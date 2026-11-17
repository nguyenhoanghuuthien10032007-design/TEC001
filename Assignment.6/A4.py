def word_frequency(text):
    words = text.lower().split()
    frequencies = {}
    
    for word in words:
        # Strip basic punctuation if needed
        word = word.strip(".,!?;:\"'()")
        if word:
            frequencies[word] = frequencies.get(word, 0) + 1
            
    return frequencies

# Example usage:
sample_text = "Python is great and Python is easy to learn."
result = word_frequency(sample_text)
print(result)