class Student: #파이썬에서 클래스란 객체를 찍어내는 틀과 같다.
    def __init__(self, name, grade, student_number, sex, address, phone_number, year): #init 함수는 초기화를 자동으로 시켜주는 메소드이다. 
    self.name = name
    self.grade = grade
    self.student_number = student_number
    self.sex = sex 
    self.address = address 
    self.phone_number = phone_number
    self.year = year

while True: #객체가 종료될 때까지 무한반복 
        Class_name = Student(name, grade, student_number, sex, address, phone_number, year)
        Class_name.introduce()

        class_name = input("객체 명을 입력하시오. ( 단 영문으로): ")
        if class_name == "종료": #종료가 입력된경우 if문 탈출
            break
        name == input("이름을 입력하시오. (단, 한글로): ")
        grade == int(input("학년을 입력하시오. (단, 숫자로): "))
        student_number == int(input("학번을 입려하시오. (단, 숫자로): "))
        sex == input("성별을 입력하시오. (모를 때는 모른다 라고 입력.): ")
        if sex == "모른다":
            sex == "None"
        address == input("주소를 입력하시오.(~시 까지만): ")
        phone_number == input("전화번호를 입력하시오. (모를 때는 모른다고 라고 입력.): ")
        if phone_number == "모른다":
            phone_number == "None"
        year == input("멋사 몇년차인가요?(단, 숫자로): ")

    def introduce(self):
        print("이름은 %s이다." %self.name)
        print("학년은 %s이다." %self.grade)
        print("학번은 %s이다." %self.student_number)
        print("성별은 %s이다." %self.sex)
        print("주소는 %s이다." %self.address)
        print("휴대폰 번호는 %s이다." %self.phone_number)

        if self.year == "1":
            print("멋사 1년차")
            print("우와 아기사자다!")
        else :
            print("멋사 n년차")
            print("우와 운영진이다!")

