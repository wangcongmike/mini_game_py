import customtkinter as ctk
import random

def open_guess(parent):
    #搭建主框架
    window = ctk.CTkToplevel(parent)
    window.title("猜数字")
    window.geometry("400x300")
    window.lift()
    
    target = random.randint(1,100)
    attempts = 0    #定义次数

    
    #游戏函数
    def Check_Guess():  
        nonlocal attempts
        try:
            guess = int(entry.get())
        except ValueError:
            result_lable.configure(text="请输入一个数字",text_color="red")
            return
        attempts += 1
        if guess < target:
            result_lable.configure(text="小了,往大点猜!",text_color="blue")
        elif guess > target:
            result_lable.configure(text="大了,往下点猜!",text_color="orange")
        else:
            result_lable.configure(text=f"这是第{attempts}次，恭喜你猜对了!",text_color="green")
            
    #
    prompt = ctk.CTkLabel(window,text="请猜一个1~100之间的数字!",font=ctk.CTkFont(size=16))
    prompt.pack(pady=10)
    
    #
    entry = ctk.CTkEntry(window,width=150)
    entry.pack(pady=10)
    
    #
    btn = ctk.CTkButton(window,text="猜!",command=Check_Guess)
    btn.pack(pady=10)
    
    #
    result_lable = ctk.CTkLabel(window,text="",font=ctk.CTkFont(size=16))
    result_lable.pack(pady=20)