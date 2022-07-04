fruits = ["apple", "banana", "cherry", "orange"]
print(fruits[2])
#เปลี่ยนค่าในlist
fruits[1]="blackcurrant"
print(fruits)
fruits[1:3]=["banana", "kiwi", "melon"]
print(fruits)
fruits[1:3]=["blackcurrant"]
print(fruits)
#เพิ่มคำในlist
fruits.append("kiwi")
print(fruits)
fruits.insert(1, "banana")
print(fruits)
tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
print(fruits)
#ลบค่าในดิส
fruits.remove("pineapple")
print(fruits)
fruits.pop(3)
print(fruits)
#del fruits ลบตัวแปรlistออกจากระบบ
#เรียงค่าในlist
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#รวมlist
vege=["carrot", "potato", "cucumber"]
all = fruits+vege
print(all)
#นายธีรเมธ ไพรินอุดมโชค ม.6/11 เลขที่16