import customtkinter as ctk
import random
from rock_paper_scissors import Rock_Paper_Scissors

#创建计分板
wins = 0
losses = 0
draws = 0

#核心设置：外观和主题色
ctk.set_appearance_mode("dark")     #可选 "dark","system","light"
ctk.set_default_color_theme("blue") #可选 "blue","dark_blue","green"
 
# 创建主窗口
root = ctk.CTk()  #调用窗口主函数
root.title("✊石头剪刀布✌️")  #设置标题
root.geometry("400x300")    #设置窗口大小
root.resizable(False,False) #禁止调窗口大小

#提示标签
prompt_label = ctk.CTkLabel(root,text="请选择你的出拳:",font=ctk.CTkFont(size=16,weight="bold"))
prompt_label.pack(pady=10)

#结果显示标签,初始为空
result_label = ctk.CTkLabel(root,text="",font=ctk.CTkFont(size=18),text_color="blue")
result_label.pack(pady=10)

#电脑出拳显示   
computer_label = ctk.CTkLabel(root,text="",font=ctk.CTkFont(size=14))
computer_label.pack(pady=10)

#计分板UI
score_label = ctk.CTkLabel(root,text=("🏆 胜: 0    负: 0    平: 0"),font=ctk.CTkFont(size=16,weight="bold"))
score_label.pack(pady=(10,5))  #放在顶部

#核心游戏函数(点击按钮时调用)
def play_game(player_choice):
    global wins,losses,draws #申明要修改全局变量
    #1.电脑随机出拳
    computer_choice = random.choice(["石头","剪刀","布"])
    
    #2.调用函数判定胜负结果
    result = Rock_Paper_Scissors(player_choice,computer_choice)
    
    #3.更新界面上的标签
    computer_label.configure(text=f"电脑出了：{computer_choice}")
    
    #4.根据结果给输赢配个色
    if result == "这局你赢了！":
        result_label.configure(text=result,text_color="green")
        wins += 1
    elif result == "你输了！":
        result_label.configure(text=result,text_color="red")
        losses += 1
    else:
        result_label.configure(text=result,text_color="orange")
        draws += 1
        
    #5.更新计分板
    score_label.configure(text=f"🏆胜{wins},负{losses},平{draws}")
    
#---创建三个按钮---
# 按钮（CTkButton 支持圆角 corner_radius 和悬停色 hover_color）
btn_frame = ctk.CTkFrame(root,fg_color="transparent")
btn_frame.pack(pady=20)

#用 lambda 将玩家的选择传给 play_game函数
btn_rock = ctk.CTkButton(btn_frame,text="✊ 石头",width=100,height=40,corner_radius=10,hover_color="#00cc00",command=lambda:play_game("石头"))
btn_rock.pack(side=ctk.LEFT,padx=10)
btn_scissors = ctk.CTkButton(btn_frame,text="✌️ 剪刀",width=100,height=40,corner_radius=10,hover_color="#cda4f9",command=lambda:play_game("剪刀"))
btn_scissors.pack(side=ctk.LEFT,padx=10)
btn_paper = ctk.CTkButton(btn_frame,text="✋ 布",width=100,height=40,corner_radius=10,hover_color="#00cc00",command=lambda:play_game("布"))
btn_paper.pack(side=ctk.LEFT,padx=10)

#进入时间循环(让窗口保持响应)
root.mainloop()