from app_design import App
from settings import *

pygame.mixer.init()
def play_mp3_from_url(url):
    print("playing: " + url)
    try:
        global sound

        audio_data = requests.get(url).content
        pygame.mixer.music.load(BytesIO(audio_data))
        sound = pygame.mixer.Sound(BytesIO(audio_data))
        return sound.get_length()
        
    except Exception as Ex:
        print(Ex)
        messagebox.showerror("Error", "Xảy ra lỗi trong quá trình đọc file mp3")
        return 0

def TextToSpeech(obj:App):
    index_api_key = obj.cbb_key.current()
    api_key = obj.keys[index_api_key]

    index_api_speed = obj.cbb_speed.current()
    api_speed = obj.speeds[index_api_speed]

    index_api_voice = obj.cbb_voice.current()
    api_voice = obj.voices[index_api_voice]
    txt = obj.entry_text.get("1.0", tk.END)
    if len(txt) < 10:
        messagebox.showinfo("Infor", "Hãy nhập từ 10 ký tự trở lên")
        return
    elif len(txt) > 5000:
        messagebox.showinfo("Infor", "Không được nhập quá 5000 ký tự")
        return

    url = 'https://api.fpt.ai/hmi/tts/v5'

    payload = txt[:-1]
    headers = {
        'api-key': api_key,
        'speed': api_speed,
        'voice': api_voice
    }
    response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)
    response = json.loads(response.text)
    messagebox.showinfo("Infor","Nhận được phản hồi")
    print(response)

    if response['error'] != 0:
        messagebox.showerror("Error", response['message'])
        return
    
    voices = read_dict_voice()
    val = {"name":"voice_{0}".format(len(voices['voices']) + 1), "url": response['async']}
    voices['voices'].append(val)
    write_dict_voice(voices)
    Load_list_mp3(obj)

def loop_play(obj:App):
    time_loop = int(obj.mp3_time_play * 10)
    val = obj.play_slider.get()
    if val < obj.play_slider.cget('to'):
        obj.play_slider.set(val + 1)
        obj.play_slider.after(time_loop, lambda:loop_play(obj))

def Play_mp3(obj:App):
    try:
        sel = obj.list_mp3.curselection()[0]
        url = read_dict_voice()['voices'][sel]['url']
        obj.mp3_time_play = play_mp3_from_url(url)
        obj.play_time['text'] = strStoM(obj.mp3_time_play)
        
        pygame.mixer.music.play()
        obj.play_slider.set(0)
        loop_play(obj)

    except Exception as ex:
        print(ex)
        pass

def Play_SliderUp(e:tk.Event, obj:App):
    tl = int(float(obj.play_slider.get()))
    start_in = tl * obj.mp3_time_play / 100 #second
    # start_in = start_in*1000 #millisecond
    print(start_in)
    pygame.mixer.music.play(start=start_in)
    loop_play(obj)

def browse_dir(obj:App):
    select_path = fd.askdirectory(initialdir=obj.cur_path).replace('/', '\\')

    if not select_path:
        select_path = obj.cur_path
    obj.lb_dir['text'] = "\\" + select_path.split('\\')[-1]

    obj.cur_path = select_path
    Load_list_mp3(obj)

def OnKeyClick(event:tk.Event, obj:App):
    #Count all char
    char = obj.entry_text.get("1.0", tk.END)[:-1]
    obj.lb_char["text"] = "Char: {0}".format(len(char))

def Load_list_mp3(obj:App):
    obj.list_mp3.delete(0, tk.END)
    data_mp3 = read_dict_voice()['voices']
    for voice in data_mp3:
        obj.list_mp3.insert(tk.END, voice['name'])

def on_select(e: tk.Event, obj:App):
    obj.lb9['text'] = "run: " + obj.list_mp3.selection_get()

def is_name_save(obj:App):
    name_voice = obj.entry1.get()

    if len(name_voice) == 0:
        return False
    return True

def count_same_name(path, name):
    count = 0
    try:
        for i in os.listdir(path):
            if name in os.path.splitext(i)[0]:
                count += 1
    except:
        messagebox.showerror("Error", "Lỗi đặt tên file")
    return count

def Delete_voice(obj:App):
    data_mp3 = read_dict_voice()
    sel = obj.list_mp3.curselection()[0]
    print("Delete", data_mp3['voices'][sel])
    data_mp3['voices'].pop(sel)
    write_dict_voice(data_mp3)
    Load_list_mp3(obj)

def Save_voice(obj:App):
    if not is_name_save(obj):
        messagebox.showinfo("Infor", "Hãy nhập tên cho file âm thanh")
        return
    
    name_mp3 = obj.cur_path + '\\' + obj.entry1.get() + ".mp3"
    sel = obj.list_mp3.curselection()[0]
    url = read_dict_voice()['voices'][sel]['url']
    audio_data = requests.get(url).content
    save_binary(name_mp3, audio_data)
    

def Save_all_voice(obj:App):
    if not is_name_save(obj):
        messagebox.showinfo("Infor", "Hãy nhập tên cho file âm thanh")
        return
    n = obj.entry1.get()
    c = count_same_name(obj.cur_path, n)
    i = 0
    for voice in read_dict_voice()['voices']:
        url = voice['url']
        audio_data = requests.get(url).content
        name_mp3 = obj.cur_path + '\\' + n + f"{c+i}.mp3"
        save_binary(name_mp3, audio_data)
        i += 1

if __name__ == "__main__":
    app = App()

    #Browsing the folder to save mp3 files
    app.btn_browse['command'] = lambda:browse_dir(app)

    #Event of pressing a key on the keyboard
    app.entry_text.bind("<KeyPress>", lambda e: OnKeyClick(e, app))
    
    #Convert text2speech
    app.btn_stt['command'] = lambda:TextToSpeech(app)

    #playing mp3 file
    app.btn_play['command'] = lambda:Play_mp3(app)

    # app.play_slider['command'] = lambda e: Play_SliderDown(e, app)
    
    app.play_slider.bind("<ButtonRelease-1>", lambda e: Play_SliderUp(e, app))
    
    #Display the selected voice
    app.list_mp3.bind("<<ListboxSelect>>", lambda e: on_select(e, app))
    
    app.btn_delete['command'] = lambda:Delete_voice(app)
    app.btn_save['command'] = lambda:Save_voice(app)
    app.btn_save_all['command'] = lambda:Save_all_voice(app)
    Load_list_mp3(app)
    app.mainloop()

