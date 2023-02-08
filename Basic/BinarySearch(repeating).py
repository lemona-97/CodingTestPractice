

def BinarySearch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾았다면 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return BinarySearch(array, target, start, mid -1)
        else:
            return BinarySearch(array, target, mid + 1, end)

    return  None



N, target = map(int, input().split())

array = list(map(int, input().split()))
result = BinarySearch(array, target, 0, N-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)