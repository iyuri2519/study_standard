import random as rd

# index() 함수를 시행합니다.
# 시행할 수 없다면 -1을 반환합니다.
def no_error_find(arr:list, value:str) -> int:
    if value not in arr:
        return -1
    return arr.index(value)

# 플레이어 기준으로 승부를 판단합니다.
# 플레이어 승 : 1, 상대 승 : -1, 무승부 : 0
def decide_win(player_idx:int, other_idx:int) -> int:
    if player_idx == other_idx:
        return 0
    elif player_idx == (other_idx+1) % 3:
        return 1
    return -1


SiRoPa = ["가위", "바위", "보"]
print("먼저 내세요. 단판 승부입니다.")
print("무승부는 승부에 포함 안합니다.")

while True:
    ans = input()
    ans_idx = no_error_find(SiRoPa, ans)
    if ans_idx == -1:
        print("다시 내주세요!")
        continue

    com_idx = rd.randint(0,2)     # SiRoPa의 index를 랜덤으로 고름
    win_player = decide_win(ans_idx, com_idx)
    print(f"플레이어 : {ans}, 컴퓨터 : {SiRoPa[com_idx]}")

    if win_player == 0:
        print("무승부! 다시!")
        continue
    elif win_player == 1:
        print("제가 졌어요...")
    else:
        print("컴퓨터 승리!")
    break