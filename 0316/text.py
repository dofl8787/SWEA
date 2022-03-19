#순회
#DFS를 배울 때, stack에 넣었다가 pop 처리를 했었음 (너비우선도 마찬가지)
# 중간에 데이터를 넣었다가 처리를 해야하는게 하나의 방법이었듯
# 순회 역시 루트에서 처리를 함
#
# =============================
# 전위 순회 (prorder)
# Tree를 처리한다.
# 1. root 처리
# 2. root를 기준으로 왼쪽 서브 트리를 처리한다.
# 3. 오른쪽 서브 트리를 처리한다.

def preorder(root):
    # 1. root를 처리한다
    print(root)
    # 2. 왼쪽 서브 트리를 처리한다 : 프리오더에 왼쪽 서브트리
    # == preorder(왼쪽 서브 트리) == preorder(g[root][0])
    # 종료 조건 : 서브트리가 없을 때  == 서브트리가 있으면 처리한다
    # if len(G[root]) >= 1:
    if len(G[root]) >= 1:
        preorder(G[root][0])

    # 3. preorder (오른쪽 서브 트리) == preorder(g[root][1]
    # 왼쪽이 없으면 오른쪽이 있을 수 없으니까, if len(G[root]) >=2:
    if len(G[root]) >= 2:
        preorder(G[root][1])


# ======================================

def preorder2(root):
    #1
    print(root)
    #2
    if T[root][0]:
        preorder2(T[root][0])
    #3
    if T[root][1]:
        preorder2(T[root][1])

def preorder3(root):
    if root:
        print(root)
        preorder3(T[root][0])
        preorder3(T[root][1])

# 트리를 그래프로 만들어보기
intS = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'

lst = list(map(int, intS.split()))

N = 13 #점의 갯수
G = [[] for _ in range(N+1)]
T = [[0]*2 for _ in range(N+1)]
leftC = [0] * (N+1)
rightC = [0] * (N+1)
#점의 구조
for i in range(0, len(lst), 2):
    P = lst[i]
    C = lst[i+1]

    G[P].append(C)

print(G)
print(T)
preorder(1)