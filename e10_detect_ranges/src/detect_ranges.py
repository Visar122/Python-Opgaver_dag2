def detect_ranges(L):
    List = L.copy()  #  copy of the original list to avoid modifying it
    List.sort()
    result = []
    start = List[0]
    end = List[0]
    for num in List[1:]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                result.append(start)
            else:
                result.append((start, end + 1))
            start = num
            end = num
    if start == end:
        result.append(start)
    else:
        result.append((start, end + 1))
    return result

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(result)

if __name__ == "__main__":
    main()
