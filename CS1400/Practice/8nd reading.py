# How to make function? (like . instance method)
def function_name(param1,param2):
    for i in range(4):
        print("param1 is: ",param1)
        print("param2 is: ",param2)
print(function_name(1,2))

# Docstring (aka JavaDoc: /** ... */)
# 자바와 다르게 함수나 클래스 본문 첫 줄에 써야함
def welcome_bot():
    "This is a function for greeting"
    print("Hello! How can I help you?")

def add(a,b):
    """
    :param a:
    :param b:
    :return: do
    """

# Special treatment
# 단순한 주석(#)과 달리, 파이썬은 이 문자열을 기억해둠
# __doc__ attribute: 이 내용을 함수의 __doc__이라는 보관함에 저장해둠
# help() : 터미널에서 help(함수명)을 치면, 이 docstring을 읽어서 보여줌

def convert_celsius_to_fahrenheit(celsius):
    result = (celsius * 9/5) + 32
    print (result)

# 값을 반환하는 함수 (fruitful functions - 결실있는 함수)
# return values
print(abs(5))
# abs는 절댓값(absolute value)을 구해주는 python 내장 함수임
print(pow(5,2))
# 거듭제곱, 즉 5의 2제곱 = 25.0 (**과 비슷함)
print(max(4,1,17,2,12))
# 가장 높은 숫자를 골라줌