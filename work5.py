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
str_list = [
    "今日はいい天気",
    "私はいい人",
    "誰もが迷惑する",
    "私は偽善者",
    "水が澄んでいる",
    "許されない",
    "明日はきっといい日に",
    "考えるだけ動かない",
    "馬鹿な自分",
]


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    user_input = entry1.get()
    count = len(str_list)
    ram = random.randrange(count)
    ram_list = str_list[ram]
    if label1.cget("text") == user_input:
        label1.config(text=f"{ram_list}")
        str_list.pop(ram)
        entry1.delete(0, 10)
    if count == 1:
        label1.config(text="clear！おめでとう")


# 出力ラベルの作成
label1 = tk.Label(
    window,
    text="スタート",
    bg=bg_color,
    fg=fg_color,
)
label1.pack(pady=10)

# 入力フィールドの作成
entry1 = tk.Entry(window, text="", bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="がんばって", command=button_action)
button1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
