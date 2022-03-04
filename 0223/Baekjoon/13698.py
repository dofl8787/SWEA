
alphabet = input()

arr = [0,1,0,0,2]

for alpha in alphabet:
    if alpha == 'A':
        arr[1], arr[2] = arr[2],arr[1]
    elif alpha == 'B':
        arr[1], arr[3] = arr[3], arr[1]
    elif alpha == 'C':
        arr[1], arr[4] = arr[4], arr[1]
    elif alpha == 'D':
        arr[2], arr[3] = arr[3], arr[2]
    elif alpha == 'E':
        arr[2], arr[4] = arr[4], arr[2]
    elif alpha == 'F':
        arr[3], arr[4] = arr[4], arr[3]

s_ball = b_ball = 0
for i in range(len(arr)):
    if arr[i] == 1:
        s_ball = i
        print(s_ball)
    elif arr[i] == 2:
        b_ball = i


print(b_ball)