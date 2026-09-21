import customtkinter as ctk
import random
from rock_paper_scissors import Rock_Paper_Scissors

def Open_Rps(parent):
     # 创建主窗口
    window = ctk.CTkToplevel(parent)
    window.title("石头剪刀布")
    window.geometry("400x500")
    window.resizable(False,False) #禁止调窗口大小
    #window.lift()
    
    #设置延迟
    #window.after(100,lambda:
       #(window.lift(),
       # window.focus_force(),
       # window.attributes('-topmost',1)
       # ))
    #window.after(300,lambda:window.attributes('-topmost',0))
    
    window.after(100,window.lift)
    window.after(200,window.focus_set)  #推荐这种写法,更温和；
    
    #创建计分板
    wins = 0
    losses = 0
    draws = 0

    #五局三胜比赛模式参数变量
    match_round = 0            #当前局数，从0开始
    player_match_wins  = 0     #玩家赢的次数
    computer_match_wins = 0    #电脑赢的次数
    match_goal = 3             #目标五局三胜
    game_over = False          #是否结束比赛，初始值为false

    #核心设置：外观和主题色
    ctk.set_appearance_mode("dark")     #可选 "dark","system","light"
    ctk.set_default_color_theme("blue") #可选 "blue","dark_blue","green"

    #提示标签
    prompt_label = ctk.CTkLabel(window,text="请选择你的出拳:",font=ctk.CTkFont(size=16,weight="bold"))
    prompt_label.pack(pady=10)

    #结果显示标签,初始为空
    result_label = ctk.CTkLabel(window,text="",font=ctk.CTkFont(size=18),text_color="blue")
    result_label.pack(pady=10)

    #电脑出拳显示   
    computer_label = ctk.CTkLabel(window,text="",font=ctk.CTkFont(size=14))
    computer_label.pack(pady=10)

    #计分板UI
    score_label = ctk.CTkLabel(window,text=("🏆 胜: 0    负: 0    平: 0"),font=ctk.CTkFont(size=16,weight="bold"))
    score_label.pack(pady=(10,5))  #放在顶部

    #比赛信息标签
    round_label = ctk.CTkLabel(window,text="第 0 局",font=ctk.CTkFont(size=14))
    round_label.pack(pady=(5,0))

    #---创建三个按钮---
    # 按钮（CTkButton 支持圆角 corner_radius 和悬停色 hover_color）
    btn_frame = ctk.CTkFrame(window,fg_color="transparent")
    btn_frame.pack(pady=20)

    #用 lambda 将玩家的选择传给 play_game函数
    btn_rock = ctk.CTkButton(btn_frame,text="✊ 石头",width=100,height=40,corner_radius=10,hover_color="#00cc00",command=lambda:Play_Game("石头"))
    btn_rock.pack(side=ctk.LEFT,padx=10)
    btn_scissors = ctk.CTkButton(btn_frame,text="✌️ 剪刀",width=100,height=40,corner_radius=10,hover_color="#cda4f9",command=lambda:Play_Game("剪刀"))
    btn_scissors.pack(side=ctk.LEFT,padx=10)
    btn_paper = ctk.CTkButton(btn_frame,text="✋ 布",width=100,height=40,corner_radius=10,hover_color="#00cc00",command=lambda:Play_Game("布"))
    btn_paper.pack(side=ctk.LEFT,padx=10)

    #比赛重置按钮
    def Reset_Match():
        nonlocal match_round,player_match_wins,computer_match_wins,game_over
        nonlocal wins,losses,draws
        
        #重置比赛状态
        match_round = 0
        player_match_wins = 0
        computer_match_wins = 0
        game_over = False
        
        #重置胜负平
        wins = 0
        losses = 0
        draws = 0
        
        #更新界面标签
        round_label.configure(text = "第 0 局")
        result_label.configure(text = "比赛开始！",text_color = "black")
        computer_label.configure(text = "")
        score_label.configure(text=f"🏆胜{wins},负{losses},平{draws}")
        
        #启用所有按钮(如果有disable状态)
        btn_rock.configure(state = "normal")
        btn_scissors.configure(state = "normal")
        btn_paper.configure(state = "normal")
    reset_btn = ctk.CTkButton(window,text="🔄 重新比赛",command=Reset_Match,width=120)
    reset_btn.pack(pady=5)

    #禁用按钮函数
    def Disable_Btn():
        btn_rock.configure(state="disabled")
        btn_scissors.configure(state="disabled")
        btn_paper.configure(state="disabled")

    #核心游戏函数(点击按钮时调用)
    def Play_Game(player_choice):
        nonlocal wins,losses,draws #申明要修改全局变量
        nonlocal match_round,player_match_wins,computer_match_wins,game_over
        
        if game_over:
            return  #比赛结束，中断，不再响应点击
        
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
            player_match_wins += 1
        elif result == "你输了！":
            result_label.configure(text=result,text_color="red")
            losses += 1
            computer_match_wins += 1
        else:
            result_label.configure(text=result,text_color="orange")
            draws += 1
            
        #5.更新计分板
        score_label.configure(text=f"🏆胜{wins},负{losses},平{draws}")
        
        #6.更新比赛局数
        match_round += 1
        round_label.configure(text=f"第{match_round}局")
        
        #7.检查是否有一方胜数达到3局
        if player_match_wins >= match_goal:
            result_label.configure(text="🎉 你赢得比赛！ 🎉",text_color="green")
            game_over = True
            Disable_Btn()
        elif computer_match_wins >= match_goal:
            result_label.configure(text="😢 电脑赢得比赛！",text_color="red")
            game_over = True
            Disable_Btn()
        else:
            pass

    #进入时间循环(让窗口保持响应)
    #window.mainloop()