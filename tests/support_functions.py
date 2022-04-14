import os
import sys

from PyQt5.QtWidgets import QApplication

from RainyBG import RainyBG


def _setup(qtbot):
    if os.getcwd().endswith("tests"):
        os.chdir("..")
    bg = RainyBG(
        db_path=os.path.join(os.getcwd(), 'RainyDB'),
        template_path=os.path.join(os.getcwd(), 'tests', 'templates')
    )
    qtbot.addWidget(bg)
    return bg


def _show_frame(widget):
    app = QApplication(sys.argv)
    widget.show()
    app.exec_()
