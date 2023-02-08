import sys

# N 은 떡의개수 M은 손님이 원하는 떡의 총 길이

N, M = map(int, input().split())

tteok = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tteok)

#이진 탐색 시작 (반복)
result = 0
while start<=end:
    total = 0
    mid = (start + end) // 2
    for x in tteok:
        if x > mid:
            total += x - mid
    # 떡이 부족한 경우 더 많이자르기 (절단기 길이 감소 == 왼쪽 범위 탐색 )
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)


