import librosa

def librosa_load(filename, offset = 0.0, duration = 5.0, sr=22050):
    """
    원하는 길이만큼 잘라서 가져오기 위한 함수
    return : 데이터, 시작점
        
    filename : 가져올 파일 이름
    offset : 시작 지점(sec)
    duration : 가져올 길이(sec)
    sr : sample rate(default : 22050)
    """
    try:
        X, sample_rate = librosa.load(filename, offset=offset, duration=duration, sr=sr, res_type='kaiser_best')
    
        if X.size / sr < duration:
            print("Arrive at the end of file")
            return False, offset
        else:
            return X, offset
    except:
        print("Offset is bigger than Length")
        return False, offset
    
