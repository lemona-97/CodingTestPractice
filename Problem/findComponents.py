import sys

N = int(input())

numbersA = list(map(int, sys.stdin.readline().split()))
numbersA.sort()

M = int(input())

numbersB = list(map(int, sys.stdin.readline().split()))

def BinarySearch(array, target, start, end):
    if start >= end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return BinarySearch(array, target, start, mid - 1)
    else:
        return BinarySearch(array, target, mid + 1, end)

for element in numbersB:
    if BinarySearch(numbersA, element, 0, N) != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")
