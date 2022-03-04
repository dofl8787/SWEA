#기본적으로 문제에서 입력은 키보드로 입력하는 걸 가정하고 있음
#ret = input() #엔터키 입력까지 문자열을 반환

#입력의 자료(data)들은 보통 정수 or 문자열 (이 두가지가 제일 많음) 실수는 아직까지 많지 않을 것
#문제에서 들어오는 건 문자열이긴 하나, 정수로 들어올 경우 형변환
#여러 개일 경우에는 먼저 개수가 주어지고, 공백으로 구분해서 자료들이 주어짐.
# ret = input().split() #공백으로 잘라낸 문자열들의 리스트로 반환
# print(ret) #문자열 반환
#
# #정수일 경우에 정수로 형변환이 필요하다. int()
# arr = map(int, ret) #뒤엔 literable한게 들어오는 것~~~~~~~
# print(arr)  # -> map 객체 반환

# for val in arr:
#     print (val, type(val))  <- int 5개가 각각 나오지만, 우린 리스트로 사용해주장 ~~

#문자열의 리스트를 정수의 리스트로 변환해서 저장해서 사용
# arr = list(map(int, input().split())) #한 행에 여러개의 정수들이 있을 때, 이렇게 한 줄로 표현하기기
# print (arr)
#
# a, b = map(int, input().split())
# print(a,b)

# a = 1
# b = 2
# c = 3
# numbers = [a, b, c]
# print(numbers)
import sys
sys.stdin = open('1206.txt')

for tc in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))
    result = 0

    #for i in T : T를 돌 때
    for i in range(2, T-2):

    # 만약 i-2, i-1, i, i+1, i+2 중 i가 가장 클 때,
        if arr[i-2] < arr[i] and arr[i-1] < arr[i] and arr[i+1] < arr[i] and arr[i+2] < arr[i]:
            #i-2 ~ i+2 중 가장 큰 수를 찾고. arr[i]에서 빼기
            numbers = [arr[i-2],arr[i-1],arr[i+1],arr[i+2]]
            max_num = numbers[0]
            for number in numbers:
                if max_num < number:
                    max_num = number

            result += (arr[i]-max_num)
    print(f"#{tc} {result}")



    # i - 두번째로 큰 i[idx] 를 빼서
    #result에 더하기

    #print result



















