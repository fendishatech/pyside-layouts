import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout , QHBoxLayout, QLabel


class MainWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Horizontal and Vertical Boxes")

        # define hbox widget and layout
        self.hBoxWidget=QWidget()
        self.hBoxWidget_layout = QVBoxLayout()
        self.hBoxWidget.setLayout(self.hBoxWidget_layout)
        self.hBoxWidget.setStyleSheet("background-color: #f0f056;")

         # define vbox widget and layout
        self.vBoxWidget=QWidget()
        self.vBoxWidget_layout = QVBoxLayout()
        self.vBoxWidget.setLayout(self.vBoxWidget_layout)
        self.vBoxWidget.setStyleSheet("background-color: #f056f0;")

        # Main widget and main layout
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.hBoxWidget)
        self.main_layout.addWidget(self.vBoxWidget)

        # set layout to widget
        self.setLayout(self.main_layout)

def main ():
    try:
        app = QApplication(sys.argv)
        myWindow = MainWidget()
        myWindow.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Exception : {e}")

if __name__ == "__main__":
    main()

