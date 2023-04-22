"""SusaPad's main file"""

import os, sys, pathlib

sys.path.append(
    os.path.dirname(
        pathlib.Path(os.path.realpath(__file__))\
        .parent.absolute()
    )
)

from PySide6 import QtWidgets

from susapad.susa.ui import main_window


def run():
    """Start SusaPad's application"""

    susa_app = QtWidgets.QApplication([])
    susa_window = main_window.MainWindow()
    susa_window.show()
    sys.exit(susa_app.exec())


if __name__ == "__main__":
    run()