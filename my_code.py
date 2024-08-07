# 말 뒤에 숨어있는 경우, 유효성 검사(올바른 좌표 입력) 미흡
# 말의 좌표
def parse_position(pos):
    col = ord(pos[0])
    row = int(pos[1])
    return (row, col)
# 잡을 수 있는 위치 확인
def can_bishop_capture(a, b_list):
    a_row, a_col = parse_position(a)
    capture_positions = []

    for b in b_list:
        b_row, b_col = parse_position(b)
        
        if abs(a_row - b_row) == abs(a_col - b_col):
            capture_positions.append(b)
    
    return capture_positions

a = input("A의 위치를 입력해주세요: ")
b_count = int(input("B말의 갯수를 입력해주세요: "))

b_list = []
for i in range(b_count):
    b_position = input("B의 위치를 입력해주세요 : ".format(i + 1))
    b_list.append(b_position)

capturable_positions = can_bishop_capture(a, b_list)

print("잡은 B말의 좌표:", capturable_positions)