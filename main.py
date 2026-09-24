import customtkinter as ctk
import math
from rps_gui import Open_Rps
from guess_gui import Open_Guess
from snake_gui import Open_Snake

#设置主窗口
ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.title("🎮 游戏大厅")
root.geometry("400x400")
root.resizable(False, False)

#渐变主题
title_label = ctk.CTkLabel(root, text="请选择游戏", font=ctk.CTkFont(size=20, weight="bold"))
title_label.place(relx=0.5,y=40,anchor="center")

#创建按钮
btn_rps = ctk.CTkButton(root, text="✊ 石头剪刀布", width=20, height=40,
                        corner_radius=15,font=ctk.CTkFont(size=16,weight="bold"),command=lambda: Open_Rps(root))
btn_guess = ctk.CTkButton(root, text="🔢 猜数字", width=200, height=40,
                          corner_radius=15,font=ctk.CTkFont(size=16,weight="bold"),command=lambda: Open_Guess(root))
btn_snake = ctk.CTkButton(root,text="🐍贪吃蛇",width=200,height=40,
                          corner_radius=15,font=ctk.CTkFont(size=16,weight="bold"),command=lambda:Open_Snake(root))

#用place布局，才能动态改变y轴坐标
btn_rps.place(relx=0.5,y=120,anchor="center")
btn_guess.place(relx=0.5,y=200,anchor="center")
btn_snake.place(relx=0.5,y=280,anchor="center")

#悬停放大
def on_enter(btn):
    btn.configure(width=240,height=56)
    
def on_leave(btn):
    btn.configure(width=220,height=50)
    
for btn in [btn_rps,btn_guess,btn_snake]:
    btn.bind("<Enter>",lambda e,b=btn:on_enter(b))
    btn.bind("<Leave>",lambda e,b=btn:on_leave(b))    
    
#标题呼吸动画
def animate_title(phase=0):
    t = (math.sin(phase)+1) / 2
    r = int(60 + 80*t)
    g = int(60 + 80*t)
    b = 255
    title_label.configure(text_color=f"#{r:02x}{g:02x}{b:02x}")
    root.after(60,lambda:animate_title(phase + 0.15))
    
#按钮浮动动画
def float_button(btn,base_y,phase):
    offset = int(4 * math.sin(phase))
    btn.place_configure(y = base_y + offset)
    root.after(60,lambda:float_button(btn,base_y,phase + 0.1))
    
#
animate_title()
float_button(btn_rps,120,0)
float_button(btn_guess,200,0.7)
float_button(btn_snake,280,1.4)

root.mainloop()