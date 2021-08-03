def mutate_string(string, position, character):
    l=list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# A another version of this code is:

def mutate_string(string, position, character):
    l = string[:position] + character + string[position+1:]
    return l

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
