#!/usr/bin/env python3

def merge(L1, L2):
    merged = []
    i, j = 0, 0
    
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1
    
   
    while i < len(L1):
        merged.append(L1[i])
        i += 1
    
    while j < len(L2):
        merged.append(L2[j])
        j += 1
    
    return merged

def main():
    L1 = [1, 3, 5]
    L2 = [2, 4, 6]
    print(merge(L1, L2))  # Output: [1, 2, 3, 4, 5, 6]

    L3 = [1, 2, 3]
    L4 = [4, 5, 6]
    print(merge(L3, L4))  # Output: [1, 2, 3, 4, 5, 6]

if __name__ == "__main__":
    main()
