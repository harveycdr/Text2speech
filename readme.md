## Overview

Xây dựng chương trình Text to speech bằng sử dụng api của fptai

Sử dụng ngôn ngữ python thư viện mixer pygame và tkinter xây dựng game

+ Chương trình để tiết kiệm thời gian tạo file mp3 giọng nói
sử dụng api từ fptai phát triển.

## Text2Speech

Trò chơi ghép hình cơ bản

Video demo: https://drive.google.com/file/d/1rbqQ9q3bT2wmwSK772yZQkn9WCrCWEnd/view

## Installation

Nếu bạn chưa cài đặt Python, bạn có thể tải về từ trang chính thức của Python theo đường dẫn: [Python.org](https://www.python.org/downloads/).

Kiểm tra xem Python đã được cài đặt thành công bằng cách chạy các lệnh sau trong terminal:

```shell
# Kiểm tra phiên bản
python --version

#  Clone git repository
git clone https://github.com/harveycdr/Text2speech.git

# Cài đặt

pip install tkinter
pip install pygame
pip install requests, json

```

## Configuration

Tại file fpt_api_voice.py thay đổi:

TOKEN_API_1 -> token api của tài khoản 
TOKEN_API_2 -> token api của tài khoản 
TOKEN_API_3 -> token api của tài khoản 

Để có thể sử dụng


## Demo chương trình python

```shell
#chạy chương trình
python app.py


```
#Ảnh trong chương trình
<img src="https://github.com/harveycdr/Text2speech/blob/root/Screenshot2024-08-31211549.png" alt="Ảnh chương trình" >

## Mô tả 

Chương trình được viết bằng ngôn ngữ python 

Xây dựng giao diện từ thư viện lập trình phổ biến giao diện tkinter

Chương trình nhằm mục đích học tập cách dùng và gọi api từ đó giúp tối ưu thời gian trong việc tạo giọng đọc

file dữ liệu sẽ được lưu dạng link mp3 (Link này sẽ bị xóa sau một khoản thời gian) từ fpt cung cấp, có thể tải về thành file mp3.