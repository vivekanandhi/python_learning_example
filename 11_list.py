if __name__ == '__main__':
    lis = []
    N = int(input())
    for i in range(N):
        mn = list(input("").split(" "))

        if mn[0]== "insert":
            a,b = map (int, (mn[1], mn[2]))
            lis.insert(a,b)

        elif mn[0]== "print":
            print(lis)

        elif mn[0]== "remove":
            lis.remove(int(mn[1]))

        elif mn[0]== "append":
            lis.append(int(mn[1]))

        elif mn[0]== "sort":
            lis.sort()

        elif mn[0]== "pop":
            lis.pop()

        elif mn[0]== "reverse":
            lis.reverse()


