#!/usr/bin/env python3

def interleave(*lists):
    interleaved = []
    for elements in zip(*lists):
        interleaved.extend(elements) #extend holder dem i en linje
    return interleaved

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
