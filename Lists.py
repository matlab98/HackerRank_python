if __name__ == '__main__':
    lst = []
    N = int(raw_input())
    for x in range(N):
        on = list(raw_input().split(" "))
        if on[0] == "insert":
            a,b = map(int, (on[1],on[2]))
            lst.insert(a,b)
            
        elif on[0] == "append":
            lst.append(int(on[1]))
        
        elif on[0] == "remove":
            lst.remove(int(on[1]))
        
        elif on[0] == "sort":
            lst.sort()
            
        elif on[0] == "pop":
            lst.pop()
        
        elif on[0] == "reverse":
            lst.reverse()
            
        elif on[0] == "print":
            print(lst)