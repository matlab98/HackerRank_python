if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    m=arr[-1]
    arr.sort(reverse=True)
    for x in arr:
        if x!=m:
            print(x)
            break
