from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QHBoxLayout
import os, sys

class RainyBAG(QMainWindow):
    def __init__(self, db_path):
        super().__init__()
        self.db_path = db_path
        self._setup_ui()
        # self._setup_menu()
        # self.bind_signals()
        self._display_ui()
        self.setStyleSheet(open(os.path.join("assets", "styles", "default.css")).read())

    def _setup_ui(self):
        self.window_frame = QFrame()
        self.window_frame.setLayout(QHBoxLayout())
        # self.window_frame.layout().setContentsMargins(0, 0, 0, 0)
        self.setFixedSize(300, 300)
        self.setWindowTitle("RainyBAG")
        

    def bind_signals(self):
        pass

    def _display_ui(self):
        self.setCentralWidget(self.window_frame)


def open_rainy_bag():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    form = RainyBAG(os.path.join(os.getcwd(), 'RainyDB'))  # We set the form to be our ExampleApp (design)

    form.show()  # Show the form
    sys.exit(app.exec_())  # and execute the app


if __name__ == "__main__":
    open_rainy_bag()