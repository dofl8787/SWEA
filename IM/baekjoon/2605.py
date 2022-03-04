N = int(input())
num_lst = list(map(int,input().split()))
s_lst = []
for i in range(N):
    s_lst.insert(num_lst[i],i+1)
s_lst.reverse()
print(*s_lst)