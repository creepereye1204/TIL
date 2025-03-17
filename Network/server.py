import os
import sys
import time
import yt_dlp
import threading
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QLabel, QSystemTrayIcon, QMenu, QApplication

class ClockWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
    
 
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_NoSystemBackground)

        # 레이블 생성
        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Helvetica", 48))

        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # 레이아웃 설정
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # 시간 업데이트 스레드 시작
        threading.Thread(target=self.update_time, daemon=True).start()

        # 드래그 이벤트 설정
        self.startPos = None
        self.setMouseTracking(True)

    def update_time(self):
        while True:
            current_time = time.strftime('%H:%M:%S')
            self.label.setText(current_time)  # 레이블의 텍스트를 현재 시간으로 업데이트
            time.sleep(1)  # 1초마다 업데이트

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            # QPoint로 변환하여 연산
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

        # 아이콘 파일 경로 생성
        icon_path = os.path.join(current_dir, 'clock_icon.png')
        self.setIcon(QtGui.QIcon(icon_path))  # 아이콘 설정
        self.setVisible(True)
        self.is_activated=False
        # 메뉴 설정
        menu = QMenu()
        open_action = menu.addAction("Open")
        open_action.triggered.connect(self.open_clock_widget)
        exit_action = menu.addAction("Exit")
        exit_action.triggered.connect(QApplication.instance().quit)
        self.setContextMenu(menu)

        # 클릭 이벤트 설정
        self.activated.connect(self.on_activated)

    def on_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.open_clock_widget()

    def open_clock_widget(self):
        if not self.is_activated:
            self.is_activated=True
            self.clock_widget = ClockWidget()
            self.clock_widget.show()


def main():
    app = QApplication(sys.argv)
    tray_icon = SystemTrayIcon()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
