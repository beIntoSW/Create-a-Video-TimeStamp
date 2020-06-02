# Create-a-Video-TimeStamp
TimeStamp extracted using Audio and Face

## 오디오 분류 순서
1. Video파일 -> Audio파일 변환 ( 전체적으로 ) ( 완료 )
> ffmpeg_extarct_subclip_audio 함수 사용
2. 5초 단위로 불러옴 ( 완료 )
> librosa_load 함수 사용 
3. 불러온 데이터 특징 추출
4. 노래라고 인식됬다면? -> 1초씩 확인
5. 특정 조건(ex. 3번이상 노래라고 판별했을 경우)이 만족하면? -> 시간 저장
6. 아니라면? -> 계속 확인 할 것인가? 아니면 뛰어 넘어갈 것인가?
    <br> // 계속 확인한다면, 언제 끝인지 알 것인가?
7. Audio 파일이 끝에 도달하면, 종료 ( 완료 )


