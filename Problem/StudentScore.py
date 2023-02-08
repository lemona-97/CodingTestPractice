N = int(input())

studentWithScore = []
for _ in range(N):
    student, score = input().split()
    studentWithScore.append((student, int(score)))

def sortStudentByScore(studentsList):
    studentsList.sort(key= lambda studentsList : studentsList[1])
    print(studentsList)


sortStudentByScore(studentWithScore)