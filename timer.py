import tkinter as tk

test = False


# メインページクラス
class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg="white")

        self.bt0 = tk.Button(self, text="0", command=lambda: change_page(master.sub_page))
        self.bt0.pack(anchor="center", expand=True)

        self.bt1 = tk.Button(self, text="1", command=lambda: make_window(master))
        self.bt1.pack(anchor="center", expand=True)


# サブページクラス
class SubPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg="green")

        # self.label = tk.Label(self, text="SubPage")
        # self.label.pack(anchor="center", expand=True)

        self.bt2 = tk.Button(self, text="2", command=lambda: change_page(master.main_page))
        self.bt2.pack(anchor="se", expand=True)


# サブウインドウクラス
class SubWindow(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.geometry("200x200")
        self.configure(bg="blue")

        self.label = tk.Label(self, text="SubWindow", bg="blue")
        self.label.pack(anchor="center", expand=True)


# アプリケーションクラス
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("400x400")
        self.grid_columnconfigure(0, weight=1)  # 行の設定
        self.grid_rowconfigure(0, weight=1)     # 列の設定
        self.title("Timer")

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
