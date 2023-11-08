# 
import matplotlib.pyplot as plt

# 예제1: x,y가 같을떄
plt.plot([1,2,3,4])
# plt.show()

# 참고: 이때까지 그렸던 plot 지우기
plt.clf()

# 예제2 : x,y가 다를 떄

x = [1,2,3,4]
y = [2,4,8,16]
plt.plot(x,y)
# plt.show()

# 예제3: 제목 + 각 축의 설명
# 기본 세팅으로는 한글 깨짐. 구글링으로 풀기@@!!@!

plt.plot(x,y)
plt.title("한글은 안되나요?")


#x,y축
plt.ylabel('y label')
plt.xlabel('x label')

# plt.show()

# 파일로 저장하기, pltshow()는 무조건 주석처리하든 지워야 됌!!!!
# pltshow()되 있을 경우 빈 화면 저장
plt.savefig('filename.png')