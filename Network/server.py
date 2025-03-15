import toga
from toga.style import Pack
from toga.widgets.box import Box
from toga.widgets.canvas import Canvas
from toga.widgets.button import Button
from toga.widgets.webview import WebView
import requests

class MyApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title="Drawing App", size=(800, 800))

        # 웹뷰 생성
        self.webview = WebView(url="https://blog.naver.com/goglkms/222088521207", style=Pack(flex=1))

        # 캔버스 생성
        self.canvas = Canvas(style=Pack(flex=1))
        self.canvas.on_mouse_down = self.on_mouse_down
        self.canvas.on_mouse_move = self.on_mouse_move
        self.canvas.on_mouse_up = self.on_mouse_up

        # 버튼 생성
        fetch_html_button = Button("Fetch HTML", on_press=self.fetch_html, style=Pack(padding=10))
        clear_button = Button("Clear Canvas", on_press=self.clear_canvas, style=Pack(padding=10))

        # 레이아웃 설정
        box = Box(direction='column')
        box.add(self.webview)
        box.add(self.canvas)
        box.add(fetch_html_button)
        box.add(clear_button)

        self.main_window.content = box

        self.drawing = False
        self.last_x = 0
        self.last_y = 0

        self.main_window.show()

    def fetch_html(self, widget):
        url = "https://blog.naver.com/goglkms/222088521207"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                html_content = response.text
                print(html_content)  # HTML 내용을 출력합니다. 필요에 따라 처리할 수 있습니다.
            else:
                print(f"Error fetching HTML: {response.status_code}")
        except Exception as e:
            print(f"Exception occurred: {str(e)}")

    def on_mouse_down(self, widget, x, y):
        self.drawing = True
        self.last_x = x
        self.last_y = y

    def on_mouse_move(self, widget, x, y):
        if self.drawing:
            self.canvas.draw_line(self.last_x, self.last_y, x, y, color=(0, 0, 0, 1), width=2)
            self.last_x = x
            self.last_y = y

    def on_mouse_up(self, widget, x, y):
        self.drawing = False

    def clear_canvas(self, widget):
        self.canvas.clear()

def main():
    return MyApp('Drawing App', 'org.beeware.drawingapp')

if __name__ == "__main__":
    app = main()
    app.main_loop()
