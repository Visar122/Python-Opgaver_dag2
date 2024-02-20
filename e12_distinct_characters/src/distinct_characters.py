#!/usr/bin/env python3

def distinct_characters(L):
    d = {}
    for w in L:
       distinct_count=len(set(w))
       d[w] = distinct_count
    return d

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
