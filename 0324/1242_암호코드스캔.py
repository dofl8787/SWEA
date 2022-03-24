import sys
sys.stdin = open('1242.txt')

hx_dict = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}


N,M = map(int, input().split())

arr = [input() for _ in range(N)]

arr = set(arr)

f_code = []
for i in arr:
    text = ''
    a = set(i)
    if len(a) != 1:
        text = i
        f_code.append(text)



s_code = []
for j in f_code:
    tx = ''
    for k in j:
        tx += hx_dict[k]
    s_code.append(tx.strip('0'))

for i in range(len(s_code)):
    if len(s_code[i]) % 56 != 0:
        a = 56 - (len(s_code[i]) % 56)
        s_code[i] = '0'*a + s_code[i]

print(f_code)
print(s_code)



