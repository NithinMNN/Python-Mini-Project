def nameRank(names,marks,updates):
    for i in range(len(names)):
        marks[i]=marks[i]+updates[i]

    max_student=""
    max_marks=0

    for i in range(len(names)):
        if marks[i]>max_marks:
            max_student=names[i]
            max_marks=marks[i]

    pr=0
    previous_ranks=[]
    for x in range(len(names)):
        pr=x+1
        previous_ranks.append(pr)

    previous_rank=0
    for i in range(len(names)):
        if names[i]==max_student:
            previous_rank=previous_ranks[i]
            
    current_rank=0
    for i in range(len(marks)):
        if marks[i] == max_marks:
            current_rank+=1
    
    rankjump=previous_rank-current_rank
    
    print(f'The student with maximum marks after updation is: {max_student}')
    print('-------')
    print(f'Rank of {max_student} before marks updation is: {previous_rank}')
    print('-------')
    print(f'Rank of {max_student} after marks updation is: {current_rank}')
    print('-------')
    print(f'Jump in rank of {max_student} is: {rankjump}')
    print()
    
names=['Manish','Kamlesh','Riya','Megha']
marks=[90,86,80,77]
updates=[-7,3,12,8]

nameRank(names,marks,updates)
