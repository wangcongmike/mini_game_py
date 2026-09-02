import tkinter as tk
import random
from rock_paper_scissors import Rock_Paper_Scissors
 
# 创建主窗口
root = tk.Tk()  #调用窗口主函数
root.title("✊石头剪刀布✊")  #设置标题
root.geometry("400x300")    #设置窗口大小
root.resizable(False,False) #禁止调窗口大小

#提示标签
prompt_label = tk.Label(root,text="请选择你的出拳:",font=("Arial",16))
prompt_label.pack(pady=20)

#结果显示标签,初始为空
result_label = tk.Label(root,text="",font=("Arial",18),fg="blue")
result_label.pack(pady=20)

#电脑出拳显示
computer_label = tk.Label(root,text="",font=("Arial",14))
computer_label.pack(pady=10)

#核心游戏函数(点击按钮时调用)
def play_game(player_choice):
    #1.电脑随机出拳
    computer_choice = random.choice(["石头","剪刀","布"])
    
    #2.调用函数判定胜负结果
    result = Rock_Paper_Scissors(player_choice,computer_choice)
    
    #3.更新界面上的标签
    computer_label.config(text=f"电脑出了：{computer_choice}")
    result_label.config(text=result)
    
#---创建三个按钮---
#用 lambda 将玩家的选择传给 play_game函数
btn_rock = tk.Button(root,text="✊ 石头",width=10,height=2,command=lambda:play_game("石头"))
btn_rock.pack(side=tk.LEFT,padx=20,pady=20)
btn_scissors = tk.Button(root,text="✌️ 剪刀",width=10,height=2,command=lambda:play_game("剪刀"))
btn_scissors.pack(side=tk.LEFT,padx=20,pady=20)
btn_paper = tk.Button(root,text="✋ 布",width=10,height=2,command=lambda:play_game("布"))
btn_paper.pack(side=tk.LEFT,padx=20,pady=20)

#进入时间循环(让窗口保持响应)
root.mainloop()