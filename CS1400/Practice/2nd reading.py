message = "What's up Doc?"
n = 17
pi = 3.14

print(message)
print(n)
print(pi)

print(type(message))
print(type(n))
print(type(pi))

#만약 variable과 sentence를 같이쓰고싶다면?
#1. f string 이용하기 (double quotes앞에 f 넣고, 대괄호로 variable 묶어주기)
print(f"{n} is the perfect number")
#2. comma 이용하기
print(n, 'is the perfect number')
print("this number is,", message,'!')
print("this number is,", message + '!')
#comma를 쓰면 MUST!!! 뒤에 space(공백)이 하나 들어간다!
#+를 쓰면 문자열 덧셈으로 하는거라 바로 붙여지기 때문(java)
#python과 java의 데이터 저장구조(heap/stack)은 비슷하나
#python은 primitive type이 없음. 전부 객체임

#파이썬에선 snack_case를 권장함.
#java: racingCar
#Python: racing_car
#참고로 자바의 camel case처럼 무조건적으로 첫글자가 lower case여야한다는 규칙은X
#ex) A_is_the_best_grade

#파이썬의 키워드들을 변수이름으로 설정하면 안됨.
#ex. java의 return, static 같은것들

#python은 interpreter, java는 compiler 방식을 사용함.
#java: 컴파일러가 먼저 코드 전체를 읽고, 그다음 실행
#따라서 아래에 있는 함수를 위에서 먼저 호출 가능함
#python: 실행하면서 읽어내려감 (위->아래)
#정의되지 않은 함수를 부를 수 없음, 무조건 먼저 def 해야함
