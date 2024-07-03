import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

# for row in range(3):
#     for col in range(3):
#         button = tk.Button(
#             window, text="", command=lambda r=row, c=col: button_action(r, c)
#         )

# 同じボタンを押せないようにする
# 勝利した瞬間、全てのボタンの機能をオフにする

human_player = "O"
ai_player = "X"
current_player = human_player


# ボタンそれぞれにプレイヤー１の時◯、プレイヤー２の時バツの機能を追加
def ai_action():
    if button1.cget("text") == "":
        button1.config(text=ai_player)

    elif button2.cget("text") == "":
        button2.config(text=ai_player)

    elif button3.cget("text") == "":
        button3.config(text=ai_player)

    elif button4.cget("text") == "":
        button4.config(text=ai_player)

    elif button5.cget("text") == "":
        button5.config(text=ai_player)

    elif button6.cget("text") == "":
        button6.config(text=ai_player)

    elif button7.cget("text") == "":
        button7.config(text=ai_player)

    elif button8.cget("text") == "":
        button8.config(text=ai_player)

    elif button9.cget("text") == "":
        button9.config(text=ai_player)
    ai_reach()


def order_action():
    coin = random.randint(1, 2)
    if coin == 1:
        current_player == human_player
    elif coin == 2:
        ai_action()


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    if button1.cget("text") == "":
        button1.config(text=human_player)
        ai_action()
    victory()
    ai_victory()


def button_action2():  # 関数の定義 ※ボタンが押されたときの動き
    if button2.cget("text") == "":
        button2.config(text=human_player)
        ai_action()
    victory()
    ai_victory()


def button_action3():  # 関数の定義 ※ボタンが押されたときの動き
    if button3.cget("text") == "":
        button3.config(text=human_player)
        ai_action()
    victory()
    ai_victory()


def button_action4():  # 関数の定義 ※ボタンが押されたときの動き
    if button4.cget("text") == "":
        button4.config(text=human_player)
        ai_action()
    victory()
    ai_victory()


def button_action5():  # 関数の定義 ※ボタンが押されたときの動き
    if button5.cget("text") == "":
        button5.config(text=human_player)
        ai_action()
    victory()
    ai_victory()


def button_action6():  # 関数の定義 ※ボタンが押されたときの動き
    if button6.cget("text") == "":
        button6.config(text=human_player)
        ai_action()
    victory()
    ai_victory()


def button_action7():  # 関数の定義 ※ボタンが押されたときの動き
    if button7.cget("text") == "":
        button7.config(text=human_player)
        ai_action()
    victory()
    ai_victory()


def button_action8():  # 関数の定義 ※ボタンが押されたときの動き
    if button8.cget("text") == "":
        button8.config(text=human_player)
        ai_action()
    victory()
    ai_victory()


def button_action9():  # 関数の定義 ※ボタンが押されたときの動き
    if button9.cget("text") == "":
        button9.config(text=human_player)
        ai_action()
    victory()
    ai_victory()


