from AppAdaptor import *
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pyqtgraph as pg
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from statistic.StatCounter import StatCounter


class StatisticModel:

    def __init__(self):
        self.main_file = ""
        self.additional_file = ""
        self.info = {}


class StatisticUi(QtWidgets.QMainWindow):
    """
    Class that provides all UI components and signals to work with them, also it builds main logical dependencies
    in stat builder and parser
    """

    def __init__(self, statistic: StatisticModel):
        super().__init__()

        self.model = statistic
        self.setWindowTitle("StatCounter")
        self.setFixedSize(600, 400)

        # main layout and main widget
        self.general_layout = QGridLayout()
        self.centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.general_layout)

        # init inclusive layouts
        self._init_left_layout()
        self._init_right_layout()

    def _init_left_layout(self):
        """
        Do not call this method, it is only for internal usage in __init__
        to build left part of UI
        :return:
        """
        # left
        self.left_layout = QGridLayout()
        self.general_layout.addLayout(self.left_layout, 0, 0)

        self.content = QtWidgets.QTextEdit()
        self.content.setMaximumWidth(450)
        self.content.setReadOnly(True)

        self.label_info = QtWidgets.QLabel()
        self.label_info.setText("Statistic")
        self.label_info.setFont(QFont('', 15))
        self.label_info.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.left_layout.addWidget(self.label_info, 0, 0)
        self.left_layout.addWidget(self.content, 1, 0)

    def _init_right_layout(self):
        """
        Do not call this method, it is for internal usage in __init__
        to build right part of NavigationUI
        :return:
        """
        self.central_layout = QGridLayout()
        self.general_layout.addLayout(self.central_layout, 0, 4)

        self.import_general_btn = QPushButton("Import main")
        self.import_general_btn.clicked.connect(self.import_general_file)
        self.import_additional_btn = QPushButton("Import additional")
        self.import_additional_btn.clicked.connect(self.import_additional_file)

        self.export_btn = QPushButton("Export statistic")
        self.export_btn.clicked.connect(self.export_file)

        self.refresh_btn = QPushButton("Refresh")
        self.refresh_btn.clicked.connect(self.refresh)

        self.count_btn = QPushButton("Count statistics")
        self.count_btn.clicked.connect(self.count_stat)

        self.format_selection = QComboBox()
        for f in FORMATS:
            self.format_selection.addItem(f)

        self.central_layout.addWidget(self.import_general_btn, 0, 0)
        self.central_layout.addWidget(self.import_additional_btn, 2, 0)
        self.central_layout.addWidget(self.refresh_btn, 4, 0)
        self.central_layout.addWidget(self.export_btn, 6, 0)
        self.central_layout.addWidget(self.format_selection, 8, 0)
        self.central_layout.addWidget(self.count_btn, 10, 0)
        self.central_layout.addLayout(QGridLayout(), 12, 0, 6, 1)

    def _update_ui(self):
        """
        method updates all ui elements that changed after uploading new data
        :return:
        """
        try:
            self._update_content()
        except:
            raise ValueError

    def _update_content(self):
        """
        update left content
        :return:
        """

        self.content.clear()
        try:
            form = Factory.create(Statistic.name())
            self.content.append(form.to_str(self.model.info))
        except:
            StatisticUi.error("File error", f"There was en error while loading {form.name()} content",
                               "idk what to do lol")

    @staticmethod
    def error(text: str = "", info_text: str = "", title: str = ""):
        """
        method to call, when error has happened
        :param text: short description of error
        :param info_text: extended error description
        :param title: window title
        :return:
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        msg.setInformativeText(info_text)
        msg.setWindowTitle(title)
        msg.exec()

    def upload(self, filename, f: str = "") -> []:
        if f == Nmea.name():
            form = Factory.create(f)
            return form.load(filename)

        else:
            self.error("Wrong statistic", "Wrong type was provided for statistic", "Try change file type")

    def one_file_stat(self, filename: str = "", f: str = ""):
        if f == Nmea.name():
            counter = StatCounter()
            return counter.count(self.upload(filename, f), f)

        else:
            self.error("Wrong statistic", "Wrong type was provided for statistic", "Try change file type")

    # signals
    def import_general_file(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')[0]
        f = str(self.format_selection.currentText())

        try:
            form = Factory.create(f)
            self.model.main_file = filename
        except:
            StatisticUi.error("Import error", "There was an error while trying to open file", "Error")
            return

    def import_additional_file(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')[0]
        f = str(self.format_selection.currentText())

        try:
            self.model.additional_file = filename
        except:
            StatisticUi.error("Import error", "There was an error while trying to open file", "Error")
            return

    def export_file(self):
        """
        signal to connect with Export-button
        :return:
        """
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Open file')
        try:
            form = Factory.create(Statistic.name())
            form.upload(filename[0], self.model.info)
        except:
            self.error("Export error", "There was an error while trying to export file", "Error")

    def refresh(self):
        self.model.main_file = ""
        self.model.additional_file = ""
        self.model.info = ""
        self._update_ui()

    def count_stat(self):

        def add_str_to_keys(d: dict, s: str):
            new_d = {}
            for k, v in d.items():
                new_d[k + s] = d[k]
            return new_d

        try:
            if not self.model.main_file or not self.model.additional_file:

                filename = self.model.main_file if self.model.main_file is not None else self.model.additional_file
                self.model.info = {"main": self.one_file_stat(filename, self.format_selection.currentText())}

            else:

                f = self.format_selection.currentText()
                all_data = dict()

                all_data["main"] = self.one_file_stat(self.model.main_file, f)
                all_data["additional"] = self.one_file_stat(self.model.additional_file, f)

                v1 = self.upload(self.model.main_file, f)
                v2 = self.upload(self.model.additional_file, f)

                counter = StatCounter()
                all_data["difference"] = counter.count_comparing(v1, v2, f)
                self.model.info = all_data

            self._update_ui()

        except BaseException as be:
            self.error("Statistic error", "Error while trying to count statistic", str(be))