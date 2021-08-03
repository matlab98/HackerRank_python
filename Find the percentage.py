if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    sum =student_marks[query_name][0]+student_marks[query_name][1]+student_marks[query_name][2]
    div = sum/3
    print("{:.2f}".format(div))

#or

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks:
        j = student_marks.get(i)
        if i==query_name:
            result = 0
            for k in j:
                result+= float(k)
            print("{:.2f}".format((result/len(j))))
            break
        else:
            continue