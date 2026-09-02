#------"石头剪刀布"-----
import random

def Rock_Paper_Scissors(player_choice,computer_choice):
    print(f"你选择的是{player_choice}",f"电脑的选择是{computer_choice}")
    
     # 判断胜负
    if player_choice == computer_choice:
        #print("平局")
        return "平局"
    elif (player_choice == "石头" and computer_choice == "剪刀") or  \
         (player_choice == "剪刀" and computer_choice == "布") or \
         (player_choice == "布" and computer_choice == "石头"):
        #print("这局你赢了！")
        return "这局你赢了！"
    else:    
        #print("你输了！")
        return "你输了！"
        
def main():  # 定义函数用 "def"
    choices = ["石头","剪刀","布"]  # 数组
    showhand = {"石头":"石头","剪刀":"剪刀","布":"布","r":"石头","s":"剪刀","p":"布"}   #用字典来映射简写
    
    print("欢迎来到石头剪刀布游戏！")
    print("请输入：石头/剪刀/布 (或输入简写:r/s/p)")
    
    while True:
        player_input = input("你的选择:").strip().lower()   # strip() 是去除字符串前后的空格， lower() 是将英文字符小写化
        if player_input not in showhand:
            print("输入无效，请重新输入!")
            continue
        
        player_choice = showhand[player_input]
        computer_choice = random.choice(choices)
        
        # 调用函数传参判断胜负
        result = Rock_Paper_Scissors(player_choice,computer_choice)
        print(result)
        # 询问是否再来一次
        while True:
            again = input("再来一局? y/n:").strip().lower()
            if again == "y":
                break
            elif again == "n":
                print("下次再来哈~")
                return   # return 是跳出函数，结束代码最优雅，也是最温和！break  是跳出循环，但函数里出来循环外的代码还会执行exit() 是跳出整个代码，直接杀死进程，太暴力，尽量少用；
            else:
                print("输入错误，请输入 y/n: ")
        
# 运行游戏
if __name__ == "__main__":  
    # 这段代码是 Python 中最经典、最重要的入口点惯用法（Entry Point Idiom）。它的核心作用是：让同一个 .py 文件既能被直接运行，又能被安全地导入为模块，而不会在导入时自动执行游戏.
    # “如果这个脚本是被人直接点击运行或在命令行里执行的主程序，那么就去启动游戏；如果它是被别人引进来的‘工具包’，那就老老实实待着，别擅自开始玩。”
    main()
    
        