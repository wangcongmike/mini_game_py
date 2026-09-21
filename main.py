import customtkinter as ctk
from rps_gui import Open_Rps
from guess_gui import Open_Guess
from snake_gui import Open_Snake

#设置主窗口
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.title("🎮 游戏大厅")
root.geometry("300x300")
root.resizable(False, False)

title_label = ctk.CTkLabel(root, text="请选择游戏", font=ctk.CTkFont(size=20, weight="bold"))
title_label.pack(pady=30)

btn_rps = ctk.CTkButton(root, text="✊ 石头剪刀布", width=200, height=40,command=lambda: Open_Rps(root))
btn_rps.pack(pady=10)

btn_guess = ctk.CTkButton(root, text="🔢 猜数字", width=200, height=40,command=lambda: Open_Guess(root))
btn_guess.pack(pady=10)

btn_snake = ctk.CTkButton(root,text="🐍贪吃蛇",width=200,height=40,command=lambda:Open_Snake(root))
btn_snake.pack(pady=10)

root.mainloop()