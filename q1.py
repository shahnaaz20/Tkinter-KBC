from ast import Num


list_students=[["Harry",37.21],["Barry",37.21],["Tina",37.2],["Akirti",41],["Harsh",39]]
low_g=0
s_low=0
list1=[]
minimum = list_students[0][1]
for each_student in list_students:
    index=0
    for j in each_student:
        if index==1:
            print("j---",j)
            if minimum > j:
                minimum = j
            else:
                list1.append(minimum)    
        index+=1
list2=[]
for l in list1:
    print(l)
    for j in list_students:
        if l in j:
            if j[0] not in list2:
                list2.append(j[0])
lsit3=sorted(list2)
print(lsit3[0])
print(lsit3[1])
