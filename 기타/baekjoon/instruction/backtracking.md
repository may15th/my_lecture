DP는 PROBLEM들을 SUB으로 나누면서 
MEMOIZATION으로 중복된 SUB들 줄여나가는 식

BT는 DECISIONSPACE을 만들고 하나씩 살펴가는 것.
어떠한 후보들은 더이상 진행할 필요 없다 결론이나면 더이상
진행할 필요가 없는 것,.
하나의 선택권이 다시 뒤로 가면서 백트래킹 하는 것 decision 들은 더이상 가능성 없기 때문에 탐색 가능한 것들만 가져가면서 모두 서칭을 한다는 개념.

recursion과 memoization이 코드에서 어떻게 진행되는지 이해 해야 한다.

def BackTracking(index. letter)

num = input[index]
chars = hashmap[num]
for (c:chars){
  bt(index+1. letter+1)
}
output array에 add(letter)해주는 것