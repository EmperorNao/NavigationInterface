from formats.Format import Format
from datetime import date
from datetime import time
import pyqtgraph
from math import sin, cos, pi


class Nmea(Format):
    """
    Class which represent NMEA format
    """
    def __init__(self):
        self.keys = {
            "GPGGA": ["TIME", "LATITUDE", "N/S", "LONGITUDE", "E/W", "POS_FIX", "SATELLITES_USED",
                      "HDOP", "MSL_ALTITUDE", "UNITS_1", "GEOID_SEPARATION", "UNITS_2",
                      "AGE_OF_DIFF_CORRECTION", "DIFF_REF_STATION_ID", "CHECKSUM"],
            "GPGSA": ["MODE_1", "MODE_2", "SATELLITE_USED_01", "SATELLITE_USED_02", "SATELLITE_USED_03",
                      "SATELLITE_USED_04",
                      "SATELLITE_USED_05", "SATELLITE_USED_06", "SATELLITE_USED_07", "SATELLITE_USED_08",
                      "SATELLITE_USED_09",
                      "SATELLITE_USED_10", "SATELLITE_USED_11", "SATELLITE_USED_12", "PDOP", "HDOP", "VDOP",
                      "CHECKSUM"],
            "GPGSV": ["NUMBER_OF_MESSAGES", "MESSAGE_NUMBER", "SATELLITES_IN_VIEW", "CHECKSUM"],
            "GPRMC": ["TIME", "STATUS", "LATITUDE", "N/S", "LONGITUDE", "E/W", "SPEED_OVER_GROUND",
                      "COURSE_OVER_GROUND", "DATE", "MAGNETIC_VARIATION", "CHECKSUM"],
            "SATELLITE": ["SATELLITE_ID", "ELEVATION", "AZIMUTH", "SNR"]
        }
        self.plot_vars = ["TIME", "MSL_ALTITUDE", "LATITUDE", "LONGITUDE", "HDOP", "PDOP", "VDOP", "SPEED_OVER_GROUND",
                          "COURSE_OVER_GROUND", "ELEVATION", "AZIMUTH", "SNR"]
        self.plot_stat = ["TIME", "SOLUTION_LONGITUDE", "SOLUTION_LATITUDE", "SOLUTION_MSL_ALTITUDE",
                          "DEVIATION_LONGITUDE", "DEVIATION_LATITUDE", "DEVIATION_MSL_ALTITUDE"]
        self.interval = "TIME"

    @staticmethod
    def name():
        """

        :return: format name
        """
        return "NMEA"

    def to_str(self, d) -> str:
        """

        :param d: data to repr
        :return: representation of all information
        """
        o = []
        if isinstance(d, dict):
            for k, v in d.items():
                o.append(str(k) + ": " + self.to_str(v))

        elif isinstance(d, list):
            for el in d:
                o.append(self.to_str(el))

        else:
            o.append(str(d))

        return "\n".join(o)

    def measure(self, f: str = '') -> str:
        """

        :param f: format of value
        :return: measurement to this format
        """
        if f == "TIME":
            return "minute"
        elif f == 'LATITUDE':
            return "degree"
        elif f == 'N/S':
            return "__"
        elif f == 'LONGITUDE':
            return "degree"
        elif f == "E/W":
            return "__"
        elif f == "POS_FIX":
            return "__"
        elif f == "SATELLITES_USED":
            return "__"
        elif f == "HDOP":
            return "HDOP"
        elif f == "MSL_ALTITUDE":
            return "meters"
        elif f == "UNITS_1":
            return "__"
        elif f == "GEOID_SEPARATION":
            return "meters"
        elif f == "UNITS_2":
            return "__"
        elif f == "AGE_OF_DIFF_CORRECTION":
            return "seconds"
        elif f == "DIFF_REF_STATION_ID":
            return "__"
        elif f == "CHECKSUM":
            return "__"
        elif f == "MODE_1":
            return "__"
        elif f == "MODE_2":
            return "__"
        elif f[:-2] == "SATELLITE_USED_":
            return "__"
        elif f == "PDOP":
            return "PDOP"
        elif f == "VDOP":
            return "VDOP"
        elif f == "STATUS":
            return "__"
        elif f == "SPEED_OVER_GROUND":
            return "usels"
        elif f == "COURSE_OVER_GROUND":
            return "degrees"
        elif f == "DATE":
            return "__"
        elif f == "MAGNETIC_VARIATION":
            return "degrees"
        elif f == "NUMBER_OF_MESSAGES":
            return "__"
        elif f == "MESSAGE_NUMBER":
            return "__"
        elif f == "SATELLITES_IN_VIEW":
            return "__"
        elif f == "ELEVATION":
            return "degrees"
        elif f == "AZIMUTH":
            return "degrees"
        elif f == "SNR":
            return "DBHz"
        elif f == "DEVIATION_LATITUDE":
            return ""
        elif f == "DEVIATION_LONGITUDE":
            return ""
        elif f == "DEVIATION_MSL_ALTITUDE":
            return ""
        elif f == "SOLUTION_LATITUDE":
            return ""
        elif f == "SOLUTION_LONGITUDE":
            return ""
        elif f == "SOLUTION_MSL_ALTITUDE":
            return ""
        else:
            raise KeyError("Don't find right format for NMEA")

    def value(self, s: str = "", f: str = "") -> float:
        """
        get value as number for current format
        :param s: value to convert
        :param f: format of value
        :return: value as number
        """
        if s == "":
            raise ValueError("Value in str was empty")

        if f == "TIME":
            return int(s.hour) * 60 + int(s.minute) + float(s.second) / 60 + float(s.microsecond) / (60 * 1000 * 1000)
        elif f == 'LATITUDE':
            return float(s)
        elif f == 'N/S':
            raise ValueError
        elif f == 'LONGITUDE':
            return float(s)
        elif f == "E/W":
            raise ValueError
        elif f == "POS_FIX":
            return int(s)
        elif f == "SATELLITES_USED":
            return int(s)
        elif f == "HDOP":
            return float(s)
        elif f == "MSL_ALTITUDE":
            return float(s)
        elif f == "UNITS_1":
            raise ValueError
        elif f == "GEOID_SEPARATION":
            return float(s)
        elif f == "UNITS_2":
            raise ValueError
        elif f == "AGE_OF_DIFF_CORRECTION":
            return float(s)
        elif f == "DIFF_REF_STATION_ID":
            raise ValueError
        elif f == "CHECKSUM":
            raise ValueError
        elif f == "MODE_1":
            raise ValueError
        elif f == "MODE_2":
            raise ValueError
        elif f[:-2] == "SATELLITE_USED_":
            return int(s)
        elif f == "PDOP":
            return float(s)
        elif f == "VDOP":
            return float(s)
        elif f == "STATUS":
            raise ValueError
        elif f == "SPEED_OVER_GROUND":
            return float(s)
        elif f == "COURSE_OVER_GROUND":
            return float(s)
        elif f == "DATE":
            raise ValueError
        elif f == "MAGNETIC_VARIATION":
            return float(s)
        elif f == "NUMBER_OF_MESSAGES":
            raise ValueError
        elif f == "MESSAGE_NUMBER":
            raise ValueError
        elif f == "SATELLITES_IN_VIEW":
            raise ValueError
        elif f == "ELEVATION":
            return int(s)
        elif f == "AZIMUTH":
            return int(s)
        elif f == "SNR":
            return int(s)
        else:
            raise KeyError("Don't find right format for NMEA")

    def format(self, s: str, f: str = ''):
        """
        convertion from format to internal python storing
        :param s: value in str
        :param f: format of value
        :return: value in correct type to store
        """
        if s == "":
            raise ValueError("Value in str was empty")

        if f == "TIME":
            h = int(s[0:2])
            m = int(s[2:4])
            sec = int(s[4:6])
            mcs = int(s[7:9]) * 10000
            return time(hour=h, minute=m, second=sec, microsecond=mcs)
        elif f == 'LATITUDE':
            return int(s[0:2]) + float(s[2:]) / 60
        elif f == 'N/S':
            return s
        elif f == 'LONGITUDE':
            return int(s[0:3]) + float(s[3:]) / 60
        elif f == "E/W":
            return s
        elif f == "POS_FIX":
            return int(s)
        elif f == "SATELLITES_USED":
            return int(s)
        elif f == "HDOP":
            return float(s)
        elif f == "MSL_ALTITUDE":
            return float(s)
        elif f == "UNITS_1":
            return s
        elif f == "GEOID_SEPARATION":
            return s
        elif f == "UNITS_2":
            return s
        elif f == "AGE_OF_DIFF_CORRECTION":
            return s
        elif f == "DIFF_REF_STATION_ID":
            return s
        elif f == "CHECKSUM":
            return s
        elif f == "MODE_1":
            return s
        elif f == "MODE_2":
            return s
        elif f[:-2] == "SATELLITE_USED_":
            return int(s)
        elif f == "PDOP":
            return float(s)
        elif f == "VDOP":
            return float(s)
        elif f == "STATUS":
            return s
        elif f == "SPEED_OVER_GROUND":
            return float(s)
        elif f == "COURSE_OVER_GROUND":
            return float(s)
        elif f == "DATE":
            return date(day=int(s[0:2]), month=int(s[2:4]), year=int(s[4:6]) + 2000)
        elif f == "MAGNETIC_VARIATION":
            return float(s)
        elif f == "NUMBER_OF_MESSAGES":
            return int(s)
        elif f == "MESSAGE_NUMBER":
            return int(s)
        elif f == "SATELLITES_IN_VIEW":
            return int(s)
        elif f == "ELEVATION":
            return int(s)
        elif f == "AZIMUTH":
            return int(s)
        elif f == "SNR":
            return int(s)
        else:
            raise KeyError("Don't find right format for NMEA")

    def to_format(self, value, f: str = '') -> str:
        """
        reverse format method, convertion from python storing into format
        :param value: value
        :param f: format of value
        :return: value for format in string
        """

    def convert(self, s: str = '', sep: str = ',') -> dict:
        """
        convert one line from file
        :param s: line
        :param sep: separator
        :return: return dict of storing in line values
        """
        content = s.split(",")
        last = content.pop()
        content += last.split("*")
        message_id = content[0].strip("\ufeff")[1:]

        output = {}
        output["MESSAGE_ID"] = message_id
        if message_id == "GPGSV":
            output["NUMBER_OF_MESSAGES"] = self.format(content[1], "NUMBER_OF_MESSAGES")
            output["MESSAGE_NUMBER"] = self.format(content[2], "MESSAGE_NUMBER")
            output["SATELLITES_IN_VIEW"] = self.format(content[3], "SATELLITES_IN_VIEW")
            output["SATELLITES"] = []
            for i in range(4, len(content) - 1, 4):

                d = {}
                for j, key in enumerate(self.keys["SATELLITE"]):
                    d[key] = content[i + j]
                output["SATELLITES"].append(d)

            output["CHECKSUM"] = self.format(content[-1], "CHECKSUM")

        elif message_id in self.keys.keys():
            for i, f in enumerate(self.keys[message_id]):
                if content[i + 1] != "":
                    try:
                        output[f] = self.format(content[i + 1], f)
                    except ValueError as ve:
                        raise ve
                    except KeyError as ke:
                        raise ke

        else:
            raise KeyError("Missing format of message in NMEA message")

        return output

    def load(self, filename: str = "") -> [dict]:
        """
        load info from file
        :param filename:
        :return: list of dicts values
        """

        try:
            c = []
            with open(filename, encoding='utf8') as file:

                file = file.readlines()
                cur_d = {}
                i = 0

                while i < len(file):

                    d = self.convert(file[i][:-1])
                    msg_id = d['MESSAGE_ID']
                    if msg_id != "GPGSV" and msg_id in cur_d.keys():
                        cur_d["TIME"] = cur_d["GPGGA"]["TIME"]
                        c.append(cur_d)
                        cur_d = {}
                        continue

                    elif msg_id == "GPGSV":

                        satellites = [d]
                        num_msg = d["NUMBER_OF_MESSAGES"]
                        for j in range(1, num_msg):
                            add_d = self.convert(file[i + j][:-1])
                            satellites.append(add_d)

                        cur_d["GPGSV"] = satellites
                        i += num_msg

                    else:
                        cur_d[d["MESSAGE_ID"]] = d
                        i += 1

            return c

        except ValueError as ve:
            raise ve
        except KeyError as ke:
            raise ke

    def plot(self, format_x, format_y, info: [dict] = [], plotter: pyqtgraph.PlotWidget = None) -> None:
        """
        method to abstract plotting with sense of knowing format and values
        :param format_x:
        :param format_y:
        :param info: data to plot
        :param: plotter: class to plot that provides method plot
        :return:
        """

        if format_x == "LONGITUDE" and format_y == "LATITUDE":
            x = [self.value(el["GPRMC"][format_x], format_x) if format_x in el["GPRMC"].keys()
                 else 0 for el in info]

            y = [self.value(el["GPRMC"][format_y], format_x) if format_y in el["GPRMC"].keys()
                 else 0 for el in info]

            hdop_format = "HDOP"
            hdop = [self.value(el["GPGGA"][hdop_format], hdop_format) / 6371000 if hdop_format
                    in el["GPGGA"].keys() else 0 for el in info]

            h = []
            num = len(x)
            max_y = max(y)
            for i in range(0, num):
                h.append(y[i] + hdop[i])
            plotter.plot(x, h, pen=pyqtgraph.mkPen('b'))

            h = []
            for i in range(0, num):
                h.append(y[i] - hdop[i])
            plotter.plot(x, h, pen=pyqtgraph.mkPen('r'))

            plotter.plot(x, y, pen=pyqtgraph.mkPen('w'))
            return

        elif format_x == "TIME" and format_y == "MSL_ALTITUDE":
            x = [self.value(el["GPGGA"][format_x], format_x) if format_x in el["GPGGA"].keys()
                 else 0 for el in info]

            y = [self.value(el["GPGGA"][format_y], format_x) if format_y in el["GPGGA"].keys()
                 else 0 for el in info]

            vdop_format = "VDOP"
            vdop = [self.value(el["GPGSA"][vdop_format], vdop_format) / 6371000 if vdop_format
                    in el["GPGSA"].keys() else 0 for el in info]

            v = []
            num = len(x)
            max_y = max(y)
            for i in range(0, num):
                v.append(y[i] + vdop[i])
            plotter.plot(x, v, pen=pyqtgraph.mkPen('b'))

            v = []
            for i in range(0, num):
                v.append(y[i] - vdop[i])
            plotter.plot(x, v, pen=pyqtgraph.mkPen('r'))

            plotter.plot(x, y, pen=pyqtgraph.mkPen('w'))
            return

        elif format_x == "AZIMUTH" and format_y == "ELEVATION":

            colors = ["g", "r", "c", "m", "y", "k", "w", (100, 100, 100), (200, 200, 200), (150, 150, 150), (50, 50, 50), (50, 150, 200)]
            d = {}
            for el in info:

                for msg in el["GPGSV"]:

                    for sat in msg['SATELLITES']:
                        id = sat["SATELLITE_ID"]
                        try:
                            r = 90 - self.value(sat["ELEVATION"], "ELEVATION")
                            alpha = self.value(sat["AZIMUTH"], "AZIMUTH") * pi / 180
                            if id in d.keys():
                                d[id].append([r * cos(alpha), r * sin(alpha)])

                            else:
                                d[id] = [[r * cos(alpha), r * sin(alpha)]]
                        except ValueError as ve:
                            pass

            plotter.setBackground((30, 30, 30))
            plotter.addLegend()
            for i, id in enumerate(d.keys()):

                x = []
                y = []
            for x_, y_ in d[id]:
                x.append(x_)
                y.append(y_)

            plotter.plot(x, y, pen=pyqtgraph.mkPen(colors[i % (len(colors))], width = 3), name=id)

            xs = []
            ys = []

            r = 90
            x = []
            y = []
            for alpha in range(0, 360):
                alpha = alpha * pi / 180
                x.append(r * cos(alpha))
                y.append(r * sin(alpha))
            xs.append(x)
            ys.append(y)

            r = 60
            x = []
            y = []
            for alpha in range(0, 360):
                alpha = alpha * pi / 180
                x.append(r * cos(alpha))
                y.append(r * sin(alpha))
            xs.append(x)
            ys.append(y)

            r = 30
            x = []
            y = []
            for alpha in range(0, 360):
                alpha = alpha * pi / 180
                x.append(r * cos(alpha))
                y.append(r * sin(alpha))
            xs.append(x)
            ys.append(y)

            for i in range(len(xs)):
                plotter.plot(xs[i], ys[i], pen=pyqtgraph.mkPen("w", width=1), name=id)
            return

        x = []
        for k, v in self.var_keys().items():
            if format_x in v:
                x = [self.value(el[k][format_x], format_x) if format_x in el[k].keys() else 0
                     for el in info]

        y = []
        for k, v in self.var_keys().items():
            if format_y in v:
                y = [self.value(el[k][format_y], format_y) if format_x in el[k].keys() else 0
                     for el in info[k]]

        plotter.plot(x, y)

    def plot_with_stat(self, format_x, format_y, info: [dict] = [], stat: dict = dict(), plotter=None):

        spl_x = format_x.split("_")
        var_x = "_".join(spl_x[1:])
        spl_y = format_y.split("_")
        var_y = "_".join(spl_y[1:])

        statistic = []
        if "difference" in stat.keys():
            statistic = stat["difference"]
        else:
            statistic = stat["main"]

        x_data = []
        if spl_x[0] == "SOLUTION":

            x_data.append([])
            for el in info:
                if var_x in el["GPGGA"].keys():
                    x_data[0].append(el["GPGGA"][var_x])

            ind = 0
            if var_x == "LATITUDE":
                ind = 0
            elif var_x == "LONGITUDE":
                ind = 1
            elif var_x == "MSL_ALTITUDE":
                ind = 2

            mean = statistic["MEAN"][ind]

            x_data.append([])
            for el in x_data[0]:
                x_data[1].append(mean)

        elif spl_x[0] == "DEVIATION":

            values = []
            for el in info:
                if var_x in el["GPGGA"].keys():
                    values.append(el["GPGGA"][var_x])

            ind = 0
            if var_x == "LATITUDE":
                ind = 0
            elif var_x == "LONGITUDE":
                ind = 1
            elif var_x == "MSL_ALTITUDE":
                ind = 2

            mean = statistic["MEAN"][ind]

            x_data.append([])
            for el in values:
                x_data[0].append(abs(el - mean))

        elif spl_x[0] == "TIME":
            x_data.append([])
            for el in info:
                x_data[0].append(self.value(el["GPGGA"]["TIME"], "TIME"))

        y_data = []
        if spl_y[0] == "SOLUTION":

            y_data.append([])
            for el in info:
                if var_y in el["GPGGA"].keys():
                    y_data[0].append(el["GPGGA"][var_y])

            ind = 0
            if var_y == "LATITUDE":
                ind = 0
            elif var_y == "LONGITUDE":
                ind = 1
            elif var_y == "MSL_ALTITUDE":
                ind = 2

            mean = statistic["MEAN"][ind]

            y_data.append([])
            for el in y_data[0]:
                y_data[1].append(mean)

        elif spl_y[0] == "DEVIATION":

            values = []
            for el in info:
                if var_y in el["GPGGA"].keys():
                    values.append(el["GPGGA"][var_y])

            ind = 0
            if var_y == "LATITUDE":
                ind = 0
            elif var_y == "LONGITUDE":
                ind = 1
            elif var_y == "MSL_ALTITUDE":
                ind = 2

            mean = statistic["MEAN"][ind]

            y_data.append([])
            for el in values:
                y_data[0].append(abs(el - mean))

        elif spl_y[0] == "TIME":
            y_data.append([])
            for el in info:
                y_data[0].append(self.value(el["GPGGA"]["TIME"], "TIME"))

        colors = ["w", "r", "c", "m", "y", "k", "w"]
        for i, y in enumerate(y_data):
            min_len = len(x_data[0])
            if len(x_data[0]) != len(y):
                min_len = min(len(x_data[0]), len(y))

            plotter.plot(x_data[0][:min_len], y[:min_len], pen=pyqtgraph.mkPen(colors[i % (len(colors))], width=3), name=id)

            #plotter.plot(x_data[0][:min_len], y[:min_len])

    def upload(self, filename: str = "", info: [dict] = []):
        """
        load info to file
        :param filename:
        :param info: data
        :return:
        """
        return
