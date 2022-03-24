# arr = '0000000111100000011000000111100110000110000111100111100111111001100111'
#
# new_str = ''
#
# # for i in range(0, len(arr), 7):
# #     print(int(arr[i: i+7],2), end=' ')
#
#
# for i in range(0, len(arr), 7):
#     val = 0
#     for j in range(i, i+7):
#         # val *= 2 #자리가 2진수이니까 2자리 해주기
#         # 좀 더 다른 방식으로 표현하면 (윗줄 == 아랫줄)
#         val = val << 1
#         if arr[j] == '1':
#             val = val+ 1
#     print(val, end=' ')


dict = {
    '0010' : 3,
    '0011' : 4
}

arr = '00100011'

for i in range(0, len(arr), 4):
    new_arr= ''
    for j in range(i, i+4):
        new_arr += arr[j]

    print(dict[new_arr])
    print(new_arr)