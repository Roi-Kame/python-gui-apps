import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    seireki = int(entry1.get())  # 入力値を取得
    if seireki <= 1867:
        label2.config(text="1868 以上の数字を入力してください")
    elif seireki <= 1911:
        meiji = seireki - 1867
        label2.config(text=f"明治 {meiji} 年です！")  # 画面に出力
    elif seireki <= 1925:
        taisyo = seireki - 1911
        label2.config(text=f"大正 {taisyo} 年です！")
    elif seireki <= 1987:
        syowa = seireki - 1925
        label2.config(text=f"昭和 {syowa} 年です！")
    elif seireki <= 2018:
        heisei = seireki - 1987
        label2.config(text=f"平成 {heisei} 年です！")
    elif seireki >= 2019:
        reiwa = seireki - 2018
        label2.config(text=f"令和 {reiwa} 年です！")
    else:
        label2.config(text="その年は、登録されていません")


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="変換する", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="西暦を入力してください", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
