if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lis = list(arr)
    lis.sort()
    max1 = lis[-1]
    print(max1)
    lis.sort(reverse=True)
    for x in lis:
        if x != max1:
            print(x)
            break


























