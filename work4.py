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
li = []


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    name = entry1.get()  # 入力値を取得
    li.append(name)
    name_list = ""
    for n in li:
        name_list = name_list + "\n" + n

    label1.config(text=f"{name_list}")  # 画面に出力


def button_action2():
    name = entry1.get()
    li.append(name)
    name_ran = random.randint(len(name))
    label2.config(text=f"{name[name_ran]}")


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# 追加ボタンの作成
button1 = tk.Button(window, text="追加する", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="名前を入力してください", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ランダムボタンの作成
button2 = tk.Button(window, text="ランダム選択", command=button_action2)
button2.pack(pady=10)

# 出力ラベルの作成
label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
