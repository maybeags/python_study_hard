# chapter09_class 우클릭 -> new -> python package -> constructor
# constructor 우클릭 -> new -> python file -> main

'''
1. 생성자(Constructor)
'''
from statistics import stdev

# 클래스 정의
# class Candy:
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def display_info(self):
#         print(f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.")

# 객체 생성
# satang = Candy()
# satang.set_info("구형", "갈색")
# satang.display_info()
'''
    satang이라는 인스턴스는 생성된 '이후'에 set_info() 메서드를 호출하여 "구형" 모양의,
    "갈색"이라는 속성(attribute)을 갖게 됩니다.
    
    satang 인스턴스의 생성 과정
        1. 값이 없는(속성에 값이 대입되어있지 않은) 인스턴스를 생성
        2. 값을 저장할 수 있는 메서드 호출
        
    그렇다면 처음부터 값이 있는 인스턴스를 생성하면 코드라인이 줄어들지 않을까.
        이에 대한 해답이 생성자라는 개념이고,
        C / Java의 경우의 생성자는 클래스명과 동일한데, 또 python만 이상한 방식으로 만듭니다
        -> __init__() 라는 메서드
        
    __init__()메서드(생성자)는 인스턴스가 생성될 때 '자동으로 호출'되기 때문에 인스턴스 변수의
    '초기화' 용도로 사용, 즉 값이 있는 인스턴스를 생성할 수 있다는 의미입니다.
    '객체 생성과 동시에' 생성자가 호출됨 -> 초기값을 작성할 때 사용한다는 의미
    
    형식 :

class 클래스명:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
'''
# class Candy2():
#
#     #생성자 정의
#     def __init__(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def display_info(self):
#         print(f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.")
#
# satang2 = Candy2("정육면체", "흰색")  # 이 부분이 달라졌죠.
# satang2.display_info()

'''
이상에서 주목해야 할 점은 satang 인스턴스와 satang2 인스턴스의 생성 방식의 차이입니다.

2. 소멸자(Destructor)
    인스턴스가 생성될 때 자동으로 생성되는 생성자와 마찬가지로 인스턴스가 소멸될 때 호출되는 메서드
    이를 소멸자라고 하며, 소멸자를 정의하는 메서드는 __del__()
'''
# class Sample:
#
#     # 생성자 정의
#     def __init__(self):
#         print(f"인스턴스가 생성되었습니다.")    # 생성자 생성할 때 속성에 값만 대입하는게 아니라 출력문을 삽입할 수도 있음.
#
#     def __del__(self):
#         print(f"인스턴스가 소멸되었습니다.")

# 객체 생성
# sample = Sample()

# del sample      # del 객체명으로 소멸자를 "원하는 시기"에 호출할 수 있음 -> 예를 들어 일단 객체 소멸 시킴

# 여기 부분에 추가적인 로직을 작성하여 더 프로그램이 진행된 후에 프로그램 전체 종료가 이루어질 수 있음.
#
# print("프로그램이 종료되었습니다.")
'''
기본 예제

생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램을 작성하시오.

지시 사항
1. 클래스 USB를 정의할 것
2. 생성자를 정의하여 매개변수로 capacity를 받을 것
3. get_info() 메서드를 정의할 것

main 단계 코드
usb = USB(64)
usb.get_info()

실행 예
64GB USB 
'''
# 1번 지시 사항
# class USB:
#     # 2번 지시 사항
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     # 3번 지시 사항
#     def get_info(self):
#         print(f"{self.capacity}GB USB")
#
# # 객체 생성 및 get_info() 메서드 호출
# usb = USB(64)
# usb.get_info()

'''
생성자와 소멸자를 이용하여 서비스 안내 메시지를 출력하는 프로그램을 작성하시오.

class Service를 정의하고, 생성자를 통해 매개변수를 service로 받고, print() 메서드를 생성자와 소멸자 내에 작성하시오.

main 단계에서의 작성
s = Service("길 안내")
del s

실행 예
길 안내 Service가 시작되었습니다.
길 안내 Service가 종료되었습니다.
'''
# class Service:
#     def __init__(self, service):
#         self.service = service
#         print(f"{self.service} Service가 시작되었습니다.")
#
#     def __del__(self):
#         print(f"{self.service} Service가 종료되었습니다.")
#
#
#
#
# s = Service("길 안내")
# # del s
# print("프로그램이 종료되는 시점")
# del s


