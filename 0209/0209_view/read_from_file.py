import sys
sys.stdin = open('input.txt')
#stdin = 키보드라고 생각하기~ // file 객체인데 프로그램이 실행이 되면 무조건 열리는 파일이 있음 *3개
#stdin, stdout, stderr : out,err는 출력 장치임~~ 표준 출력 장치
#stdin은 키보드 (오픈하지 않아도 무조건 입력되게 되어있음)
#stdout을 사용하면 출력값이 파일로 저장됨~~~~
#기본적으로 키보드 입력을 기준으로 하지만, input 파일을 여는 걸 키보드로 입력받은 것처럼 착각하게  하는 것
#나중에 서버에 제출할 때 윗줄 빼고 제출하기~~~~~~

N = int(input())
for _ in range(N):
    arr = list(map(int, input().split()))
    print(arr)