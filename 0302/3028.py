
ball_game = [0,1,0,0]

order = list(input())

for od in order:
    if od == 'A':
        ball_game[1],ball_game[2] = ball_game[2],ball_game[1]
    elif od == 'B':
        ball_game[2],ball_game[3] = ball_game[3],ball_game[2]
    elif od == 'C':
        ball_game[1],ball_game[3] = ball_game[3], ball_game[1]

for ball in range(4):
    if ball_game[ball] == 1:
        print(ball)
