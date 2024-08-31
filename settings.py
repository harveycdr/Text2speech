from tkinter import filedialog as fd
from tkinter import messagebox
import requests, json, os, time, random, sys, pygame
from io import BytesIO
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
import base64,json

CURRENT_PATH = os.getcwd()
PATH_FILE_VOICE = CURRENT_PATH + '\\' + "voicefile.ls"

def strStoM(i):
    if i < 60:
        return "00:{:02}:{:03}".format(int(i), int(1000 * (i-int(i))))
    minute = i // 60
    second = i % 60
    mili = int((i - int(i)) * 1000)
    return print("{:02}:{:02}:{:03}".format(minute, second, mili))


def write_dict_voice(voices : dict):
    with open(PATH_FILE_VOICE, mode='w', encoding='utf-8') as wd:
        data_writer = json.dumps(voices)
        wd.write(data_writer)
        wd.close()

def read_dict_voice():
    #Read the voices existing in the data file
    data = {}
    

    try:
        with open(PATH_FILE_VOICE, mode='r', encoding='utf-8') as rd:
            data = json.loads(rd.read())
            rd.close()
        if data.get('voices') is None:
            data = {'voices':[]}
        return data

    except:
        messagebox.showerror("Lỗi đọc file voice", "Dữ liệu bị lỗi")
        if os.path.exists(PATH_FILE_VOICE):
            os.remove(PATH_FILE_VOICE)
        write_dict_voice({'voices':[]})
        return read_dict_voice()
    
def save_binary(filename, bytearr):
    try:
        with open(filename, "wb") as file: 
            file.write(bytearr)
            file.close()
        messagebox.showinfo("Infor", f"Lưu thành công file {filename}")
    except:
        messagebox.showinfo("Infor", f"Lưu file thất bại, file '{filename}' có thể đã tồn tại")
    
