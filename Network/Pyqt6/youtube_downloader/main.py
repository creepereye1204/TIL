import os
import sys
import threading
from util import download  # 다운로드 함수를 가져옵니다.
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QSystemTrayIcon, QMenu, QApplication


class DownloaderWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint |
                            QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_NoSystemBackground)

        # 레이블 생성
        self.label = QLabel("다운로드할 URL을 입력하세요:", self)
        self.label.setFont(QtGui.QFont("Helvetica", 16))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # URL 입력 필드
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("URL을 입력하세요...")

        # 다운로드 버튼
        self.download_button = QPushButton("다운로드", self)
        self.download_button.clicked.connect(self.download_file)

        # 레이아웃 설정
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.download_button)
        self.setLayout(layout)

        # 드래그 이벤트 설정
        self.startPos = None
        self.setMouseTracking(True)

    def download_file(self):
        url = self.url_input.text()
        if url:
            threading.Thread(target=self.download_url,
                             args=(url,), daemon=True).start()

    def download_url(self, url):
        try:
            # 사용자 정의 다운로드 함수 호출
            download(url)  # download 함수가 파일명을 반환한다고 가정

            self.label.setText("다운로드 완료!")

        except Exception as e:
            self.label.setText(f"오류 발생: {str(e)}")

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.startPos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if self.startPos is not None:
            self.move(event.globalPosition().toPoint() - self.startPos)

    def mouseReleaseEvent(self, event):
        self.startPos = None


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self):
        super().__init__()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, 'clock_icon.png')
        self.setIcon(QtGui.QIcon(icon_path))
        self.setVisible(True)
        self.is_activated = False

        # 메뉴 설정
        menu = QMenu()
        open_action = menu.addAction("Open Downloader")
        open_action.triggered.connect(self.open_downloader_widget)
        exit_action = menu.addAction("Exit")
        exit_action.triggered.connect(QApplication.instance().quit)
        self.setContextMenu(menu)

        # 클릭 이벤트 설정
        self.activated.connect(self.on_activated)

    def on_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.open_downloader_widget()

    def open_downloader_widget(self):
        if not self.is_activated:
            self.is_activated = True
            self.downloader_widget = DownloaderWidget()
            self.downloader_widget.show()


def main():
    app = QApplication(sys.argv)
    tray_icon = SystemTrayIcon()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
