import re

def find_name(line):
    pattern = r"[A-Z][a-z.]*[\ ][A-Z][a-z]*"

    #I would think this would print names with First Middle Last but it doesn't
    # print out anything but the third name
    #pattern = r"[A-Z][a-z.]*[\ ][A-Z][a-z]*([\ ][A-Z][a-z]*)*"

    result = re.findall(pattern,line)

    return result


f = open("namefile.dat")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)

"""
def find_date(line):
    pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
    result = re.findall(pattern,line)

    pattern = r"(October|Oct|November|Nov)( \d{1,2}, \d{4})"
    result = result + re.findall(pattern,line)
    return result

#result = find_date("10/15/2023 is a October 13, 2025 date as is 1/23/19")
#print(result)

f = open("datefile.dat")
for line in f.readlines():
    #print(line)
    result = find_date(line)
    if (len(result)>0):
        print(result)
"""
