from Format import Format


class Nmea(Format):
    """
    Class which represent NMEA format
    """
    def __init__(self):
        self.keys = {
            "GPGGA": ["UTC_TIME", "LATITUDE", "N/S", "E/W", "POS_FIX", "SATELLITES_USED",
                      "HDOP", "MSL_ALTITUDE", "UNITS1_", "GEOID_SEPARATION", "UNITS_2",
                      "AGE_OF_DIFF_CORRECTION", "DIFF_REF_STATION_ID", "CHECKSUM"],
            "GPGSA": ["MODE_1", "MODE_2", "SATELLITE_USED_1", "SATELLITE_USED_2", "SATELLITE_USED_3", "SATELLITE_USED_4",
                      "SATELLITE_USED_5", "SATELLITE_USED_6", "SATELLITE_USED_7", "SATELLITE_USED_8", "SATELLITE_USED_9",
                      "SATELLITE_USED_10", "SATELLITE_USED_11", "SATELLITE_USED_12", "PDOP", "HDOP", "VDOP", "CHECKSUM"],
            "GPGSV": ["NUMBER_OF_MESSAGES", "MESSAGE_NUMBER", "SATELLITES IN VIEW",
                      ["SATELLITE_ID", "ELEVATION", "AZIMUTH", "SNR", "CHECKSUM"]],
            "GPRMC": ["UTC_TIME", "STATUS", "LATITUDE", "N/S", "LONGITUDE", "E/W", "SPEED_OVER_GROUND",
                      "COURSE_OVER_GROUND", "DATE", "MAGNETIC_VARIATION", "CHECKSUM"]
        }

    @staticmethod
    def name():
        """

        :return: format name
        """
        return "NMEA"

    def value(self, s: str = "", f: str = "") -> float:
        """
        get value as number for current format
        :param s: value to convert
        :param f: format of value
        :return: value as number
        """
        return None

    def format(self, s: str, f: str = ''):
        """
        convertion from format to internal python storing
        :param s: value in str
        :param f: format of value
        :return: value in correct type to store
        """
        return None

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
        if content[0] == "$GPGGA":
            pass

        elif content[0] == "$GPRMC":
            pass

        elif content[0] == "$GPGSA":
            pass

        elif content[0] == "$GPGSV":
            pass

        else:
            raise KeyError

        return None

    def load(self, filename: str = "") -> [dict]:
        """
        load info from file
        :param filename:
        :return: list of dicts values
        """
        return None

    def plot(self, format_x, format_y, info: [dict] = []) -> tuple:
        """
        method to abstract plotting with sense of knowing format and values
        :param format_x:
        :param format_y:
        :param info: data to plot
        :return: return tuple of values for x and y from info
        """
        return None

    def upload(self, filename: str = "", info: [dict] = []):
        """
        load info to file
        :param filename:
        :param info: data
        :return:
        """
        return
