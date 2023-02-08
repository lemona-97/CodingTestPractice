# target에 해당하는 원소가 몇번째 원소인지 출력

# 재귀
def BinarySearch(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif target < array[mid]:
        return BinarySearch(array, target, start, mid-1)
    else:
        return BinarySearch(array, target, mid+1, end)


n, target = map(int, input().split())

array = list(map(int, input().split()))

result = BinarySearch(array, target, 0, n-1)
if result == None:
    print("원소가 존재 하지 않습니다.")
else:
    print(result+1)