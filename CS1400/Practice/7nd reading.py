# All standard Python modules will work in activecode.
# activecode 란? 웹브라우저 상에서 코드를 직접 입력하고 즉시 실행해 볼 수 있는 연습창! ex.turtle
# module을 사용하기 전엔 항상 import 하는 것 잊지말 것!

import math
# The math module
# including pi, e, sqrt function, sin, cos, etc.

print(math.pi) # 원주율 : 3.141592...
print(math.e) # 자연상수 : 2.718281...
print(math.sqrt(2.0)) # 제곱근 : ex. sqrt(16) --> 4! (4X4 = 16)
print(math.sin(math.radians(90))) # 라디안 90의 sin값은? --> 1! sin 90도

import random
# random.random() : [0.0, 1.0) --> 0.0은 가능, 1.0은 미포함!
# random.randrange(start,stop) : [start, stop)

prob = random.random() #랜덤 숫자 만들기 단! prob는 몇번을 출력하던 처음에 얻는 랜덤값임.
print(prob) #프로그램을 다시시작하거나, 루프안에 있지않으면 무조건 같은값!~
diceThrow = random.randrange(1,7) # range안의 값으로 랜덤값 출력 int니까 return int
print(diceThrow)

result = prob*5
print(result)