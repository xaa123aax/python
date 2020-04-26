students = {'Chang': {'Math': 90, 'Chinese': 85, 'English': 60},
            'Tang': {'Math': 85, 'Chinese': 70, 'English': 62},
            'Chen': {'Math': 90, 'Chinese': 93, 'English': 95}}
studenttatal = []
rank = []

for student in students:

    total = 0

    for grade in students[student]:
        total = total + students[student][grade]
    students[student].setdefault('total', total)
    studenttatal.append(total)

#print(students)
for i in studenttatal:

    rank1 = 1

    for j in studenttatal:
        total1=i
        if total1<j:
            rank1=rank1+1 
    rank.append(rank1)

#print(rank)
rank2=0
for student in students:
    #rank2=0
    students[student].setdefault('rank', rank[rank2])
    rank2 = rank2 + 1

print(students)