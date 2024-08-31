from settings import *
from fpt_api_voice import *

class App:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Text To Speech Python")
        self.root.geometry("700x400")
        self.root.resizable(False, False)

        self.frame = tk.Frame(self.root, background="#eeeeee")
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.initialize()

    def initialize(self):


        self.lb1 = tk.Label(self.frame, anchor=tk.W, text="Name speech:", font="Consolas 12")
        self.entry1 = tk.Entry(self.frame, font="Consolas 15")
        self.lb2 = tk.Label(self.frame, text=".mp3", font="Consolas 12")
        self.lb3 = tk.Label(self.frame, text="Save Dir",font="Consolas 12")
        
        self.cur_path = CURRENT_PATH
        self.lb_dir = tk.Label(self.frame, text=CURRENT_PATH.split('\\')[-1], font="Consolas 12")

        self.btn_browse = tk.Button(self.frame, text= "Browse", font="Consolas 12")
        self.lb4 = tk.Label(self.frame, anchor=tk.W, text="Input:",font="Consolas 12")
        self.lb_char = tk.Label(self.frame, anchor=tk.W, text="Char: 0",font="Consolas 12")
        self.lb5 = tk.Label(self.frame, text="Voice",font="Consolas 12")

        self.voices = ["banmai", "thuminh", "myan", "giahuy", "ngoclam", "leminh", "minhquang", "linhsan", "lannhi"]
        voices = ["Ban Mai","Thu Minh","Mỹ An", "Gia Huy", "Ngọc Lam", "Lê Minh", "Minh Quang", "Linh San", "Lan Nhi"]
        self.cbb_voice = ttk.Combobox(self.frame, values=voices, font="Consolas 10")
        self.cbb_voice.current(0)

        self.lb6 = tk.Label(self.frame, text="Speed",font="Consolas 12")

        self.speeds = ["+3", "+2", "+1", "0", "-1", "-2", "-3"]
        speeds = ["+3 (faster)", "+2", "+1", "0 (normal)", "-1", "-2", "-3 (lower)"]
        self.cbb_speed = ttk.Combobox(self.frame, values=speeds, font="Consolas 10")
        self.cbb_speed.current(3)

        self.lb7 = tk.Label(self.frame, text="Key:",font="Consolas 12")

        keys = [i["name"] for i in fpt_api_voice()]
        self.keys = [i["token"] for i in fpt_api_voice()]
        self.cbb_key = ttk.Combobox(self.frame, values=keys, font="Consolas 10")
        self.cbb_key.current(0)

        self.entry_text = tk.Text(self.frame, font="Consolas 15")

        self.btn_stt = tk.Button(self.frame, text="Convert", font="Consolas 15")

        self.lb8 = tk.Label(self.frame, text="List voice", anchor=tk.W, font="Consolas 15")
        self.lb9 = tk.Label(self.frame, text="run: ", anchor=tk.W, font="Consolas 10")

        self.btn_play = tk.Button(self.frame, text="Play", font="Consolas 12")
        self.mp3_time_play = 0

        self.list_mp3 = tk.Listbox(self.frame, font="Consolas 15")

        self.btn_delete = tk.Button(self.frame, text="Delete", font="Consolas 15")

        self.btn_save = tk.Button(self.frame, text="Save", font="Consolas 15")
        self.btn_save_all = tk.Button(self.frame, text="Save all", font="Consolas 15")

        self.play_slider = ttk.Scale(self.frame, from_=0, to=100, orient=tk.HORIZONTAL, value=0)
        self.play_time = tk.Label(self.frame, text="00:00:00", anchor=tk.W, font="Consolas 8")


        self.lb1.place(relwidth=0.2, relheight=0.1, relx=0, rely=0)
        self.entry1.place(relwidth=0.2, relx=0.2, rely=0.02)
        self.lb2.place(relwidth=0.1, relheight=0.1, relx=0.4, rely=0)
        self.lb3.place(relwidth=0.15, relheight=0.1, relx=0.5, rely=0)
        self.lb_dir.place(relwidth=0.2, relheight=0.1, relx=0.65, rely=0)
        self.btn_browse.place(relwidth=0.13, relheight=0.1, relx=0.85, rely=0)
        self.lb4.place(relwidth=0.1, relheight=0.1, relx=0, rely=0.1)
        self.lb_char.place(relwidth=0.2, relheight=0.1, relx=0.1, rely=0.1)
        self.lb5.place(relwidth=0.1, relheight=0.1, relx=0.3, rely=0.1)
        self.cbb_voice.place(relwidth=0.15, relx=0.4, rely=0.12)
        self.lb6.place(relwidth=0.1, relheight=0.1, relx=0.55, rely=0.1)
        self.cbb_speed.place(relwidth=0.1, relx=0.65, rely=0.12)
        self.lb7.place(relwidth=0.1, relheight=0.1, relx=0.75, rely=0.1)
        self.cbb_key.place(relwidth=0.13, relx=0.85, rely=0.12)
        self.entry_text.place(relwidth=0.5, relheight=0.74, relx=0.02, rely=0.22)
        self.btn_stt.place(relwidth=0.13, relheight=0.1, relx=0.53, rely=0.22)
        self.lb8.place(relwidth=0.2, relheight=0.1, relx=0.53, rely=0.32)
        self.lb9.place(relwidth=0.2, relheight=0.08, relx=0.83, rely=0.33)
        self.list_mp3.place(relwidth=0.28, relheight=0.54, relx=0.53, rely=0.42)
        self.btn_play.place(relwidth=0.08, relheight=0.08, relx=0.73, rely=0.33)
        self.btn_delete.place(relwidth=0.15, relheight=0.1, relx=0.83, rely=0.42)
        self.btn_save.place(relwidth=0.15, relheight=0.1, relx=0.83, rely=0.70)
        self.btn_save_all.place(relwidth=0.15, relheight=0.1, relx=0.83, rely=0.82)
        self.play_slider.place(relwidth=0.22, relheight=0.1, relx=0.68, rely=0.22)
        self.play_time.place(relwidth=0.1, relheight=0.1, relx=0.9, rely=0.22)

    def mainloop(self):
        self.root.mainloop()

