import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout


class MyLayoutWidget(QWidget):
    def __init__(self):
        super().__init__()

        # define the layouts here
        self.vBox = QVBoxLayout()

        self.setWindowTitle("My Layout Widget")
        self.setStyleSheet("background-color:#f045e0")
        self.setLayout(self.vBox)


def main():
    try :
        app = QApplication(sys.argv)
        window = MyLayoutWidget()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Exception : {e}")
    except NameError as name_error:
        print(f"Name Error : {name_error}")


if __name__ == "__main__":
    main()
