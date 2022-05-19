Dic = {}

while True:
        key = int(input("정수 key값을 입력해주세요 : "))
        value = input("문자열 value값을 입력해주세요 : ")
if(key == 0 or value == "종료"):
        print("그만")
        print(Dic)
        break
else:
        Dic[key]=value


print(list(Dic.keys()))
print(list(Dic.values()))
print(list(Dic.items()))
