# 1A2B
import random
from datetime import datetime
import matplotlib.pyplot as plt

def generate_answer_number(): # 產生4位答案數字的模組
    # 取得1970/1/1以來累積的秒數(str的型式)作為種子數字，並將其轉換為浮點數再轉為整數再轉回字符串格式(因int無法處理小數點)
    seed_seconds = str(int(float((datetime.now().timestamp()))))
    # 取得seed_seconds的位數，方便後續計算
    seed_seconds_len = len(seed_seconds)
    # 以seed_seconds_len取地的長度，取得不重複的四個位數
    seed_seconds_digit = random.sample(range(seed_seconds_len),4)
    # 取得位數對應seed_seconds的數字，從seed_seconds串中提取特定索引位置的str，並組成列表answer_number
    answer_number = [seed_seconds[dig] for dig in seed_seconds_digit]
    return answer_number

def check_input(guess_input): # 使用者輸入檢查模組
    try: # 先檢查錯誤的輸入，除此之外都是正確的
        # 檢查是否沒有輸入
        if not guess_input:
            return (False, "不能沒有輸入數字！")
        # 檢查長度是否為四位數字
        if len(guess_input) != 4:
            return (False, "請輸入四位數字！")
        # 檢查是否為數字
        if not guess_input.isdigit():
            return (False, "只能輸入數字！")
        return (True, "")
    except:
        return (False, "其他錯誤")
    
def compare_number(answer_number, guess_input): # 對答案計算AB數量模組
    count_A = 0 #初始值0
    count_B = 0 #初始值0
    for i in range(4):
        if guess_input[i] == answer_number[i]: # 位子數字都對，count_A+1
            count_A += 1
        elif guess_input[i] in answer_number: # 數字對，count_B+1
            count_B += 1
    return count_A, count_B

def game_1A2B(): # 遊戲主要程式模組
    answer_number = generate_answer_number()
    input_times = 0 # 計算遊戲輸入次數，初始值0
    input_times_deltas = [] # 時間差陣列
#    print (answer_number)
    print ("1A2B猜數字遊戲")
    print ("請猜一個4位數字，且數字可以重複")
    print ("或輸入EXIT退出遊戲")
    mode = "START"
    while mode == "START":
        input_start_time = datetime.now()
        guess_input = str(input ("請輸入:")) #輸入提示
        input_end_time = datetime.now()
        delta_input_time = (input_end_time - input_start_time).total_seconds()
        input_times_deltas.append(delta_input_time)
        if guess_input == "EXIT": #當使用者輸入EXIT跳轉至EXIT模式離開
            mode = "EXIT"
        is_valid, error_message = check_input(guess_input) # 輸入檢查模組的回傳值，使不符合規則的輸入時可以在else迴圈print錯誤訊息
        if is_valid == True: #當使用者輸入非EXIT時使用check_input(guess_input)進行檢查，當True時進行後續計算count_A, count_B
            count_A, count_B = compare_number(answer_number, list(guess_input))
            print (f"{count_A}A{count_B}B")
            input_times +=1 # 輸入次數+1
            if count_A == 4: # 當4A的情況發生
                print(f"恭喜你猜對了！總共猜了 {input_times} 次。") # 恭喜猜對的提示，並顯示輸入次數
                print("以下是你每次輸入的時間差折線圖")
                plt.plot(range(1, len(input_times_deltas) + 1), input_times_deltas, marker='o')
                plt.title("Time difference for each input")
                plt.xlabel('Number of guesses')
                plt.ylabel('Time difference (seconds)')
                plt.xticks(range(1, len(input_times_deltas) + 1))
                plt.grid(True)
                plt.show()
                mode = "EXIT" # 離開程式
        else:
            print(error_message)  #輸出錯誤資訊
    while mode == "EXIT":
        print ("期待再次相見，再次按下Enter鍵結束程式")
        break

if __name__ == "__main__": # 主程式
    game_1A2B()
    input() # 避免程式結束後直接關閉視窗，Colab環境可忽略此行