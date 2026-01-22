print(1+1)
print(len("hello"))
#len() 은 parentheses 안에 있는 문자열의 개수를 출력함.

print(2 ** 3 ** 2)     # the right-most ** operator gets done first!
print((2 ** 3) ** 2)   # use parentheses to force the order you want!
# >>> 오른쪽부터 계산하니까 3의 2승 = 9, 2의 9승 = 152 로 계산됨.

print(2**2**3*3)
#>>> 2**3부터 계산, 따라서 2**8*3. *3을 맨 마지막에 계산함