import subprocess
import os
import sys
import numpy as np
from moviepy.tools import subprocess_call

def ffmpeg_extarct_subclip_audio(filename, output_path='./', isfolder=False, sr=22050, output_format='wav'):
    """
    Extact Audio files(.WAV) from Video files(.MP4)
    
    filename : 가져올 파일 or 폴더 이름
    output_path : 저장할 경로
    isfolder : 폴더 유무를 판단하는 함수
    sr : sample rate(default : 22050)
    output_format : 출력할 형식
    """
    ffmpeg_path = "D:/ffmpeg-4.2-win64-static/bin/ffmpeg.exe" ## ffmpeg 주소
    saved_path = output_path
    if saved_path[-1] != "/":
        saved_path += "/"
        
    if isfolder:
        file_list = [f for f in os.listdir(filename)]
        command = [[ffmpeg_path, '-y', '-i', filename+file, saved_path + os.path.splitext(file)[0]
                    + '.' + output_format] for file in file_list]
        
    else:     
        command = [ffmpeg_path, '-y', '-i', filename, saved_path + os.path.splitext(filename)[0].split('/')[-1]
                   + '.' + output_format]
    
    for cmd in command:
        try:
            if type(cmd) != list:
                subprocess_call(command)
                return
            
            subprocess_call(cmd)
            print("Convert Completes")
        except OSError:
            print("Don't exist File or Audio in File")
            print("Please check the file")
            return