'''
응용 예제

1. 다음 지시 사항을 읽고 이름을 저장하는 Person 클래스를 생성하시오.

지시 사항

1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하시오
man = Person("james")
woman = Person("emily")
2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오
james is born.
emily is born.

3. 다음과 같은 방법으로 man 인스턴스를 삭제하시오.
del man

4. 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
james is dead.

'''
# class Person:
#
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} is born.")
#
#
#     def __del__(self):
#         print(f"{self.name} is dead.")
#
# man = Person("james")
# woman = Person("emily")
#
# del man
#
# print("프로그램이 종료되었습니다")

'''
예제 1.
    학생들의 성적을 관리하는 Student 클래스를 작성하시오. 이 클래스는
    학생의 이름, 학번, 성적을 인스턴스 변수로 갖습니다.
    
    지시 사항
        1) Student 클래스를 정의하고 생성자를 통해 name, student_id, grade을 초기화 하시오.
        2) 학생의 프로필을 출력하는 인스턴스 메서드 print_profile()를 작성하시오.(call1()타입으로 : 매개변수x 리턴x)
        3) 학생의 성적을 변경할 수 있는 인스턴스 메서드 set_grade()를 작성하시오 
            -> '이부분이 고민해볼만한 요소입니다 // set_info() 메서드를 검색해보세요 ctrl + shift + f 눌러서
        4) 세 명의 학생 인스턴스를 생성하고, 각 학생의 정보를 출력한 다음,
            성적을 변경하고 다시 출력하시오.
            
    
    student1 = Student("김철수", 20250001, "A")
    student2 = Student("이영희", 20250002, "B")
    student3 = Student("박민지", 20250003, "C")
    
    실행 예
    
    학생 이름 : 김철수
    학번 : 20250001
    성적 : A
    
    student2 / student3도 출력하시오.
    
    이후 student1 성적을 A+ / student2는 A / student3은 B+로 성적을 변경하고
    
    다시 print_profile을 적용하여 출력하시오.

'''
# 클래스 정의
# class Student:
#     # 생성자
#     def __init__(self, name, student_id, grade):
#         self.name = name
#         self.student_id = student_id
#         self.grade = grade
#     # 객체의 인스턴스 변수 값을 출력해주는 메서드
#     def print_profile(self):                    # 잠재적인 문제점 : 모든 속성을 전부 확인해야 한다는 점
#         print(f"학생 이름 : {self.name}")        # 콘솔에 찍히는 call1() -> 수학적인 연산이 불가능하다는 점
#         print(f"학번 : {self.student_id}")
#         print(f"학점 : {self.grade}")
#
#     # 이상의 코드는 console에 찍히기만 할 뿐 연산이 불가능하기 때문에 getter는 call1() 유형으로 작성하기 보다는
#     # call3() 매개변수x / 리턴o 형태로 작성합니다
#     def get_grade(self):
#         return self.grade
#
#     # grade만 바꾸게 될 메서드 -> set_info() : Book 클래스의 set_info() 메서드를 참조하시면 됩니다.
#     # setter 정의
#     def set_grade(self, grade):
#         if grade not in ["A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"]:
#             print(f"{grade}는 불가능한 점수 입력입니다.")
#             return                              # 조건문에 return 걸고 아무것도 쓰지 않으면 그대로 메서드 종료
#         self.grade = grade      # Book클래스에서 set_info(self, title, author):
#
# # 객체 생성
# # student1 = Student("김철수", 20250001, "A")
# # # 인스턴스 메서드를 호출
# # student1.print_profile()
# #
# # # 속성값을 직접 참조해서 바꾸는 방법
# # student1.grade = "A+"
# #
# # student1.print_profile()
# # student1.grade = "말도안되는 값을 넣더라도 일단 가능"          # 직접 입력했기 때문에
# # print(student1.get_grade())                                 # 결과값 : 말도안되는 값을 넣더라도 일단 가능 ->로 나왔습니다.
# # student1.set_grade("A+")
# # student1.print_profile()
# #
# # student1.set_grade("안되는거입력")
# # student1.print_profile()
# # 이상을 이유로 인스턴스 변수에 값을 대입할 때 제약을 걸기 위해 method를 경유하여 값을 대입하도록
# # 권장함. -> setter(call2()유형) / getter(call3()유형)라는 개념 -> 클래스로 돌아가서 해당 메서드들 추가하겠습니다.
#
#
# # 지시사항에 따른 코드라인만 작성하시오.
#
# # 지시사항4)
# # 객체 생성
# student1 = Student("김철수", 20250001, "A")
# student2 = Student("이영희", 20250002, "B")
# student3 = Student("박민지", 20250003, "C")
#
# # 인스턴스 메서드 호출
# student1.print_profile()
# student2.print_profile()
# student3.print_profile()
#
# # setter 이용하여 성적에 해당하는 속성값 변환
# student1.set_grade("A+")
# student2.set_grade("A")
# student3.set_grade("B+")
#
# # 바꾼 것을 확인하기 위한 인스턴스 메서드 호출
# student1.print_profile()
# student2.print_profile()
# student3.print_profile()

