import sys
sys.stdin = open('4839.txt')

T = int(input())

for tc in range(T):
   p, a, b = map(int, input().split())
   start = 1
   end = p

   count_a = 0
   while start <= end:
       mid = (start + end) // 2
       if mid == a:
           break
       elif mid < a:
           start = mid
           count_a += 1
       else:
           end = mid
           count_a += 1

#B
   start = 1
   end = p
   count_b = 0
   while start <= end:
       mid = (start + end) // 2
       if mid == b:
           break
       elif mid < b:
           start = mid
           count_b += 1
       else:
           end = mid
           count_b += 1


   if count_a < count_b:
       print(f'#{tc+1} A')
   elif count_a > count_b:
       print(f'#{tc+1} B')
   elif count_a == count_b:
       print(f'#{tc+1} 0')



