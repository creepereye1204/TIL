# import os
# import yt_dlp


# def download(url):
#     folder=os.path.join(os.path.dirname(os.path.abspath(__file__)),'youtube')
#     if not os.path.exists(folder):
#         os.makedirs(folder)
#     ydl = yt_dlp.YoutubeDL(
#         {
#             "format": "bestvideo+bestaudio",
#             "merge_output_format": "mp4",
#             "outtmpl": folder+"/%(title)s.%(ext)s",  # 파일 이름을 원래 제목으로 설정
#             "overwrites": True,
#         }
#     )

    
#     if not url.startswith('https://'):
#         url = 'https://www.youtube.com/watch?v=' + url
#     ydl.extract_info(url, download=False)
#     ydl.download([url])
import os
import yt_dlp

def download(url):
    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'youtube')
    if not os.path.exists(folder):
        os.makedirs(folder)
    ydl = yt_dlp.YoutubeDL(
        {
            "format": "bestaudio",  # 오디오만 다운로드
            "outtmpl": folder + "/%(title)s.%(ext)s",  # 파일 이름을 원래 제목으로 설정
            
            "overwrites": True
        }
    )

    # if not url.startswith('https://www.youtube.com/watch?v='):
    #     return
    ydl.extract_info(url, download=False)
    ydl.download([url])
