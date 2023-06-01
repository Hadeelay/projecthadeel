### Question 1 ###
name = ["Tarteel","Asmaa","Ahmed"]
name.insert(0,"Sabrin")
print(name)
name.remove("Ahmed")
print(name)
name.append("Hamda")
print(name)
name.remove("Asmaa")
print(name)

### Question 2 ###
frinds = ["Adel","Ahmed"]
employees = ["Samah","Amjad"]
school = ["Ali","Basma"]
MERG = [*frinds, *employees, *school]
print(MERG)

### Question 3 ###
dic1 ={1: 10, 2: 20}
dic2 ={3: 30, 4: 40}
dic3 ={5: 50, 6: 60}
dic4 ={}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)

### Question 4 ###
d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)

##USE INPUT##
n=int(input("Enter number: "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x
print(d)

### Question 5 ###
dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}
var = {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2)}
print(var)



### Question 6 ###
keys = ["Ten","Twenty","Thirty"]
values = [10, 20, 30]
sol = dict(zip(keys,values))
print(sol)

### Question 7 ###
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])


### Question 8 ###
my_dict = {1:"Alaa", 5:"Hadeel", 7:"Hanin", 13:"Malak"}
my_key = my_dict.keys()
my_val = my_dict.values()
for key,value in my_dict.items():
    if key < 10:
        print(value,end="->")

