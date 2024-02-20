def reverse_dictionary(d):
    reverse_d = {}
    for english_word, finnish_words in d.items():
        for finnish_word in finnish_words:
            if finnish_word not in reverse_d:
                reverse_d[finnish_word] = []
            reverse_d[finnish_word].append(english_word)
    return reverse_d

def main():
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    result = reverse_dictionary(d)
    print(result)

if __name__ == "__main__":
    main()
