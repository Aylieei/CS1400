from operator import and_

print ("Hello, World!")
print ('c')
print ('자바랑 다르게')
print ("double quotes를 넣던 single quotes를 넣던 상관없이 다 string임")

print (type("이건 타입 알려주는거임 앞에 type쓰면"))
print (type('c'))
print (type(7))

print (type("안녕"))
print (type('전부'))
print (type("""str이지롱"""))
print (type('''심지어 quotes 3개로 감싸면
내려쓰기해도 적용됨 ㄷㄷ'''))

print ('''"문자열 3개로" 감싸면 "중간에 quotes 넣어도 상관없음!" ''')
#참고로 python shell 쓰는법은 '>>> type(7)' 이런식으로 쓰면 되는데
#이건 지금 shell이 아니라 못 씀 (shell은 왼쪽아래 파이썬모양 누르면 나옴 = console)
#아무튼 저렇게 shell을 쓰면 run해야 결과가 나오는게 아니라
#바로바로 결과가 나와서 좋음

print ('hello', 7, 'a')
#자바같은 경우엔 전부 문자열과 '+' 로 처리해줬어야 햇지만,
# 파이썬은 콤마자체가 구분자임.타입이 섞여있어도 상관없음

print (47000)
print (47,000)
# >>> 두번째처럼 쓰면 콤마가 있기때문에 이렇게생각함
# 콤마: 아, 47이랑 000이라는 구분된 두개의 숫자구나?
# 근데 어차피 000은 0이잖아? 그냥 0으로 써야겠다

System.out.println("ffff");
print('ffff')
print("ffff")