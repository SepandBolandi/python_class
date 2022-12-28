item0 = 7
mylist = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78]
mylist.insert(0, item0)
print(mylist)
print(mylist[12])
mylist1 = ["Julia", "Python"]
mylist1.append("R")
print(mylist1)
thislist = ["SQL", "Scala"]
mylist1.extend(thislist)
print(mylist1)
mylist1.insert(1, "C++")
print(mylist1)
mylist1.remove("Julia")
print(mylist1)
mylist1.reverse()
print(mylist1)
list1 = [0, 0, 1, 0, 0, 1, 6, 0, 1, 0, 2, 1, 6, 6, 1, 0, 16, 1, 18, 0, 6, 2, 22, 1, 0, 6, 3, 6, 28, 1, 15, 0, 2, 16, 6, 1, 3, 18, 6, 0, 5, 6, 21, 2, 1, 22, 46, 1, 42, 0, 16, 6, 13, 3, 2, 6, 18, 28, 58, 1, 60, 15, 6, 0, 6, 2, 33, 16, 22, 6, 35, 1, 8, 3, 1, 18, 6, 6, 13, 0, 9, 5, 41, 6, 16, 21, 28, 2, 44, 1]
print(list1.count(0))
print(sum(list1))