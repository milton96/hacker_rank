if __name__ == '__main__':
    records = []
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        records.append([name, score])
        if score not in scores:
            scores.append(score)
    
    scores.sort()
    scores.pop(0)
    
    for rec in records:
        if rec[1] == scores[0]:
            students.append(rec[0])

    students.sort()
    print(*students, sep='\n')