# 가위바위보 게임
def play(s, e):
    if s == e:
        return s
    else:
        mid = (s + e) // 2
        lwin = play(s, mid)
        rwin = play(mid + 1, e)

        return who_win(lwin, rwin)


def who_win(left, right):
    lwin, rwin = rsp[left-1], rsp[right-1]

    if lwin == rwin:
        return left
    elif lwin == 1:
        if rwin == 2:
            return right
        elif rwin == 3:
            return left
    elif lwin == 2:
        if rwin == 1:
            return left
        elif rwin == 3:
            return right
    elif lwin == 3:
        if rwin == 1:
            return right
        elif rwin == 2:
            return left

T = int(input())
for tc in range(T):
    N = int(input())
    rsp = list(map(int, input().split()))

    print(f'#{tc+1} {play(1,N)}')