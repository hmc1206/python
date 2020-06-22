from random import *
customer = 0 #총 고객수
for i in range(1,51): #1~50 이라는 수
  time = randrange(5,51) # 5부터 50분 까지 랜덤으로 
  if 5 <= time <=15: #5부터 15분까지 소요 되는 손님(매칭성공)
    print("[o] {0}번째 손님 {1}분 소요".format(i, time))
    customer += 1
  else : #(매칭 실패)
    print("[ ] {0}번째 손님 {1}분 소요".format(i, time))

print("매칭 성공수 : {0}분".format(customer)) #매칭 성공한 손님 수