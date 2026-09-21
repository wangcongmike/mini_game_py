import tkinter as tk
import random
from customtkinter import CTkToplevel,CTkButton,CTkLabel,CTkFont

def Open_Snake(parent):
    #1.创建窗口
    window = CTkToplevel(parent)
    window.title("贪吃蛇")
    window.geometry("700x700")
    window.resizable(False,False)
    
    #2.延迟提升窗口
    window.after(100,window.lift)   #0.1s后提升到叠层顶部
    window.after(200,window.focus_set)  #0.2s后聚焦
    
    #3.游戏参数
    CELL = 20   #像素
    COLS = 30   #行
    ROWS = 30   #列
    WIDTH = COLS * CELL
    HEIGHT = ROWS * CELL
    SPEED = 150 #速度，值越小越快
    
    #4.状态变量   
    snake = [(5,10),(4,10),(3,10)]  #定义蛇的坐标站点，头部在前
    direction = "Right" #定义初始移动方向
    next_direction = "Right"    #确定下一帧移动方向也是同步，防止乱跑
    food = None
    score = 0
    running = True  #定时器开启
    
    #5.创建画布   
    canvas = tk.Canvas(window,width=WIDTH,height=HEIGHT,bg="#1e1e1e",highlightthickness=0)  #消除聚焦后的边框
    canvas.pack(pady=10)
    
    #6.分数标签   
    score_label = CTkLabel(window,text="得分:0",font=CTkFont(size=16,weight="bold"))
    score_label.pack(pady=5)
    
    #7.随机生成实物，避开蛇身
    def Generate_Food():
        nonlocal food
        while True:
            x = random.randint(0,COLS - 1)
            y = random.randint(0,ROWS - 1)
            if(x,y) not in snake:
                food = (x,y)
                break
    
    #8.绘制画布 [画食物+🐍]
    def Draw():
        canvas.delete("all")  #清空旧帧内容，刷新界面
        if food:
            fx,fy = food
            canvas.create_oval(fx*CELL,fy*CELL,(fx+1)*CELL,(fy+1)*CELL,fill="#ff4d4d",outline="")   #将食物像素化画圆
            
        for i,(x,y) in enumerate(snake):    #接收可迭代的数据，并返回一个枚举对象，生成一个索引+值 -例如- 1(5,10)...
            color = "#00ff88" if i == 0 else "#00cc66"
            canvas.create_rectangle(x*CELL,y*CELL,(x+1)*CELL,(y+1)*CELL,fill=color,outline="#1e1e1e")   #画方形
    
    #9.移动逻辑
    def Move():
        nonlocal snake,direction,next_direction,score,running,score_label
        if not running:
            return
        
        #9.1、更新方向，禁止反向
        if  (direction == "Right" and next_direction != "Left") or \
            (direction == "Left" and next_direction != "Right") or \
            (direction == "Up" and next_direction != "Down") or \
            (direction == "Down" and next_direction != "Up"):
            direction = next_direction
            
        #9.2、计算新头部
        head_x,head_y = snake[0]
        if direction == "Right":
            new_head = (head_x + 1,head_y)
        elif direction == "Left":
            new_head = (head_x - 1,head_y)
        elif direction == "Up":
            new_head = (head_x,head_y - 1)
        else:   #Down
            new_head = (head_x,head_y + 1)  #######
            
        #9.3、撞墙或者撞到自己
        if (new_head[0] < 0 or new_head[0] >= COLS or   #[0]左右撞墙
            new_head[1] < 0 or new_head[1] >= ROWS or   #[1]上下撞墙
            new_head in snake): #撞到自己
            running = False
            canvas.create_text(WIDTH // 2,HEIGHT // 2,text="游戏结束\n按 R 重新开始！", #在画布中间弹窗
                               fill="white",font=("Arial",20,"bold"),   
                               justify="center")    #文本居中
            return  #退出该函数
        
        #9.4、移动蛇
        snake.insert(0,new_head)
        if new_head == food:
            score += 1
            score_label.configure(text=f"得分:{score}")
            Generate_Food() #吃完了要生成新的事物
        else:
            snake.pop() #没吃到就掉尾巴，保持长度不变
            
        Draw()  #随时刷新画布
        window.after(SPEED,Move)
        
    #10.键盘控制
    def On_Key(event):
        nonlocal next_direction
        key = event.keysym
        if key == "Up":
            next_direction = "Up"
        elif key == "Down":
            next_direction = "Down"
        elif key == "Left":
            next_direction = "Left"
        elif key == "Right":
            next_direction = "Right"
        elif key.lower() == "r":
            Restart()

    #11.重新开始
    def Restart():
        nonlocal snake,direction,next_direction,score,running,food
        snake = [(5,10),(4,10),(3,10)]
        direction = "Right" 
        next_direction = "Right"    
        score = 0
        running = True  
        score_label.configure(text="得分: 0")
        Generate_Food()
        Draw()
        Move()
    
    #12.绑定键盘
    window.bind("<Key>",On_Key)
    window.focus_set()
    
    #13.初始化
    Generate_Food()
    Draw()
    Move()
    
    #14.关闭定时器
    def On_Close():
        nonlocal running 
        running = False
        window.destroy()
        
    #15.
    window.protocol("WM_DELETE_WINDOW", On_Close)