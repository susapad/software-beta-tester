from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from susapad.susa.ui import alert_dialog


def in_percent(value: int) -> str:
        return f"{((value - 10) / 3.9):0.1f}%"

class PressSensibilitySlider(QtWidgets.QSlider):

    def __init__(self, window, susapad, forms):
        super().__init__()

        self.susapad = susapad
        self.forms = forms
        self.window = window

        self.setMinimumWidth(330)
        self.setMinimum(10)
        self.setMaximum(400)
        self.setOrientation(Qt.Horizontal)

        self.sliderReleased.connect(self.action)
        self.valueChanged.connect(self.update_label)

    def __raise_alert(self):
        alert = alert_dialog.AlertDialog(self.window)
        alert.show()
        self.window.close()

    @QtCore.Slot()
    def action(self):
        if not self.susapad.set_press_sensibility(self.value()):
            self.__raise_alert()

    @QtCore.Slot()
    def update_label(self):
        press = in_percent(self.value())
        release = in_percent(self.forms.sensibility_slider_release.value())
        self.forms.sensibility_label.setText(
            f"Sensibilidade: Pressionar ({press}) e Soltar ({release})"
        )


class ReleaseSensibilitySlider(QtWidgets.QSlider):

    def __init__(self, window, susapad, forms):
        super().__init__()

        self.susapad = susapad
        self.forms = forms
        self.window = window

        self.setMinimumWidth(330)
        self.setMinimum(10)
        self.setMaximum(400)
        self.setOrientation(Qt.Horizontal)

        self.sliderReleased.connect(self.action)
        self.valueChanged.connect(self.update_label)

    def __raise_alert(self):
        alert = alert_dialog.AlertDialog(self.window)
        alert.show()
        self.window.close()

    @QtCore.Slot()
    def action(self):
        if not self.susapad.set_release_sensibility(self.value()):
            self.__raise_alert()

    @QtCore.Slot()
    def update_label(self):
        release = in_percent(self.value())
        press = in_percent(self.forms.sensibility_slider_press.value())
        self.forms.sensibility_label.setText(
            f"Sensibilidade: Pressionar ({press}) e Soltar ({release})"
        )
