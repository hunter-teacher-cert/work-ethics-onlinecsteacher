# For dictionaries you can write a program that reads a file and uses a dictionary to count the number of times each word appears.

dict={}

dict['one']=23
dict['two']="hello world"
dict[3] = 55.3
dict[0] = [1,2,3,4,5]
dict['jl']=lawrence

print(dict)

print(dict[0])
print(dict[0][3])
print(dict.keys())
print(dict.values())

for k in dict.keys():
    print(k,dict[k])


# also reading a file:
f = open("data.dat")
for line in f.readlines():
    line = line.strip()
    print(line)
