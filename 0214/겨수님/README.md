## List 02



#### delta 

- 기준점 (행, 열)과 인접한 상하좌우의 좌표와의 차이값을 활용
- 인접한 요소의 값을 읽어와서 동일한 작업을 반복적으로 수행할 때 적용
  - 가독성, 수정, 디버깅에 용이

<img src="README.assets/image-20220214134454459.png" alt="image-20220214134454459" style="margin-left: 0; zoom:50%;" />



```python
N = 9
arr = [[' '] * N for _ in range(N)]
r = c = 4
arr[r][c] = '#'
arr[r - 1][c + 0] = '*' #상
arr[r + 1][c + 0] = '*' #하
arr[r + 0][c - 1] = '*' #좌
arr[r + 0][c + 1] = '*' #우

for lst in arr:
    print(*lst)
print('===================')
#========================
arr = [[' '] * N for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
r = c = 4
arr[r][c] = '#'
for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    arr[nr][nc] = '*'

for lst in arr:
    print(*lst)
```



#### bit 연산자

- 알고리즘 문제 해결에 비트연산자를 종종 활용한다.

  - 비트연산자는 다른 연산자들에 비해 실행 사이클이 짧다. (파이썬은 글쎄?)
  - 수식을 간결하게 표현할 수 있다.

- 대표적인 사용예

  ```python
  print(10 & 7)
  print(10 | 7)
  # 홀짝 판별
  n = 5
  if n & 1:  # 홀수, /, % 연산자는 가장 느린 연산자
      print('홀수')
  else:
      print('짝수')
  
  # shift 연산자
  print(10 << 1)
  print(10 << 2)
  print(10 >> 1)
  print(5 >> 1)
  ```

  

- 홀짝 판별

<img src="README.assets/image-20220214170105241.png" alt="image-20220214170105241" style="zoom:50%;" />

- 2로  곱하거나 나누기

  <img src="README.assets/image-20220214171245523.png" alt="image-20220214171245523" style="zoom:50%;" />

----------

부분집합 --> 2진수

![image-20220214172524671](README.assets/image-20220214172524671.png)



-------

- 바이너리 카운팅

<img src="README.assets/image-20220214174137036.png" alt="image-20220214174137036" style="zoom:50%;" />

```python
arr = [1, 2, 3, 4]
N = len(arr)  # 4

# 모든 부분집합에 대응하는 정수값을 생성
for subset in range(1 << N):
    # subset에 저장된 하위 4bit(4자리 2진수) 값을 확인
    print(subset, '==>', end=' ')
    for i in range(N):
        if subset & (1 << i):
            print(arr[i], end=' ')
    print()
```

















