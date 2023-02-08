N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))

def sorting(list):
    list.sort(reverse= True)
    print(list)
sorting(numbers)