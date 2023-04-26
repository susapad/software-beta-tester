from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from . import actuation_point, togglers, sensibility


class FormsGroup(QtWidgets.QWidget):

    def __init__(self, window, susapad):
        super().__init__()

        self.first_h2 = QtWidgets.QLabel("Rapid Trigger")
        self.first_h2.setObjectName("first-h2")

        self.rt_button = togglers.RapidTriggerButton(window, susapad)
        self.crt_button = togglers.ContinuousRapidTriggerButton(window, susapad)

        self.sensibility_slider_press = sensibility.PressSensibilitySlider(window, susapad, self)
        self.sensibility_slider_release = sensibility.ReleaseSensibilitySlider(window, susapad, self)
        
        self.actuation_slider_lower = actuation_point.LowerActuationSlider(window, susapad, self)
        self.actuation_slider_upper = actuation_point.UpperActuationSlider(window, susapad, self)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.first_h2)
        self.layout.addWidget(self.rt_button)
        self.layout.addWidget(QtWidgets.QLabel("Rapid Trigger Contínuor"))
        self.layout.addWidget(self.crt_button)
        self.layout.addWidget(QtWidgets.QLabel("Sensibilidade: Pressionar e Soltar"))
        self.layout.addWidget(self.sensibility_slider_press, alignment = Qt.AlignJustify)
        self.layout.addWidget(self.sensibility_slider_release, alignment = Qt.AlignJustify)
        self.layout.addWidget(QtWidgets.QLabel("Pontos de Ativação: Mínimo e Máximo"))
        self.layout.addWidget(self.actuation_slider_lower, alignment = Qt.AlignJustify)
        self.layout.addWidget(self.actuation_slider_upper, alignment = Qt.AlignJustify)



class WindowLayout(QtWidgets.QFrame):

    def __init__(self, window, susapad):
        super().__init__()

        self.setObjectName("background-frame")
        self.__init_style()

        self.forms = FormsGroup(window, susapad)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.forms)


    def __init_style(self):
        self.setStyleSheet(
            """

            QFrame {
                border-radius: 20px;
                background-color: #121212;
            }

            QLabel {
                color: white;
                font: 16px;
                margin-top: 20px;
                margin-bottom: 10px;
            } 

            QLabel#first-h2 {
                margin-top: 0px;
            } 

            QPushButton {
                margin-left: 20px;
            }

            QSlider::groove:horizontal {
                height: 16px;
                background-color: #861252;
                border-radius: 8px;
            }

            QSlider::handle:horizontal {
                width: 16px;
                height: 16px;
                border-radius: 8px;
                background-color: #127ecb;
                cursor: pointer;
            }

            """
        )
        self.setContentsMargins(20, 20, 20, 20)
