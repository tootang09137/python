Limminji={'name':'Limminji','age':'21','birthday':'020506','sex':'여자','phone':'01066366287'}
kimjongah={'name':"kimjongah",'age':'21','birthday':'020205','sex':'여자','phone':'01099718402'}
kimminji={'name':"kimminji",'age':'21','birthday':'020204','sex':'여자','phone':'01040970963'}

name=[1, 2, 3]
age=[1, 2, 3]
birthday=[1, 2, 3]
sex=[1, 2, 3]
phone=[1, 2, 3]


name[0:3]=[Limminji['name'],kimjongah['name'],kimminji['name']]
age[0:3]=[Limminji['age'], kimjongah['age'], kimminji['age']]
birthday[0:3]=[Limminji['birthday'], kimjongah['birthday'],kimminji['birthday']]
sex[0:3]=[ Limminji['sex'], kimjongah['sex'],kimminji['sex']]
phone[0:3]=[Limminji['phone'], kimjongah['phone'], kimminji['phone']]

print("이름 리스트는 %s" %name) 
print("나이 리스트는 %s" %age )
print("생일 리스트는 %s" %birthday)
print("성별 리스트는 %s" %sex)
print("전화번호 리스트는 %s" %phone)