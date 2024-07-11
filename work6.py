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

human_player = "O"
ai_player = "X"
check = ""


# 通常時のAIの行動を設定
def ai_action():
    if button5.cget("text") == "":
        button5.config(text=ai_player)
        draw_check()

    elif (
        button3.cget("text"),
        button7.cget("text"),
        button2.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        button2.config(text=ai_player)
        draw_check()

    elif (
        button1.cget("text"),
        button9.cget("text"),
        button2.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        button2.config(text=ai_player)
        draw_check()

    elif (
        button1.cget("text"),
        button8.cget("text"),
        button7.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        button7.config(text=ai_player)
        draw_check()

    elif (
        button3.cget("text"),
        button8.cget("text"),
        button9.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        button9.config(text=ai_player)
        draw_check()

    elif (
        button6.cget("text"),
        button7.cget("text"),
        button9.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        button9.config(text=ai_player)
        draw_check()

    elif (
        button6.cget("text"),
        button8.cget("text"),
        button9.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        button9.config(text=ai_player)
        draw_check()

    elif button1.cget("text") == "":
        button1.config(text=ai_player)
        draw_check()

    elif button9.cget("text") == "":
        button9.config(text=ai_player)
        draw_check()

    elif button7.cget("text") == "":
        button7.config(text=ai_player)
        draw_check()

    elif button3.cget("text") == "":
        button3.config(text=ai_player)
        draw_check()

    elif button2.cget("text") == "":
        button2.config(text=ai_player)
        draw_check()

    elif button4.cget("text") == "":
        button4.config(text=ai_player)
        draw_check()

    elif button6.cget("text") == "":
        button6.config(text=ai_player)
        draw_check()

    elif button8.cget("text") == "":
        button8.config(text=ai_player)
        draw_check()
    ai_reach()


def order_action():
    coin = random.randint(1, 2)
    if coin == 1:
        label2.config(text="嬉しい！あなたが先手です")
        label2.config(text="嬉しい！あなたが先手です")
    elif coin == 2:
        label2.config(text="AIが先手です がんばって！")
        label2.config(text="AIが先手です がんばって！")
        ai_action()


# 引き分けチェッカー
def draw_check():
    if button1.cget("text") == "":
        label3.config(text="ファイト！")

    elif button2.cget("text") == "":
        label3.config(text="ファイト！")

    elif button3.cget("text") == "":
        label3.config(text="ファイト！")

    elif button4.cget("text") == "":
        label3.config(text="ファイト！")

    elif button5.cget("text") == "":
        label3.config(text="ファイト！")

    elif button6.cget("text") == "":
        label3.config(text="ファイト！")

    elif button7.cget("text") == "":
        label3.config(text="ファイト！")

    elif button8.cget("text") == "":
        label3.config(text="ファイト！")

    elif button9.cget("text") == "":
        label3.config(text="ファイト！")

    else:
        label3.config(text="ドロー！")
        draw_color()
        draw_color()


# ボタン１が押されたら
def button_action():
    if button1.cget("text") == "":
        button1.config(text=human_player)
        draw_check()
        victory()
        ai_action_check()
        ai_victory()


# ボタン２が押されたら
def button_action2():
    if button2.cget("text") == "":
        button2.config(text=human_player)
        draw_check()
        victory()
        ai_action_check()
        ai_victory()


# ボタン３が押されたら
def button_action3():
    if button3.cget("text") == "":
        button3.config(text=human_player)
        draw_check()
        victory()
        ai_action_check()
        ai_victory()


# ボタン４が押されたら
def button_action4():
    if button4.cget("text") == "":
        button4.config(text=human_player)
        draw_check()
        victory()
        ai_action_check()
        ai_victory()


# ボタン５が押されたら
def button_action5():
    if button5.cget("text") == "":
        button5.config(text=human_player)
        draw_check()
        victory()
        ai_action_check()
        ai_victory()


# ボタン６が押されたら
def button_action6():
    if button6.cget("text") == "":
        button6.config(text=human_player)
        draw_check()
        victory()
        ai_action_check()
        ai_victory()


# ボタン７が押されたら
def button_action7():
    if button7.cget("text") == "":
        button7.config(text=human_player)
        draw_check()
        victory()
        ai_action_check()
        ai_victory()


# ボタン８が押されたら
def button_action8():
    if button8.cget("text") == "":
        button8.config(text=human_player)
        draw_check()
        victory()
        ai_action_check()
        ai_victory()


# ボタン９が押されたら
def button_action9():
    if button9.cget("text") == "":
        button9.config(text=human_player)
        draw_check()
        victory()
        ai_action_check()
        ai_victory()


# 勝利条件の設定と動き
def victory():
    # 横１列目
    if (button1.cget("text"), button2.cget("text"), button3.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        button1.config(fg="#008000")
        button2.config(fg="#008000")
        button3.config(fg="#008000")

        button4.config(state="disabled")
        button5.config(state="disabled")
        button6.config(state="disabled")
        button7.config(state="disabled")
        button8.config(state="disabled")
        button9.config(state="disabled")

        label3.config(text="勝利！")

        ai_action_check(False)

    # 横２列目
    if (button4.cget("text"), button5.cget("text"), button6.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        button4.config(fg="#008000")
        button5.config(fg="#008000")
        button6.config(fg="#008000")

        button1.config(state="disabled")
        button2.config(state="disabled")
        button3.config(state="disabled")
        button7.config(state="disabled")
        button8.config(state="disabled")
        button9.config(state="disabled")

        label3.config(text="勝利！")

        ai_action_check(False)

    # 横３列目
    if (button7.cget("text"), button8.cget("text"), button9.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        button7.config(fg="#008000")
        button8.config(fg="#008000")
        button9.config(fg="#008000")

        button1.config(state="disabled")
        button2.config(state="disabled")
        button3.config(state="disabled")
        button4.config(state="disabled")
        button5.config(state="disabled")
        button6.config(state="disabled")

        label3.config(text="勝利！")

        ai_action_check(False)

    # 縦１列目
    if (button1.cget("text"), button4.cget("text"), button7.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        button1.config(fg="#008000")
        button4.config(fg="#008000")
        button7.config(fg="#008000")

        button2.config(state="disabled")
        button3.config(state="disabled")
        button5.config(state="disabled")
        button6.config(state="disabled")
        button8.config(state="disabled")
        button9.config(state="disabled")

        label3.config(text="勝利！")

        ai_action_check(False)

    # 縦２列目
    if (button2.cget("text"), button5.cget("text"), button8.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        button2.config(fg="#008000")
        button5.config(fg="#008000")
        button8.config(fg="#008000")

        button1.config(state="disabled")
        button3.config(state="disabled")
        button4.config(state="disabled")
        button6.config(state="disabled")
        button7.config(state="disabled")
        button9.config(state="disabled")

        label3.config(text="勝利！")

        ai_action_check(False)

    # 縦３列目
    if (button3.cget("text"), button6.cget("text"), button9.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        button3.config(fg="#008000")
        button6.config(fg="#008000")
        button9.config(fg="#008000")

        button1.config(state="disabled")
        button2.config(state="disabled")
        button4.config(state="disabled")
        button5.config(state="disabled")
        button7.config(state="disabled")
        button8.config(state="disabled")

        label3.config(text="勝利！")

        ai_action_check(False)

    # 斜め１個目
    if (button1.cget("text"), button5.cget("text"), button9.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        button1.config(fg="#008000")
        button5.config(fg="#008000")
        button9.config(fg="#008000")

        button2.config(state="disabled")
        button3.config(state="disabled")
        button4.config(state="disabled")
        button6.config(state="disabled")
        button7.config(state="disabled")
        button8.config(state="disabled")

        label3.config(text="勝利！")

        ai_action_check(False)

    # 斜め２個目
    if (button3.cget("text"), button5.cget("text"), button7.cget("text")) == (
        human_player,
        human_player,
        human_player,
    ):
        button3.config(fg="#008000")
        button5.config(fg="#008000")
        button7.config(fg="#008000")

        button1.config(state="disabled")
        button2.config(state="disabled")
        button4.config(state="disabled")
        button6.config(state="disabled")
        button8.config(state="disabled")
        button9.config(state="disabled")

        label3.config(text="勝利！")

        ai_action_check(False)


# AI勝利時の動き
def ai_victory():
    # 横１列目
    if (button1.cget("text"), button2.cget("text"), button3.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        button1.config(fg="#008000")
        button2.config(fg="#008000")
        button3.config(fg="#008000")

        button4.config(state="disabled")
        button5.config(state="disabled")
        button6.config(state="disabled")
        button7.config(state="disabled")
        button8.config(state="disabled")
        button9.config(state="disabled")

        label3.config(text="AIの勝利！")
    # 横２列目
    if (button4.cget("text"), button5.cget("text"), button6.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        button4.config(fg="#008000")
        button5.config(fg="#008000")
        button6.config(fg="#008000")

        button1.config(state="disabled")
        button2.config(state="disabled")
        button3.config(state="disabled")
        button7.config(state="disabled")
        button8.config(state="disabled")
        button9.config(state="disabled")

        label3.config(text="AIの勝利！")
    # 横３列目
    if (button7.cget("text"), button8.cget("text"), button9.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        button7.config(fg="#008000")
        button8.config(fg="#008000")
        button9.config(fg="#008000")

        button1.config(state="disabled")
        button2.config(state="disabled")
        button3.config(state="disabled")
        button4.config(state="disabled")
        button5.config(state="disabled")
        button6.config(state="disabled")

        label3.config(text="AIの勝利！")
    # 縦１列目
    if (button1.cget("text"), button4.cget("text"), button7.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        button1.config(fg="#008000")
        button4.config(fg="#008000")
        button7.config(fg="#008000")

        button2.config(state="disabled")
        button3.config(state="disabled")
        button5.config(state="disabled")
        button6.config(state="disabled")
        button8.config(state="disabled")
        button9.config(state="disabled")

        label3.config(text="AIの勝利！")
    # 縦２列目
    if (button2.cget("text"), button5.cget("text"), button8.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        button2.config(fg="#008000")
        button5.config(fg="#008000")
        button8.config(fg="#008000")

        button1.config(state="disabled")
        button3.config(state="disabled")
        button4.config(state="disabled")
        button6.config(state="disabled")
        button7.config(state="disabled")
        button9.config(state="disabled")

        label3.config(text="AIの勝利！")
    # 縦３列目
    if (button3.cget("text"), button6.cget("text"), button9.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        button3.config(fg="#008000")
        button6.config(fg="#008000")
        button9.config(fg="#008000")

        button1.config(state="disabled")
        button2.config(state="disabled")
        button4.config(state="disabled")
        button5.config(state="disabled")
        button7.config(state="disabled")
        button8.config(state="disabled")

        label3.config(text="AIの勝利！")
    # 斜め１列目
    if (button1.cget("text"), button5.cget("text"), button9.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        button1.config(fg="#008000")
        button5.config(fg="#008000")
        button9.config(fg="#008000")

        button2.config(state="disabled")
        button3.config(state="disabled")
        button4.config(state="disabled")
        button6.config(state="disabled")
        button7.config(state="disabled")
        button8.config(state="disabled")

        label3.config(text="AIの勝利！")
    # 斜め２列目
    if (button3.cget("text"), button5.cget("text"), button7.cget("text")) == (
        ai_player,
        ai_player,
        ai_player,
    ):
        button3.config(fg="#008000")
        button5.config(fg="#008000")
        button7.config(fg="#008000")

        button1.config(state="disabled")
        button2.config(state="disabled")
        button4.config(state="disabled")
        button6.config(state="disabled")
        button8.config(state="disabled")
        button9.config(state="disabled")

        label3.config(text="AIの勝利！")


# リセット用の初期設定
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

    button1.config(state="normal")
    button2.config(state="normal")
    button3.config(state="normal")
    button4.config(state="normal")
    button5.config(state="normal")
    button6.config(state="normal")
    button7.config(state="normal")
    button8.config(state="normal")
    button9.config(state="normal")

    button1.config(fg="black")
    button2.config(fg="black")
    button3.config(fg="black")
    button4.config(fg="black")
    button5.config(fg="black")
    button6.config(fg="black")
    button7.config(fg="black")
    button8.config(fg="black")
    button9.config(fg="black")
    label3.config(text="スタート！")
    order_action()


# AIがリーチした時に、ラベル3のテキストを変更
def ai_reach():
    # 横１列目
    if (button1.cget("text"), button2.cget("text"), button3.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button2.cget("text"), button3.cget("text"), button1.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button1.cget("text"), button3.cget("text"), button2.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    # 横２列目
    if (button4.cget("text"), button5.cget("text"), button6.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button5.cget("text"), button6.cget("text"), button4.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button4.cget("text"), button6.cget("text"), button5.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    # 横３列目
    if (button7.cget("text"), button8.cget("text"), button9.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button8.cget("text"), button9.cget("text"), button7.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button7.cget("text"), button9.cget("text"), button8.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    # 縦１列目
    if (button1.cget("text"), button4.cget("text"), button7.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button4.cget("text"), button7.cget("text"), button1.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button1.cget("text"), button7.cget("text"), button4.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    # 縦２列目
    if (button2.cget("text"), button5.cget("text"), button8.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button5.cget("text"), button8.cget("text"), button2.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button2.cget("text"), button8.cget("text"), button5.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    # 縦３列目
    if (button3.cget("text"), button6.cget("text"), button9.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button6.cget("text"), button9.cget("text"), button3.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button3.cget("text"), button9.cget("text"), button6.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    # 斜め１個目
    if (button1.cget("text"), button5.cget("text"), button9.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button5.cget("text"), button9.cget("text"), button1.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button1.cget("text"), button9.cget("text"), button5.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    # 斜め２個目
    if (button3.cget("text"), button5.cget("text"), button7.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button5.cget("text"), button7.cget("text"), button3.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")

    if (button3.cget("text"), button7.cget("text"), button5.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        label3.config(text="AIがリーチ！")


# AI強化合宿
def ai_action_check():
    check = 0

    if (button1.cget("text"), button2.cget("text"), button3.cget("text")) == (
        human_player,
        human_player,
        "",
    ):
        check = 25
        draw_check()

    if (
        button2.cget("text"),
        button3.cget("text"),
        button1.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 26
        draw_check()

    if (
        button1.cget("text"),
        button3.cget("text"),
        button2.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 27
        draw_check()

    # 横２列目
    if (
        button4.cget("text"),
        button5.cget("text"),
        button6.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 28
        draw_check()

    if (
        button5.cget("text"),
        button6.cget("text"),
        button4.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 29
        draw_check()

    if (
        button4.cget("text"),
        button6.cget("text"),
        button5.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 30
        draw_check()

    # 横３列目
    if (
        button7.cget("text"),
        button8.cget("text"),
        button9.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 31
        draw_check()

    if (
        button8.cget("text"),
        button9.cget("text"),
        button7.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 32
        draw_check()

    if (
        button7.cget("text"),
        button9.cget("text"),
        button8.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 33
        draw_check()

    # 縦１列目
    if (
        button1.cget("text"),
        button4.cget("text"),
        button7.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 34
        draw_check()

    if (
        button4.cget("text"),
        button7.cget("text"),
        button1.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 35
        draw_check()

    if (
        button1.cget("text"),
        button7.cget("text"),
        button4.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 36
        draw_check()

    # 縦２列目
    if (
        button2.cget("text"),
        button5.cget("text"),
        button8.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 37
        draw_check()

    if (
        button5.cget("text"),
        button8.cget("text"),
        button2.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 38
        draw_check()

    if (
        button2.cget("text"),
        button8.cget("text"),
        button5.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 39
        draw_check()

    # 縦３列目
    if (
        button3.cget("text"),
        button6.cget("text"),
        button9.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 40
        draw_check()

    if (
        button6.cget("text"),
        button9.cget("text"),
        button3.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 41
        draw_check()

    if (
        button3.cget("text"),
        button9.cget("text"),
        button6.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 42
        draw_check()

    # 斜め１個目
    if (
        button1.cget("text"),
        button5.cget("text"),
        button9.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 43
        draw_check()

    if (
        button5.cget("text"),
        button9.cget("text"),
        button1.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 44
        draw_check()

    if (
        button1.cget("text"),
        button9.cget("text"),
        button5.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 45
        draw_check()

    # 斜め２個目
    if (
        button3.cget("text"),
        button5.cget("text"),
        button7.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 46
        draw_check()

    if (
        button5.cget("text"),
        button7.cget("text"),
        button3.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 47
        draw_check()

    if (
        button3.cget("text"),
        button7.cget("text"),
        button5.cget("text"),
    ) == (
        human_player,
        human_player,
        "",
    ):
        check = 48
        draw_check()

    if (button1.cget("text"), button2.cget("text"), button3.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 1

    if (button2.cget("text"), button3.cget("text"), button1.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 2

    if (button1.cget("text"), button3.cget("text"), button2.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 3

    # 横２列目
    if (button4.cget("text"), button5.cget("text"), button6.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 4

    if (button5.cget("text"), button6.cget("text"), button4.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 5

    if (button4.cget("text"), button6.cget("text"), button5.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 6

    # 横３列目
    if (button7.cget("text"), button8.cget("text"), button9.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 7

    if (button8.cget("text"), button9.cget("text"), button7.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 8

    if (button7.cget("text"), button9.cget("text"), button8.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 9

    # 縦１列目
    if (button1.cget("text"), button4.cget("text"), button7.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 10

    if (button4.cget("text"), button7.cget("text"), button1.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 11

    if (button1.cget("text"), button7.cget("text"), button4.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 12

    # 縦２列目
    if (button2.cget("text"), button5.cget("text"), button8.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 13

    if (button5.cget("text"), button8.cget("text"), button2.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 14

    if (button2.cget("text"), button8.cget("text"), button5.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 15

    # 縦３列目
    if (button3.cget("text"), button6.cget("text"), button9.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 16

    if (button6.cget("text"), button9.cget("text"), button3.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 17

    if (button3.cget("text"), button9.cget("text"), button6.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 18

    # 斜め１個目
    if (button1.cget("text"), button5.cget("text"), button9.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 19

    if (button5.cget("text"), button9.cget("text"), button1.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 20

    if (button1.cget("text"), button9.cget("text"), button5.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 21

    # 斜め２個目
    if (button3.cget("text"), button5.cget("text"), button7.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 22

    if (button5.cget("text"), button7.cget("text"), button3.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 23

    if (button3.cget("text"), button7.cget("text"), button5.cget("text")) == (
        ai_player,
        ai_player,
        "",
    ):
        check = 24

    # checkの数字で行動を変化

    if check == 0:
        ai_action()

    if check == 1:
        button3.config(text=ai_player)

    if check == 2:
        button1.config(text=ai_player)

    if check == 3:
        button2.config(text=ai_player)

    if check == 4:
        button6.config(text=ai_player)

    if check == 5:
        button4.config(text=ai_player)

    if check == 6:
        button5.config(text=ai_player)

    if check == 7:
        button9.config(text=ai_player)

    if check == 8:
        button7.config(text=ai_player)

    if check == 9:
        button8.config(text=ai_player)

    if check == 10:
        button7.config(text=ai_player)

    if check == 11:
        button1.config(text=ai_player)

    if check == 12:
        button4.config(text=ai_player)

    if check == 13:
        button8.config(text=ai_player)

    if check == 14:
        button2.config(text=ai_player)

    if check == 15:
        button5.config(text=ai_player)

    if check == 16:
        button9.config(text=ai_player)

    if check == 17:
        button3.config(text=ai_player)

    if check == 18:
        button6.config(text=ai_player)

    if check == 19:
        button9.config(text=ai_player)

    if check == 20:
        button1.config(text=ai_player)

    if check == 21:
        button5.config(text=ai_player)

    if check == 22:
        button7.config(text=ai_player)

    if check == 23:
        button3.config(text=ai_player)

    if check == 24:
        button5.config(text=ai_player)

    if check == 25:
        button3.config(text=ai_player)

    if check == 26:
        button1.config(text=ai_player)

    if check == 27:
        button2.config(text=ai_player)

    if check == 28:
        button6.config(text=ai_player)

    if check == 29:
        button4.config(text=ai_player)

    if check == 30:
        button5.config(text=ai_player)

    if check == 31:
        button9.config(text=ai_player)

    if check == 32:
        button7.config(text=ai_player)

    if check == 33:
        button8.config(text=ai_player)

    if check == 34:
        button7.config(text=ai_player)

    if check == 35:
        button1.config(text=ai_player)

    if check == 36:
        button4.config(text=ai_player)

    if check == 37:
        button8.config(text=ai_player)

    if check == 38:
        button2.config(text=ai_player)

    if check == 39:
        button5.config(text=ai_player)

    if check == 40:
        button9.config(text=ai_player)

    if check == 41:
        button3.config(text=ai_player)

    if check == 42:
        button6.config(text=ai_player)

    if check == 43:
        button9.config(text=ai_player)

    if check == 44:
        button1.config(text=ai_player)

    if check == 45:
        button5.config(text=ai_player)

    if check == 46:
        button7.config(text=ai_player)

    if check == 47:
        button3.config(text=ai_player)

    if check == 48:
        button5.config(text=ai_player)


def draw_color():
    button1.config(fg="#5f9ea0")
    button2.config(fg="#5f9ea0")
    button3.config(fg="#5f9ea0")
    button4.config(fg="#5f9ea0")
    button5.config(fg="#5f9ea0")
    button6.config(fg="#5f9ea0")
    button7.config(fg="#5f9ea0")
    button8.config(fg="#5f9ea0")
    button9.config(fg="#5f9ea0")


label1 = tk.Label(window, text="円罰ゲーム", bg=bg_color, fg=fg_color)
label1.pack(pady=10)
# ラベル、行動順
label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=2)
# ラベル、応援
label3 = tk.Label(window, text="スタート！", bg=bg_color, fg=fg_color)
label3.pack(pady=2)
# リセットボタン
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

# 行動順を決める
order_action()

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
