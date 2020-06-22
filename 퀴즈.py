from random import *
num = range(1,21) #1부터 20까지 숫자를 생성
num = list(num)

print(num)
shuffle(num)
print(num)


snum = sample(num, 4)# 4명 중에서 1명은 치킨,3명은 커피

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(snum[0]))
print("커피 당첨자 : {0}".format(snum[1:]))
print(" -- 축하합니다 -- ")