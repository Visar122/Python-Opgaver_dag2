#!/usr/bin/env python3

def transform(s1, s2):
    list1=list(map(int,s1.split())) #map() convert the string to integer
    list2=list(map(int,s2.split()))
    
    result = [x * y for x, y in zip(list1, list2)]  #sætter result i en ny liste
    
    return result

def main():
    result = transform("1 5 3", "2 6 -1")
    print(result)
if __name__ == "__main__":
    main()
