import tkinter as tk
import time
import threading
import pystray
from PIL import Image, ImageDraw

# 현재 시간을 업데이트하는 함수
def update_time(label):
    while True:
        current_time = time.strftime('%H:%M:%S')
        label.config(text=current_time)  # 레이블의 텍스트를 현재 시간으로 업데이트
        time.sleep(1)  # 1초마다 업데이트

# 드래그를 위한 변수
dragging = False
drag_start_x = 0
drag_start_y = 0

def on_drag_start(event):
    global dragging, drag_start_x, drag_start_y
    dragging = True
    drag_start_x = event.x
    drag_start_y = event.y

def on_drag_motion(event):
    global dragging
    if dragging:
        x = root.winfo_x() + (event.x - drag_start_x)
        y = root.winfo_y() + (event.y - drag_start_y)
        root.geometry(f"+{x}+{y}")

def on_drag_end(event):
    global dragging
    dragging = False

# GUI 창을 여는 함수
def open_window():
    global root
    root = tk.Tk()
    root.title("시계 위젯")

    # 투명한 배경 설정
    root.overrideredirect(True)  # 메뉴 바와 제목 표시줄을 숨김
    root.wm_attributes("-alpha", 0.8)  # 배경 투명도 설정 (0.0 ~ 1.0)
    root.wm_attributes("-transparentcolor", "white")  # 투명 색상 설정

    # 레이블 생성
    label = tk.Label(root, font=("Helvetica", 48), fg="black", bg="white")  # 배경을 흰색으로 설정
    label.pack()

    # 시간 업데이트 스레드 시작
    threading.Thread(target=update_time, args=(label,), daemon=True).start()

    # 드래그 이벤트 바인딩
    root.bind("<Button-1>", on_drag_start)
    root.bind("<B1-Motion>", on_drag_motion)
    root.bind("<ButtonRelease-1>", on_drag_end)

    # GUI 실행
    root.mainloop()

# 아이콘 이미지를 생성하는 함수
def create_image():
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), (255, 255, 255))
    dc = ImageDraw.Draw(image)

    # 아이콘에 시계 표시
    dc.ellipse((0, 0, width, height), fill=(0, 0, 0))
    return image

# 프로그램 종료
def exit_action(icon, item):
    icon.stop()  # 아이콘 종료
    if root is not None:
        root.destroy()  # GUI 종료

# 트레이 아이콘 클릭 이벤트
def on_icon_click(icon, item):
    open_window()  # GUI 창 열기

# 메인 함수
def main():
    global root
    root = None  # 전역 변수로 GUI 창을 관리

    # 시스템 트레이 아이콘 설정
    icon = pystray.Icon("Clock")
    icon.icon = create_image()
    icon.title = "시계"
    icon.menu = pystray.Menu(
        pystray.MenuItem("Open", on_icon_click),  # 아이콘 클릭 시 GUI 열기
        pystray.MenuItem("Exit", exit_action)  # 종료 메뉴
    )

    # 트레이 아이콘 실행
    icon.run()

if __name__ == "__main__":
    main()
