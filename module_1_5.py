immutable_var = (1, 2, "papa")
print(immutable_var)
#immutable_var [0]=4
#print(immutable_var) #TypeError: 'tuple' object does not support item assignment
mutable_list = [1,2,'papa']
mutable_list[1]=5
print(mutable_list)
mutable_list.remove(1),mutable_list.append('mama')
print(mutable_list)