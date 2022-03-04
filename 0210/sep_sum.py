#구간합
#arr = [i for i in range(1,11)]
#N = len(arr)  ==> 5
#M = 3
#시작과 끝을 ㄴs, e
#for i in range(s, e+1)
#s, e+1 의 경우를 다 가져오기

#끝은 알고 있으니까 -> M
#시작 S 끝 S+M-1
# for  i in range (S, S+M)
#더하는 건 i 더하기
#내가 조사할 위치의 모든 시작 위치만 알면 됨
#모든 경우에 대해서 다 돌리려면 시작 위치만 찾아서 넣어주면 됨
# 맨 마지막 시작 값은 N-M
#모든 첫번째 구간의 시작 위치는 0번
# 두번재 위치는 1
# range(N-M)
import sys
sys.stdin = open('sep_sum.txt')

T = int(input())

for i in range(T):
    N,M = map(int, input().split())
    ai = list(map(int, input().split()))
    sum_list=[]
    for s in range(0, N-M+1):
        num_sum = 0
        max=min=0
        for k in range(s, s+M):
            num_sum += ai[k]

        sum_list.append(num_sum)
    max = min = sum_list[0]
    for m in sum_list:
        if max < m:
            max = m
        if min > m:
            min = m
    result = max - min

    print(f'#{i+1} {result}')