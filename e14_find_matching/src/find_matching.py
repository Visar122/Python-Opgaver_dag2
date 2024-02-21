def find_matching(L, pattern):
    indices = []
    for index, string in enumerate(L):
        if pattern in string:
            indices.append(index)
    return indices

def main():
    strings = ["sensitive", "engine", "rubbish", "comment"]
    pattern = "en"
    result = find_matching(strings, pattern)
    print(result)   

if __name__ == "__main__":
    main()
