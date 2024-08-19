# 뒤에 숨은 말은 못잡게
# def is_obstructed(a, b, b_list):
#     a_row, a_col = parse_position(a)
#     b_row, b_col = parse_position(b)

#     if abs(a_row - b_row) == abs(a_col - b_col):
#         delta_row = 1 if b_row > a_row else -1
#         delta_col = 1 if b_col > a_col else -1

#         current_row = a_row + delta_row
#         current_col = a_col + delta_col

#         while (current_row, current_col) != (b_row, b_col):
#             if (current_row, current_col) in b_list:
#                 return True
#             current_row += delta_row
#             current_col += delta_col

#     return False

# 말의 좌표

def parse_position(pos):
    if len(pos) != 2:
        return False
    try:
        col = int(pos[0])
        row = int(pos[1])
    except ValueError:
        return False

    if not (1 <= col <= 8) or not (1 <= row <= 8):
        return False

    return (row, col)


# 유효성 확인(반복)
def get_position(prompt):
    while True:
        pos = input(prompt)
        if parse_position(pos):
            return parse_position(pos)
        else:
            print("유효하지 않은 값입니다.")


# 잡을 수 있는 위치 확인
def can_bishop_capture(a, b_list):
    a_row, a_col = parse_position(a)
    capture_positions = []

    for b in b_list:
        # if not is_obstructed(a, b, b_list):
        # capture_positions.append(b)
        b_row, b_col = parse_position(b)

        if abs(a_row - b_row) == abs(a_col - b_col):
            capture_positions.append(b)

    return capture_positions


def get_b_count():
    while True:
        try:
            b_count = int(input("B말의 갯수를 입력해주세요: "))
            if b_count >= 16:
                print("유효하지 않은 값입니다.")
            else:
                return b_count
        except ValueError:
            print("유효하지 않은 값입니다.")


a = get_position("A의 위치를 입력해주세요: ")
b_list = []
for i in range(get_b_count()):
    b_position = get_position("B의 위치를 입력해주세요 : ".format(i + 1))
    b_list.append(b_position)

capturable_positions = can_bishop_capture(a, b_list)

print("잡을 수 있는 B말의 좌표:", capturable_positions)