'''
1. Setter / Getter란?
    1) Stter : 객체의 속성 값(인스턴스 변수)을 변경하는 메서드
    2) Stter : 객체의 속성 값(인스턴스 변수)을 조회하는 메서드
    
    3) 왜 Setter / Getter를 사용하는가?
        (1) 데이터 보호 및 무결성 유지
            : 속성 값을 직접 변경하는 경우, 잘못된 값이 입력될 가능성이 높음.
            : Setter를 사용하면 특정 조건을 만족하는 값만 속성에 대입 가능
        (2) 객체의 캡슐화(Encapsulation) 실현
            : 객체의 내부 데이터를 외부에서 직접 수정하는 것을 방지
            : 대신 메서드를 통해서만 접근하도록 제한하여 보안성을 높임
        (3) 추후 유지 보수 및 확장성 용이
            : Setter / Getter를 사용하면 특정 속성에 대한 로직을 쉽게 변경 가능(if절 바꾸는거 생각하시면 됩니다)
            : 예를 들어, 특정 속성을 설정할 때 추가적인 검증이 필요하면 Setter에서 처리 가능
            
2. 이제 클래스를 정의할 때 기본적으로 Setter / Getter를 타이핑하면서 형태를 배울 예정입니다.
    1) Setter : call2() 유형 -> 매개변수 o / 리턴 x
    2) Getter : call3() 유형 -> 매개변수 x / 리턴 o 

'''
# Setter / Getter 적용된 클래스 정의 예시
class Person:
    # 생성자 정의
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # setter 정의
    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        # 0미만 및 200 초과는 입력 불가 / 0이상 200이하의 경우에는 self.age = age가 적용되도록
        if age < 0 or age > 200:
            print("불가능한 나이 입력입니다.")
            return
        self.age = age

    # getter 정의 예시
    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    # set_age / set_address를 정의하는데, set_age의 경우 0 미만 및 200 초과는 입력 불가능하게
    # 로직을 작성하시오.

    # get_age / get_address를 정의하시오.


# 객체 생성
person = Person("안근수", 38, "부산광역시 연제구")

print(f"제 이름은 {person.get_name()}입니다.")
print(f"나이는 {person.get_age()}인데, 만으로는 {person.get_age()-2}살입니다.")  # 이런 이유로 getter 사용함.
print(f"현재 {person.get_address()}에 살고 있습니다.")

# 불가능한 나이 입력
person.set_age(-30)

'''
chapter09_classes에 우클릭 new -> python package -> bank_account 패키지 생성
main 생성

'''

