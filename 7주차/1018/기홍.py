import sys

input = sys.stdin.readline

a, b = map(int, input().split())

board = []

for i in range(a):
    board.append(list(map(str, input().strip())))


# def check_chess(_list, x_start, y_start):
#     check = _list[y_start][x_start]
#     count = 0
#     for x in range(x_start, x_start + 8):
#         for y in range(y_start, y_start + 8):
#             if (x - x_start) % 2 == 0: # x와 2씩 뛰어진 줄일 때
#                 if (y - y_start) % 2 == 0:
#                     if check != _list[y][x]:
#                         count += 1
#                 else:
#                     if check == _list[y][x]:
#                         count += 1
#             else: # x와 엇갈려서 2씩 뛰어진 줄일 때
#                 if (y - y_start) % 2 == 0:
#                     if check == _list[y][x]:
#                         count += 1
#                 else:
#                     if check != _list[y][x]:
#                         count += 1
#     return count

_list = ["B", "W", "B", "W", "B", "W", "B", "W"]
_list2 = ["W", "B", "W", "B", "W", "B", "W", "B"]

# 처음이 B로 시작하는 체스판
chess_1 = [_list if i % 2 == 0 else _list2 for i in range(8)]
# 처음이 W로 시작하는 체스판
chess_2 = [_list2 if i % 2 == 0 else _list for i in range(8)]


def check_chess(board, x_start, y_start):
    check_1 = 0
    check_2 = 0
    for x in range(8):
        for y in range(8):
            point = board[y + y_start][x + x_start]
            if chess_1[y][x] != point:
                check_1 += 1
            if chess_2[y][x] != point:
                check_2 += 1
    return min(
        check_1, check_2
    )  # 2개의 체스판과 비교해서 가장 적게 수정할 수 있는 걸 찾기


m_value = 999999
for x in range(b):
    for y in range(a):
        if x + 8 <= b and y + 8 <= a:
            count = check_chess(board, x, y)
            if m_value > count:
                m_value = count

print(m_value)
