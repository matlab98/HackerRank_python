from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    
    i = 1
    f=''
    while i <= n:
        f=f+str(i)
        i += 1
    print(f)