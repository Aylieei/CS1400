# making own fruitful functions
def square(x):
    y = x*x
    return y

toSquare = 10
result = square(toSquare)
print("The result of", toSquare, "squared is", result)

# return 문에는 y 같이 temporary variable (임시변수) 를 사용해도 OK
# 참고로 함수를 define하는것과 execute 하는것은 다르기때문에!
# line 2 --> line 6으로 넘어갔다가, 7번에서 함수가 호출되며 다시 2로 돌아가 실행됨.
# 모든 파이썬 함수는 return문이 없다면 기본적으로 none을 반환함
# return문 이후에 그 어떤 문장도 있어서는 안 됨!
# 값을 받아야한다면 꼭!!!! return문을 사용할 것!

# local variable (ex:y)
# it's only exists while the function is executing --> lifetime

# Python's scope
# local scope/global scope --> local scope는 함수 내부의 정의된 local variable을 찾음
# 만약 못찾았다? --> global scope(함수 바깥) 으로 나감으로써 전역 변수들을 찾아봄.