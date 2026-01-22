n = input("Please enter your name: ")
print('Hello,', n)
#function (input)
# ONLY return str type.
# if I want to get value as int or float,
# type(variable) <-- type casting
str_second = input("Please enter number of seconds you wish to convert: ")
total_secs = int(str_second)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("hours: ",hours, ", min:", minutes,", sec:", secs_finally_remaining)
# // = int/int (그러나 negative의 경우 항상 낮은수로!
# / = double/double
#ex. 7//2 = 3, -7//2 = -4 (내려버림 실제결과는 -3.5, 더 낮은숫자로 항상 왼쪽으로!)

for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi", name, "Please come to my party on Saturday!")
# for loops --> for ___ in [...]

for x in range(3)
print('A', end="")
    for y in range(2, end="")
        print('B', end="")
    print('C', end="")
print('D')
# ANSWER: ABBCABBCABBCD
# x를 0,1,2 (int)형식임. string이 아님!
# x loop를 3번돌아라--> 중간에 y loop(2)가 있으니
# x가 한번 돌떄마다 y는 2번씩 돌게됨
# 따라서 x loop의 블럭 끝은 print(C) 까지임
# print D는 루프 바깥이니 마지막에만 한 번 나옴
# end="" <-- 출력 후 줄바꿈 없음.
# end=""\n <-- 출력 후 줄바꿈
# end=" " <-- 출력 후 공백 하나
# println 이나 print가 없고, 대신 전부 print로 출력,
# 뒤에 end= ... 를 붙여서 줄바꿈 여부를 조절함.

for child in range(1,9,3) :
    print( "kid", child, "gets candy" )
#(1,9,3) >>> 1부터 9까지 3씩 더하면서 루프해.
# same as (int i = 1; i <= 9; i+3)
# >> kid 1,4,7 gets candy

#참고로 range(10)이 아니라 그냥 10 넣으면 숫자 10하나만 있기땜누에 반복문 X!
# for i in range(10) : 1,2,3...9
# for i in 10 : 10. 그래서 뭐?