# 파이썬은 파일을 실행할 때 __name__ 이라는 특별한 변수를 생성함.
# 파일을 직접 "run" 할 때: 파이썬이 이 변수에 "__main__"이라는 값을 넣어줌.
# 다른 파일에서 import 할 때: 파이썬이 이 변수에 "파일 이름"을 넣어줌
# if __name__ == "__main__":
#    main()
# 내가 직접 이 파일을 실행할 때만 동작해라!
# if 다른파일을 넣으면 저 if __name__자리에 my_math같은 다른 이름이 되고,
# 그럼 자동으로 들어가는 __main__과 일치하지 않으니 동작되지않음!

import test
def distance(x1, y1, x2, y2):
    return 0.0
test.testEqual(distance(1, 2, 1, 2), 0)
# 다른 함수 이름을 호출하여 테스트

