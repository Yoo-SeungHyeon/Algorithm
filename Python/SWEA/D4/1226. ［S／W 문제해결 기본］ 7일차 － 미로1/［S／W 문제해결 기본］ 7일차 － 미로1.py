from collections import deque

direction = [(1,0), (-1,0), (0, 1), (0, -1)]

def move_to_zero(start):
    queue = deque([start])
    while queue:
        now_x, now_y = queue.popleft()
        for x, y in direction:
            nx, ny = x + now_x, y + now_y
            t = maze[nx][ny]
            if t == '0':
                queue.append((nx,ny))
                maze[nx][ny] = 1
            elif (nx, ny) == end:
                return 1
    return 0

for _ in range(10):
    tc = int(input())

    # input 받으면서 start와 end도 찾기
    # start = tuple()
    # end = tuple()
    start = (1, 1)
    end = (13, 13)
    maze = []
    for i in range(16):
        # temp = list(input())
        # if '2' in temp:
        #     j = temp.index('2')
        #     start = (i, j)
        # if '3' in temp:
        #     k = temp.index('3')
        #     end = (i, k)
        # maze.append(temp)
        maze.append(list(input()))
    result = move_to_zero(start)

    print(f'#{tc} {result}')