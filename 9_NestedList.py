if __name__ == '__main__':
    student_name =[]
    marks = []
    for _ in range(int(input())):
        name = list()
        name.append(input())
        score = float(input())
        name.append(score)
        marks.append(score)
        student_name.append(name)
    marks.sort()
    min_value = marks[0]
    marks.remove(min_value)
    for i in marks:
        if i > min_value:
            second_lowest = i
            break
    second_lowest_name =[]
    for i in range(len(student_name)):
        if second_lowest in student_name[i]:
            second_lowest_name.append(student_name[i][0])
    second_lowest_name.sort()
    for i in second_lowest_name:
        print(i)

































