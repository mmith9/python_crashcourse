print("Hello")
message="a simple message"
print(message)
print(message.title(),end ="")
print(message.count("a"))
print(message.center(10,"z"))
print(f"{message.title()}\t{message}\t{2+4}")
msg2=f"        {message.title()}\t{message}\t{2+4}     "
print(msg2,"a")
print(msg2.strip(),"a")
a_list=[i*i for i in range(0,11)]

print(len(a_list))
print(range(0,len(a_list)))
#a_list.append("appendix")
#a_list.insert(3,"instertix")

for i in range(0,len(a_list)) :
    print(i,end="\t")
    print(a_list[i],end="\t")
    print(a_list[-1-i])

#for i in range(0,len(a_list)):
#    a_list[i]=str(a_list[i])


#a_list.sort()
#a_list.sort()
#for i in range(0,len(a_list)) :
#    a_list.remove(a_list[0])
#    print(a_list)

print(a_list)
print(len(a_list))
middle=int(len(a_list)/2)
print(middle)
print(a_list[0:middle])
print(a_list[middle:len(a_list)])

next_list=a_list
print(next_list)

static_list=(0,1,2,3,4,5,)
print(static_list," bla")
static_list=(1,)
print(static_list)
if 1 in static_list:
    print("1 is in static_list")
if 2 not in static_list:
    print("2 not in static_list")
car="citroen"
print(car.lower()=="CitroEn".lower())

print(10<20 and 20>=20)

data="simple or not"
if len(data) <5 :
    print ("short")
elif len(data)<9:
    print("medium")
elif len(data)>=9:
    print("large")
else :
    pass

list=[]
for x in list:
    print(x)

if list:
    print(list)
else:
    print("empty!")

dick={"1":"key1", 3: "third", "color":"black"}
print(dick)
dick["4th"]="fourth"
print(dick)
print(dick.popitem())
print(dick)
print(dick.pop("1"))
print(dick)
del dick[3]
print(dick)

newdick={
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
    "key4":"value3",
    "key5":"value1"
    }

print(newdick)
print(newdick.get("some key","unknown key"))
print(newdick.items())
for key, value in newdick.items():
    print (key,value)

print(newdick.values())
print(sorted(newdick.values()))
print(sorted(set(newdick.values())))
print(type(newdick))
print(newdick["key1"])

#name=input("name pliz ")
#print(name)
#print(f"The name variable has value: {name}, //formatted by fstring")
#if name.isnumeric():
#    print(int(name))
#else:
#    print("not a number")

def copylist(first,second):
    while first:
        second.append(first.pop())

firstlist=[1,2,3,4,5,6]
secondlist=[]

print(f"firstlist {firstlist} secondlist{secondlist}")
print("copying")
copylist(firstlist[:],secondlist)
print(f"firstlist {firstlist} secondlist{secondlist}")

def copyvalue(first,second):
    second=first

v1=100
v2=0
copyvalue(v1,v2)
print(v1,v2)

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)


class drukarka3d:
    def __init__(self,model):
        self.model=model
        self.filament="undefined"
        self.bedsize="undefined"
        self.state="undefined"
    def insert_filament(self,filament):
        self.filament=filament
        print(f"Założono filament{filament}")
    def drukuj(self,co):
        print(f"Drukuje {co}")
        self.state="printing"
    
mojender=drukarka3d("ender 3")
mojender.insert_filament(["pla","szary","1.75mm","100m"])
mojender.drukuj("statek")
print(mojender.state)

with open("pi_digits.txt") as file_object:
    contents=file_object.read()
print(contents.rstrip())
print("_end_")

pi_string=""
with open("pi_digits.txt") as file_object:
    lines=file_object.readlines()

for line in lines:
    pi_string+=line.strip()

print(pi_string)
print(lines)

with open("pi_million.txt") as file_object:
    lines=file_object.readlines()

pi_string=""
for line in lines:
    pi_string+=line.strip()

print(f"Pi i 50 cyfr po przecinku: {pi_string[:52]}")

try:
    print(50/0)
except FileNotFoundError:
    pass
except ZeroDivisionError:
    print("Division by zero!")

filename="alice.txt"

try:
    with open(filename) as f:
        contents=f.read()
except FileNotFoundError:
    print(f"Plik {filename} nie istnieje!")
else:
    lines=contents.split()
    print(f"Plik {filename} zawiera około {len(lines)} słów.")
    print(lines[10001:10050])

import json
filename="json_dump.json"
with open(filename,"w") as f:
    json.dump(lines[10000:11000],f)

with open(filename,"r") as f:
    test=json.load(f)
print(test)

def sample_function(first , second="2" , third="3"):
    return (f"first:{first} second:{second} third:{third}")

import unittest

class SampleTest(unittest.TestCase):
    """Test for sample_function"""
    
    def test_1param(self):
        output=sample_function("3")
        self.assertEqual(output,"first:3 second:2 third:3")
    
    if __name__ == '__main__':
         unittest.main()

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

import unittest
#from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """"Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    if __name__ == '__main__':
        unittest.main()