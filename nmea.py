'''
def convert_to_value(s: str, f: str = '', var: str = ''):
    if f == SGK_T:
        try:
            return sgk_t_value(s, var)
        except:
            raise ValueError


def convert_formats(src_f: str = "", destination_f: str = "", data: list = []):
    if src_f not in FORMATS or destination_f not in FORMATS:
        raise ValueError

    new_data = data
    if src_f == SGK_T:

        pass

    return new_data


def sgk_t_value(s, f: str = '') -> tuple:
    """
    :param s: value to convert
    :param f: name of value
    :return: return tuple of (value: int, measure: str)
    """

    if s == '':
        raise ValueError

    if f == 'DEVICE_ID':
        raise ValueError
    elif f == 'DATE':
        raise ValueError
    elif f == 'TIME':
        return int(s.hour) * 60 + int(s.minute) + float(s.second) / 60, "minute"
    elif f == 'LATITUDE':
        return float(s), "degree"
    elif f == 'N/S':
        raise ValueError
    elif f == 'LONGITUDE':
        return float(s), "degree"
    elif f == 'E/W':
        raise ValueError
    elif f == 'SPEED':
        return int(s), "km/h"
    elif f == 'COURSE':
        return int(s), "__"
    elif f == 'ALTITUDE':
        return int(s), "__"
    elif f == 'ODOMETER':
        return int(s), "__"
    elif f == 'IO_STATUS':
        return int(s), "__"
    elif f == 'EVENT_ID':
        return int(s), "__"
    elif f == 'AIN1':
        return float(s), "__"
    elif f == 'AIN2':
        return float(s), "__"
    elif f == 'FIX_MODE':
        return int(s), "__"
    elif f == ('%s_SAT_NO' % SGK_T):
        return int(s), "__"
    elif f == 'GPS_SAT_NO':
        return int(s), "__"
    elif f == 'HDOP':
        return float(s), "__"


def sgk_t_format(s: str, f: str = ''):

    if s == '':
        raise ValueError

    if f == 'DEVICE_ID':
        return int(s)
    elif f == 'DATE':
        return date(int('20' + s[4:6]), int(s[2:4]), int(s[0:2]))
    elif f == 'TIME':
        return time(int(s[0:2]), int(s[2:4]), int(s[4:6]))
    elif f == 'LATITUDE':
        return int(s[0:2]) + float(s[2:]) / 60
    elif f == 'N/S':
        return s
    elif f == 'LONGITUDE':
        return int(s[0:3]) + float(s[3:]) / 60
    elif f == 'E/W':
        return s
    elif f == 'SPEED':
        return int(s)
    elif f == 'COURSE':
        return int(s)
    elif f == 'ALTITUDE':
        return int(s)
    elif f == 'ODOMETER':
        return int(s)
    elif f == 'IO_STATUS':
        return int(s)
    elif f == 'EVENT_ID':
        return int(s)
    elif f == 'AIN1':
        return float(s)
    elif f == 'AIN2':
        return float(s)
    elif f == 'FIX_MODE':
        return int(s)
    elif f == ('%s_SAT_NO' % SGK_T):
        return int(s)
    elif f == 'GPS_SAT_NO':
        return int(s)
    elif f == 'HDOP':
        return float(s)


def convert_sgk_t(s: str = '', sep: str = ',') -> dict:
    """
    :return: converted dict from sgk string format to dict
    """

    s = s[:-1]
    data = s.split(sep)
    output = {}

    form = ['DEVICE_ID', 'DATE', 'TIME', 'LATITUDE', 'N/S', 'LONGITUDE', 'E/W',
              'SPEED', 'COURSE', 'ALTITUDE', 'ODOMETER', 'IO_STATUS', 'EVENT_ID', 'AIN1', 'AIN2',
              'FIX_MODE', ('%s_SAT_NO' % SGK_T), 'GPS_SAT_NO', 'HDOP']

    # TODO: FIX REPORT TEST
    # t = data[0]
    # if t != '&REPORT':
    #    raise ValueError

    for i, f in enumerate(form):
        if data[i + 1] != '':

            try:
                output[f] = sgk_t_format(data[i + 1], f)
            except:
                raise ValueError

    return output


def load_file_format(filename: str = "", f: str = "") -> list:
    """
    :param filename: file which consists rows
    :param f: format of file
    :return: list of dicts
    """

    if f not in FORMATS:
        raise ValueError

    try:
        c = []
        with open(filename, encoding='utf8') as file:
            if f == SGK_T:
                for line in file:
                    d = convert_sgk_t(line[:-1])
                    c.append(d)
            elif f == NMEA:
                pass

        return c
    except:
        raise ValueError


def upload_file_format(filename: str = "", f: str = ""):
    """
    :param filename: new file
    :param f: format of file
    :return: list of dicts
    """
    pass
    if f not in FORMATS:
        raise ValueError

    try:
        c = []
        with open(filename, encoding='utf8') as file:
            if f == "SGK_T":
                for line in file:
                    d = convert_sgk_t(line[:-1])
                    c.append(d)

        return c
    except:
        raise ValueError


def file_print_sgk_t(filename: str = ""):

    try:
        with open(filename, encoding='utf8') as f:
            for line in f:
                d = convert_sgk_t(line[:-1])
                for k, v in d.items():
                    print(k, ':', v)
                print()
                key = input()
                if key == 'q':
                    return

    except:
        print("DURING PROGRAM ERROR WAS OCCUR")
'''