def victory():
    # 横１列目
    if (button1.cget("text"), button2.cget("text"), button3.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        label1.config(text="もう勝ちでいいよ１")
    # 横２列目
    if (button4.cget("text"), button5.cget("text"), button6.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        label1.config(text="もう勝ちでいいよ２")
    # 横３列目
    if (button7.cget("text"), button8.cget("text"), button9.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        label1.config(text="もう勝ちでいいよ３")
    # 縦１列目
    if (button1.cget("text"), button4.cget("text"), button7.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        label1.config(text="もう勝ちでいいよ４")
    # 縦２列目
    if (button2.cget("text"), button5.cget("text"), button8.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        label1.config(text="もう勝ちでいいよ５")
    # 縦３列目
    if (button3.cget("text"), button6.cget("text"), button9.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        label1.config(text="もう勝ちでいいよ６")
    # 斜め１個目
    if (button1.cget("text"), button5.cget("text"), button9.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        label1.config(text="もう勝ちでいいよ7")
    # 斜め２個目
    if (button3.cget("text"), button5.cget("text"), button7.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        label1.config(text="もう勝ちでいいよ8")


def ai_victory():
    # 横１列目
    if (button1.cget("text"), button2.cget("text"), button3.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        label1.config(text="もうaiの勝ちでいいよ１")
    # 横２列目
    if (button4.cget("text"), button5.cget("text"), button6.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        label1.config(text="もうaiの勝ちでいいよ２")
    # 横３列目
    if (button7.cget("text"), button8.cget("text"), button9.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        label1.config(text="もうaiの勝ちでいいよ３")
    # 縦１列目
    if (button1.cget("text"), button4.cget("text"), button7.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        label1.config(text="もうaiの勝ちでいいよ４")
    # 縦２列目
    if (button2.cget("text"), button5.cget("text"), button8.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        label1.config(text="もうaiの勝ちでいいよ５")
    # 縦３列目
    if (button3.cget("text"), button6.cget("text"), button9.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        label1.config(text="もうaiの勝ちでいいよ６")
    # 斜め１個目
    if (button1.cget("text"), button5.cget("text"), button9.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        label1.config(text="もうaiの勝ちでいいよ7")
    # 斜め２個目
    if (button3.cget("text"), button5.cget("text"), button7.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        label1.config(text="もうaiの勝ちでいいよ8")


def riset():
    button1.config(text="")
    button2.config(text="")
    button3.config(text="")
    button4.config(text="")
    button5.config(text="")
    button6.config(text="")
    button7.config(text="")
    button8.config(text="")
    button9.config(text="")

    label1.config(text="")
    order_action()


def ai_reach():
    # 横１列目
    if (button1.cget("text"), button2.cget("text"), button3.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ１")

    if (button2.cget("text"), button3.cget("text"), button1.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ１")

    if (button1.cget("text"), button3.cget("text"), button2.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ１")

    # 横２列目
    if (button4.cget("text"), button5.cget("text"), button6.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ２")

    if (button5.cget("text"), button6.cget("text"), button4.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ２")

    if (button4.cget("text"), button6.cget("text"), button5.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ２")

    # 横３列目
    if (button7.cget("text"), button8.cget("text"), button9.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ３")

    if (button8.cget("text"), button9.cget("text"), button7.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ３")

    if (button7.cget("text"), button9.cget("text"), button8.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ３")

    # 縦１列目
    if (button1.cget("text"), button4.cget("text"), button7.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ４")

    if (button4.cget("text"), button7.cget("text"), button1.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ４")

    if (button1.cget("text"), button7.cget("text"), button4.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ４")

    # 縦２列目
    if (button2.cget("text"), button5.cget("text"), button8.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ５")

    if (button5.cget("text"), button8.cget("text"), button2.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ５")

    if (button2.cget("text"), button8.cget("text"), button5.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ５")

    # 縦３列目
    if (button3.cget("text"), button6.cget("text"), button9.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ６")

    if (button6.cget("text"), button9.cget("text"), button3.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ６")

    if (button3.cget("text"), button9.cget("text"), button6.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ６")

    # 斜め１個目
    if (button1.cget("text"), button5.cget("text"), button9.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ７")

    if (button5.cget("text"), button9.cget("text"), button1.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ７")

    if (button1.cget("text"), button9.cget("text"), button5.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ７")

    # 斜め２個目
    if (button3.cget("text"), button5.cget("text"), button7.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ８")

    if (button5.cget("text"), button7.cget("text"), button3.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ８")

    if (button3.cget("text"), button7.cget("text"), button5.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label2.config(text="もうaiのリーチでいいよ８")


label1 = tk.Label(window, text="円罰ゲーム", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

label2 = tk.Label(window, text="あなたは円です", bg=bg_color, fg=fg_color)
label2.pack(pady=10)

riset_button = tk.Button(window, text="リセット", command=riset)
riset_button.pack(pady=10)

frame = tk.Frame(window)
frame.pack()

#  ボタンの作成
button1 = tk.Button(frame, text="", command=button_action)
button1.grid(row=0, column=0, padx=2, pady=2)

button2 = tk.Button(frame, text="", command=button_action2)
button2.grid(row=0, column=1, padx=2, pady=2)

button3 = tk.Button(frame, text="", command=button_action3)
button3.grid(row=0, column=2, padx=2, pady=2)

button4 = tk.Button(frame, text="", command=button_action4)
button4.grid(row=1, column=0, padx=2, pady=2)

button5 = tk.Button(frame, text="", command=button_action5)
button5.grid(row=1, column=1, padx=2, pady=2)

button6 = tk.Button(frame, text="", command=button_action6)
button6.grid(row=1, column=2, padx=2, pady=2)

button7 = tk.Button(frame, text="", command=button_action7)
button7.grid(row=2, column=0, padx=2, pady=2)

button8 = tk.Button(frame, text="", command=button_action8)
button8.grid(row=2, column=1, padx=2, pady=2)

button9 = tk.Button(frame, text="", command=button_action9)
button9.grid(row=2, column=2, padx=2, pady=2)

order_action()

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
