# TODO: remake imports
# TODO: do not use bare except
from AppAdaptor import *
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pyqtgraph as pg
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from datetime import datetime


class NavigationModel:
    """
    Main class that represent info about current data stored and some technical information for navigation
    """

    def __init__(self):
        self.additional_file = ""
        self.cur_file = ""
        self.cur_format = ""
        self.info = []
        self.stat = {}
        self.ind = 0


class NavigationUi(QtWidgets.QMainWindow):
    """
    Class that provides all UI components and signals to work with them, also it builds main logical dependencies
    in plotter and parser
    """

    def __init__(self, navigation: NavigationModel):
        super().__init__()

        self.model = navigation
        # main windows settings
        self.setWindowTitle("Navigation")
        self.setFixedSize(1300, 600)

        # main layout and main widget
        self.general_layout = QGridLayout()
        self.centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.general_layout)

        # init inclusive layouts
        self._init_left_layout()
        self._init_center_layout()
        self._init_right_layout()

        # init model
        self.model.cur_format = str(self.format_selection.currentText())

    def _init_left_layout(self):
        """
        Do not call this method, it is only for internal usage in __init__
        to build left part of NavigationUI
        :return:
        """
        # left
        self.left_layout = QGridLayout()
        self.general_layout.addLayout(self.left_layout, 0, 0)

        self.content = QtWidgets.QTextEdit()
        self.content.setMaximumWidth(400)
        self.content.setReadOnly(True)

        self.label_info = QtWidgets.QLabel()
        self.label_info.setText("Info")
        self.label_info.setFont(QFont('', 15))
        self.label_info.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.left_layout.addWidget(self.label_info, 0, 0)
        self.left_layout.addWidget(self.content, 1, 0)

    def _init_center_layout(self):
        """
        Do not call this method, it is for internal usage in __init__
        to build center part of NavigationUI
        :return:
        """
        self.central_layout = QGridLayout()
        self.general_layout.addLayout(self.central_layout, 0, 4)

        self.import_btn = QPushButton("Import")
        self.import_btn.clicked.connect(self.import_file)

        self.export_btn = QPushButton("Export")
        self.export_btn.clicked.connect(self.export_file)

        self.transform_btn = QPushButton("Transform")
        self.transform_btn.clicked.connect(self.transform)

        self.csv_btn = QPushButton("CSV")
        self.csv_btn.clicked.connect(self.csv)

        self.left_arrow_btn = QPushButton("<-")
        self.right_arrow_btn = QPushButton("->")

        self.import_additional_btn = QPushButton("Import stat")
        self.import_additional_btn.clicked.connect(self.import_additional_file)

        self.refresh_btn = QPushButton("Refresh")
        self.refresh_btn.clicked.connect(self.refresh)

        self.left_arrow_btn.clicked.connect(self.left_arrow)
        self.right_arrow_btn.clicked.connect(self.right_arrow)

        self.format_selection = QComboBox()
        for f in FORMATS:
            self.format_selection.addItem(f)

        self.central_layout.addWidget(self.import_btn, 0, 0)
        self.central_layout.addWidget(self.export_btn, 2, 0)
        self.central_layout.addWidget(self.transform_btn, 4, 0)
        self.central_layout.addWidget(self.csv_btn, 6, 0)
        self.central_layout.addWidget(self.format_selection, 8, 0)
        self.central_layout.addWidget(self.left_arrow_btn, 10, 0)
        self.central_layout.addWidget(self.right_arrow_btn, 12, 0)
        self.central_layout.addWidget(self.import_additional_btn, 14, 0)
        self.central_layout.addWidget(self.refresh_btn, 16, 0)
        self.central_layout.addLayout(QGridLayout(), 18, 0, 6, 1)

    def _init_right_layout(self):
        """
        Do not call this method, it is only for internal usage in __init__
        to build right part of NavigationUI
        :return:
        """
        self.right_layout = QGridLayout()
        self.general_layout.addLayout(self.right_layout, 0, 5, 7, 7)

        self.graph_widget = pg.PlotWidget()
        self.graph_widget.setLabel('left', '')
        self.graph_widget.setLabel('bottom', '')

        self.plot_btn = QPushButton('Plot')
        self.plot_btn.clicked.connect(self.plot)

        self.cur_x = QComboBox()
        self.left_x_interval = QTextEdit()
        self.cur_y = QComboBox()
        self.right_x_interval = QTextEdit()

        self.cur_x_label = QLabel("???????????????????? x: ")
        self.left_x_interval_label = QLabel('???????????? ??????????????????: ')
        self.cur_y_label = QLabel('???????????????????? y: ')
        self.right_x_interval_label = QLabel('?????????? ??????????????????: ')

        self._update_variables_combobox()

        self.cur_x.setMaximumWidth(150)
        self.cur_x.setMaximumHeight(25)
        self.left_x_interval.setMaximumWidth(150)
        self.left_x_interval.setMaximumHeight(25)
        self.cur_y.setMaximumWidth(150)
        self.cur_y.setMaximumHeight(25)
        self.right_x_interval.setMaximumWidth(150)
        self.right_x_interval.setMaximumHeight(25)

        self.cur_x_label.setMaximumWidth(150)
        self.cur_x_label.setMaximumHeight(25)
        self.left_x_interval_label.setMaximumWidth(150)
        self.left_x_interval_label.setMaximumHeight(25)
        self.cur_y_label.setMaximumWidth(150)
        self.cur_y_label.setMaximumHeight(25)
        self.right_x_interval_label.setMaximumWidth(150)
        self.right_x_interval_label.setMaximumHeight(25)

        self.right_layout.addWidget(self.cur_x, 7, 1)
        self.right_layout.addWidget(self.left_x_interval, 8, 1)
        self.right_layout.addWidget(self.cur_y, 7, 3)
        self.right_layout.addWidget(self.right_x_interval, 8, 3)

        self.right_layout.addWidget(self.cur_x_label, 7, 0)
        self.right_layout.addWidget(self.left_x_interval_label, 8, 0)
        self.right_layout.addWidget(self.cur_y_label, 7, 2)
        self.right_layout.addWidget(self.right_x_interval_label, 8, 2)

        self.right_layout.addWidget(self.plot_btn, 9, 2, 2, 1)
        self.right_layout.addWidget(self.graph_widget, 0, 0, 5, 5)

    def _update_ui(self):
        """
        method updates all ui elements that changed after uploading new data
        :return:
        """
        try:
            self._update_content()
            self._update_variables_combobox()
            self._update_intervals()
        except:
            raise ValueError

    def get_current_format(self):
        """

        :return: method return current selected format
        """
        return str(self.format_selection.currentText())

    def _update_variables_combobox(self):
        """
        method updates variable names in boxes
        :return:
        """
        self.cur_x.clear()
        self.cur_y.clear()
        f = self.get_current_format()
        if self.model.ind >= len(self.model.info):
            var = []
        else:
            form = Factory().create(f)
            plot_keys = form.plot_keys()
            var = [el for el in plot_keys]
            if self.model.additional_file:
                try:
                    for val in form.plot_stat:
                        var.append(val)
                except:
                    pass

        for val in set(var):
            self.cur_x.addItem(val)
            self.cur_y.addItem(val)

    def _update_content(self):
        """
        method updates content
        :return:
        """
        self.content.clear()
        f = str(self.format_selection.currentText())
        try:
            form = Factory.create(f)
            try:
                self.content.append(form.to_str(self.model.info[self.model.ind]))
            except KeyError as ke:
                self.content.append(form.to_str(self.model.info))

        except:
            NavigationUi.error("File error", f"There was en error while loading {form.name()} content",
                                    "idk what to do lol")

    def _update_intervals(self):
        """
        :return:
        """
        f = self.model.cur_format
        form = Factory.create(f)
        interval = form.interval
        if interval == "TIME":
            self.left_x_interval.setText("00:00:00")
            self.right_x_interval.setText("23:59:59")
        elif interval == "DATETIME":
            self.left_x_interval.setText("2000-01-01 00:00:00")
            self.right_x_interval.setText("2100-01-01 23:59:59")

    def get_cur_intervals(self) -> tuple:
        """
        :return: return values of time in start and end intervals
        """
        f = self.model.cur_format
        form = Factory.create(f)
        interval = form.interval
        if interval == "TIME":

            start_interval = time(0, 0, 0)
            try:
                val = self.left_x_interval.toPlainText()
                start_interval = NavigationUi.convert_time(val)
            except:
                if val != "":
                    self.error("Value error", "Left interval for x in time wasn't specified right",
                               "Interval for x in time wasn't specified right. Try HH:MM:SS format")

            val = self.right_x_interval.toPlainText()
            end_interval = time(23, 59, 59)
            try:
                end_interval = NavigationUi.convert_time(val)
            except:
                if val != "":
                    self.error("Value error", "Right interval for x in time wasn't specified right",
                               "Interval for x in time wasn't specified right. Try HH:mm:SS format")

            return start_interval, end_interval, interval

        elif interval == "DATETIME":

            start_interval = datetime(2000, 1, 1, 0, 0, 0)
            try:
                val = self.left_x_interval.toPlainText()
                start_interval = NavigationUi.convert_datetime(val)
            except:
                if val != "":
                    self.error("Interval for x in time wasn't specified right. Try YYYY-MM-DD HH:mm:SS format", "Left interval for x in time wasn't specified right",
                               "Value error")

            end_interval = datetime(2100, 1, 1, 23, 59, 59)
            try:
                val = self.right_x_interval.toPlainText()
                end_interval = NavigationUi.convert_datetime(val)
            except:
                if val != "":
                    self.error("Value error", "Right interval for x in time wasn't specified right",
                               "Interval for x in time wasn't specified right. Try HH:MM:SS format")

            return start_interval, end_interval, interval

    def get_info_in_cur_intervals(self) -> list:
        """
        :return: values between current intervals of time
        """
        start_interval, end_interval, interval = self.get_cur_intervals()

        x = []
        try:
            i = 0
            while i < len(self.model.info) and self.model.info[i][interval] < start_interval:
                i += 1

            j = len(self.model.info) - 1
            while j >= 0 and self.model.info[j][interval] > end_interval:
                j -= 1
            return self.model.info[i:j + 1]

        except:
            self.error("Value error", "X or Y wasn't specified right", "Error")
            raise ValueError

    @staticmethod
    def convert_time(s: str) -> time:
        """
        :param s: str
        :return: time from s in format HH:MM:SS or raise Exception
        """
        t = s.split(":")
        try:
            return time(int(t[0]), int(t[1]), int(t[2]))
        except:
            raise ValueError

    @staticmethod
    def convert_datetime(s: str) -> time:
        """
        :param s: str
        :return: time from s in format HH:MM:SS or raise Exception
        """
        dt = s.split(" ")
        d = dt[0].split("-")
        t = dt[1].split(":")
        try:
            return datetime.combine(date(int(d[0]), int(d[1]), int(d[2])), time(int(t[0]), int(t[1]), int(t[2])))
        except:
            raise ValueError

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

    # signals
    def import_additional_file(self):
        """
        signal to connect with Import-button and load all components of UI
        :return:
        """
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')
        f = Statistic.name()

        try:
            form = Factory.create(f)
            self.model.stat = form.load(filename[0])
            self.model.additional_file = filename

        except Exception as e:
            NavigationUi.error("There was an error while trying to open file", str(e), "Error")
            return

        try:
            self._update_ui()
        except:
            NavigationUi.error("Format error", "There was an error with format, change format or file", "Error")

    def refresh(self):
        self.model.cur_format = ""
        self.model.cur_file = ""
        self.model.info = []
        self.model.additional_file = ""
        self.model.stat = {}

    def import_file(self):
        """
        signal to connect with Import-button and load all components of UI
        :return:
        """
        filename = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open file')
        f = str(self.format_selection.currentText())

        try:
            form = Factory.create(f)
            self.model.ind = 0
            self.model.cur_format = f
            if len(filename[0]) == 1:
                self.model.info = form.load(filename[0][0])
                self.model.cur_file = filename[0][0]

            else:
                self.model.cur_file = filename[0]
                self.model.info = []
                for file in self.model.cur_file:

                    self.model.info += form.load(file)

        except Exception as e:
            NavigationUi.error("There was an error while trying to open file", str(e), "Error")
            return

        try:
            self._update_ui()
        except:
            NavigationUi.error("Format error", "There was an error with format, change format or file", "Error")

    def export_file(self):
        """
        signal to connect with Export-button
        :return:
        """
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Open file')
        f = str(self.format_selection.currentText())
        try:
            form = Factory.create(f)
            form.upload(filename[0], self.get_info_in_cur_intervals())
        except:
            self.error("Export error", "There was an error while trying to export file", "Error")

    def transform(self):
        """
        signal to connect with transform-button
        :return:
        """
        # TODO transform method
        new_format = str(self.format_selection.currentText())
        cur_format = self.model.cur_format
        try:
            self.model.info = Transformer(cur_format, new_format, self.get_info_in_cur_intervals())
            self.model.cur_format = new_format
            self.model.ind = 0
        except:
            NavigationUi.error("Transform error", "There was an error while trying to transform data", "Error")

        try:
            self._update_ui()
        except:
            raise ValueError

    def csv(self):
        """
        signal to connect with CSV-button
        :return:
        """
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Open file')
        # cur_format = self.model.cur_format
        try:
            df = pd.DataFrame(self.get_info_in_cur_intervals())
            filename = filename[0]
            if filename.split('.')[-1] == 'csv':
                df.to_csv(filename, index=False)
            else:
                df.to_csv(filename + '.csv', index=False)
        except:
            self.error("CSV error", "There was an error while trying to create csv file", "Error")

    def left_arrow(self):
        """
        signal to connection with left_arrow button
        which update content
        :return:
        """
        self.model.ind = (self.model.ind - 1) % len(self.model.info)

        try:
            self._update_content()
        except:
            raise ValueError

    def right_arrow(self):
        """
        signal to connection with right_arrow button
        which update content
        :return:
        """
        self.model.ind = (self.model.ind + 1) % len(self.model.info)

        try:
            self._update_content()
        except:
            raise ValueError

    def plot(self):
        """
        signal to connect with plot button
        which saving x range to model and plotting x and y variables
        :return:
        """
        # get x range
        self.graph_widget.clear()
        cur_x = str(self.cur_x.currentText())
        cur_y = str(self.cur_y.currentText())
        if cur_x == "" or cur_y == "":
            self.error("X or Y error", "X or Y wasn't specified right", "Error")
            return

        x = []
        y = []
        x_measure = ""
        y_measure = ""
        f = self.format_selection.currentText()
        form = Factory().create(f)

        try:
            builder = ValueBuilder(f, cur_x, cur_y, self.get_info_in_cur_intervals())
        except KeyError as ke:
            self.error("Format error", "Wrong format of data", "Error")
            return

        try:
            x_measure, y_measure = builder.get_measures()

            if cur_x in form.plot_stat and cur_y in form.plot_stat and self.model.additional_file:
                try:
                    builder.plot_with_stat(self.graph_widget, self.model.stat)
                except:
                    pass
            else:
                builder.plot(self.graph_widget)

            #self.graph_widget.plot(x, y)
            self.graph_widget.setLabel('left', cur_y + ", " + y_measure)
            self.graph_widget.setLabel('bottom', cur_x + ", " + x_measure)
        except BaseException as be:
            self.error("Can't convert and plot data", str(be), "Error")
            return
