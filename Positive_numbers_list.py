list1 = [12,-7,5,64,-14]
count=-1
for num in list1:
  count = count + 1
  if num >= 0:
    print(num,end=" ")
print("\n")
list2 = [12,14,-95,3]
for i in list2:
  if i<0:
    list2.remove(i)  
print(list2)
