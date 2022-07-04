tuplefruits = ("apple" , "banana" , "cherry")#Tuple
listfruits = ["apple" , "banana" , "cherry"]#List
print("original tupie:",tuplefruits)
print("original lists:",listfruits)
#เปลี่ยนค่าในtuple
x=list(tuplefruits)#แปลงเป็นlistแล้วเก็บในตัวแปรx
x[1]="blueberry"
tuplefruits=tuple(x)
print("เปลี่ยนค่าtuple:",tuplefruits)
#เพิ่มค่าในtuple
x=list(tuplefruits)
x.append("melon")
tuplefruits=tuple(x)
print("ลบค่าtuple:",tuplefruits)
#ลบtuple
x=list(tuplefruits)
x.remove("cherry")
tuplefruits=tuple(x)
print("เพิ่มค่าtuple:",tuplefruits)
#join tuple
vege=("tomato","cucumber","onion")
fruitvege=tuplefruits+vege
print("join tuple:",fruitvege)
x = range(3,6)#จะหยุดก่อนค่าstop
for n in x:
    print("range x:",n)
y = range(3,20,2)
for m in y:
    print("range y:",m)
#นายธีรเมธ ไพรินอุดมโชค ม.6/11 เลขที่ 16