import sys
from PySide6.QtWidgets import QApplication, QWidget 


def main ():
    try:
        app = QApplication(sys.argv)
        myWindow = QWidget()
        myWindow.setWindowTitle("My Window")
        myWindow.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Exception : {e}")

if __name__ == "__main__":
    main()

