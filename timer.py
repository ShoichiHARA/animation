# 参考ページ
# フレームの使い方　　　　　　　　　：https://office54.net/python/tkinter/python-tkinter-frame
# 要素の配置の指定方法　　　　　　　：https://daeudaeu.com/tkinter_place/
# ウインドウサイズの変更で要素も変更：https://python.keicode.com/advanced/tkinter-grid.php
# 描画　　　　　　　　　　　　　　　：https://daeudaeu.com/tkinter_canvas_draw/

import tkinter as tk

test = False


# メインページクラス
class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg="white")

        # ウィジェットの生成
        self.label = tk.Label(self, text="mainPage")
        self.bt0 = tk.Button(self, text="0", command=lambda: change_page(master.sub_page))
        self.bt1 = tk.Button(self, text="1", command=lambda: make_window(master))
        # self.bt2 = tk.Button(self, text="2", command=self.bt2.forget)                              # ボタンを押したらボタンを非表示
        # self.bt3 = tk.Button(self, text="3", command=self.bt2.pack(anchor="center", expand=True))  # ボタンを押したらボタンを復元
        self.tenkey = tk.Frame(self, width=130, height=170, bd=1)     # テンキーのフレーム
        self.key0   = tk.Button(self.tenkey, text="0")
        self.key1   = tk.Button(self.tenkey, text="1")
        self.key2   = tk.Button(self.tenkey, text="2")
        self.key3   = tk.Button(self.tenkey, text="3")
        self.key4   = tk.Button(self.tenkey, text="4")
        self.key5   = tk.Button(self.tenkey, text="5")
        self.key6   = tk.Button(self.tenkey, text="6")
        self.key7   = tk.Button(self.tenkey, text="7")
        self.key8   = tk.Button(self.tenkey, text="8")
        self.key9   = tk.Button(self.tenkey, text="9")
        
        # ウィジェットの配置
        self.label.pack(anchor="center", expand=True)
        self.bt0.pack(anchor="center", expand=True)  # expand=True：ウインドウサイズの変更で要素の位置も変更
        self.bt1.pack(anchor="center", expand=True)
        # self.bt2.pack(anchor="center", expand=True)
        # self.bt3.pack(anchor="center", expand=True)
        self.tenkey.pack(anchor="center")
        self.key0.place(x=5, y=125, width=120, height=40)
        self.key1.place(x=5, y=85, width=40, height=40)
        self.key2.place(x=45, y=85, width=40, height=40)
        self.key3.place(x=85, y=85, width=40, height=40)
        self.key4.place(x=5, y=45, width=40, height=40)
        self.key5.place(x=45, y=45, width=40, height=40)
        self.key6.place(x=85, y=45, width=40, height=40)
        self.key7.place(x=5, y=5, width=40, height=40)
        self.key8.place(x=45, y=5, width=40, height=40)
        self.key9.place(x=85, y=5, width=40, height=40)


# サブページクラス
class SubPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg="green")

        # ウィジェットの生成
        self.label = tk.Label(self, text="SubPage")
        self.bt3 = tk.Button(self, text="3", command=lambda: change_page(master.main_page))

        # ウィジェットの配置
        self.label.place(x=5, y=5)
        self.bt3.pack(anchor="se", expand=True)


# サブウインドウクラス
class SubWindow(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.geometry("200x200")
        self.grid_columnconfigure(0, weight=1)  # ウインドウサイズを変更した場合に行を調整
        self.grid_rowconfigure(0, weight=1)     # ウインドウサイズを変更した場合に列を調整
        self.configure(bg="blue")
        self.title("Timer_sub")                 # ウインドウのタイトル
        
        # ウィジェットの生成
        # self.label = tk.Label(self, text="SubWindow", bg="blue")
        self.canvas = tk.Canvas(self, width=200, height=200, bg="white")

        # ウィジェットの配置
        # self.label.pack(anchor="center", expand=True)
        self.canvas.pack(expand=True)

        # キャンバスへの描画
        self.seg1a = self.canvas.create_polygon(100, 50, 50, 150, 150, 150, fill="", outline="black")
        self.seg1b = self.canvas.create_polygon(100, 75, 50, 175, 150, 175, fill="", outline="green")


# アプリケーションクラス
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("400x400")
        # self.resizable(False, False)            # ウインドウサイズの固定
        self.grid_columnconfigure(0, weight=1)  # ウインドウサイズを変更した場合に行を調整
        self.grid_rowconfigure(0, weight=1)     # ウインドウサイズを変更した場合に列を調整
        self.title("Timer_main")

        # メインページ
        self.main_page = MainPage(self)
        self.main_page.grid(row=0, column=0, sticky="nsew")

        # サブページ
        self.sub_page = SubPage(self)
        self.sub_page.grid(row=0, column=0, sticky="nsew")

        self.main_page.tkraise()


# ページの移動
def change_page(page):
    page.tkraise()


# 新しいウインドウの生成
def make_window(master):
    sub_window = SubWindow(master)


if __name__ == "__main__":
    # アプリケーションの開始
    app = App()
    app.mainloop()
