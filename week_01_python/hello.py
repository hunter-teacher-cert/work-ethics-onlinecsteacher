#To run, write "python hello.py" in terminal command liine

print("Hello World!")
print("line two")
print("line 4")

#hit CTRL+D to escape from wrong terminal command

a = 5
if a > 3:
    print("a is greater than 3")
    print("in fact it's", a)
elif (a == 3):
    print("a is equal to 3")
else:
    pass

i = 0
while i < 10:
    print(i)
    i=i+1

for letter in "hello world":
    print(letter)

for item in ['a','b','c']:
    print(item)

print()

for value in range(5,15):
    print(value)

def add2(a,b):
    c = a + b
    return c

def main():
    c = add2(10, 20)
    print(c)



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




line = "this is a sentence"
for word in line.split(): #split splits a string on whitespace
                          #(or other if you pass in a parameter)
