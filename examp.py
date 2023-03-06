squares=[x**2 for x in range(10)]
twos=[2**i for i in range(8)]
odds=[x for x in squares if x%2!=0]
print(twos)
print(odds)

# A four-column/four-row table ‒ a two dimensional array (4x4)
 
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]
 
print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'


i=0
while i<=3:
    i+=2
    print("*")

i=0
while i<=5:
    i+=1
    if i%2==0:
        break
    print("*")
for i in range(1):
    print("#")
else:
    print("#")

var =1
while var<10:
    var+=1
    
    print("#")
    var=var<<1
my_list=[1,2,3,4]
print(my_list[-3:-2])

vals=[0,1,2]
vals.insert(0,1)
del vals[1]
print(vals)

my_list=[i for i in range(-1,2)]
print(my_list)
    


def message():
     print("Enter a value: ")

message()
a=int(input())
print(a)
def introduction(first_name, last_name):
     print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

def introduction(first_name, last_name):
     print("Hello, my name is", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")
def hi(name):
      print("Hi,", name)

hi("Greg")













    

