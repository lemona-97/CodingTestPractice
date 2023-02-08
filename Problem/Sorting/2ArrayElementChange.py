N, K = map(int , input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

def changeElement(listA, listB):
    listA.sort()
    listB.sort(reverse= True)
    for i in range(K):
        if listA[i] < listB[i]:
            listA[i], listB[i] = listB[i], listA[i]
        else:
            break
    print(sum(listA))

changeElement(A, B)