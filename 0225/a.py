# from time import time
# start = time()
# arr = []
# for i in range(1000000):
#     arr.append(i)
# while arr:
#     arr.pop()
# print(time()-start)
#
# #선형큐
# Q = [0]* 1000000
# front = rear = -1

print(arr)
ud = [-1, 1, 0, 0]
rl = [0, 0, 1, -1]


i, j = 6, 9
for d in range(4):
    cnt = 0
    while cnt < 2:
        if arr[i + ud[d]][j + rl[d]] == 'H':
            arr[arr[i + ud[d]][j + rl[d]]] == 'X'
        cnt += 1