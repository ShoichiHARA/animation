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
        self.bt0 = tk.Button(self, text="0", command=lambda: change_page(master.sub_page))
        self.bt1 = tk.Button(self, text="1", command=lambda: make_window(master))
        self.bt2 = tk.Button(self, text="2", command=self.bt2.forget)                              # ボタンを押したらボタンを非表示
        self.bt3 = tk.Button(self, text="3", command=self.bt2.pack(anchor="center", expand=True))  # ボタンを押したらボタンを復元
        # self.tenkey = tk.Frame(self)     # テンキーのフレーム
        # self.key0   = tk.Button(tenkey, text="0", width=30, height=10)
        # self.key1   = tk.Button(tenkey, text="1", width=10, height=10)
        # self.key2   = tk.Button(tenkey, text="2", width=10, height=10)
        # self.key3   = tk.Button(tenkey, text="3", width=10, height=10)
        
        # ウィジェットの配置
        self.bt0.pack(anchor="center", expand=True)
        self.bt1.pack(anchor="center", expand=True)
        self.bt2.pack(anchor="center", expand=True)
        self.bt3.pack(anchor="center", expand=True)
        # self.tenkey.place(anchor="center", x=100, y=100)
        # self.key0.place(x=5, y=35)
        # self.key1.place(x=5, y=25)
        # self.key2.place(x=15, y=25)
        # self.key3.place(x=25, y=25)


# サブページクラス
class SubPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg="green")

        # ウィジェットの生成
        # self.label = tk.Label(self, text="SubPage")
        self.bt3 = tk.Button(self, text="3", command=lambda: change_page(master.main_page))

        # ウィジェットの配置
        # self.label.pack(anchor="center", expand=True)
        self.bt3.pack(anchor="se", expand=True)


# サブウインドウクラス
class SubWindow(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.geometry("200x200")
        # self.grid_columnconfigure(0, weight=1)  # ウインドウサイズを変更した場合に行を調整
        # self.grid_rowconfigure(0, weight=1)     # ウインドウサイズを変更した場合に列を調整
        self.configure(bg="blue")
        # self.title("Timer_sub")                 # ウインドウのタイトル
        
        # ウィジェットの生成
        self.label = tk.Label(self, text="SubWindow", bg="blue")

        # ウィジェットの配置
        self.label.pack(anchor="center", expand=True)


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
