import datetime
import numpy as np
from AppAdaptor import *


class StatCounter:

    def __init__(self):
        pass

    def convert(self, form: Format, values: list) -> np.array:

        p = []
        for el in values:

            try:
                h = form.value(el["GPGGA"]["MSL_ALTITUDE"], "MSL_ALTITUDE")
            except:
                h = 0
            try:
                l = form.value(el["GPGGA"]["LONGITUDE"], "LONGITUDE")
            except:
                l = 0
            try:
                phi = form.value(el["GPGGA"]["LATITUDE"], "LATITUDE")
            except:
                phi = 0

            if phi or h or l:
                vec = np.array([phi, l, h])
                p.append(vec)

        if not p:
            raise ValueError("Don't find any real value in file")

        return np.array(p)

    def count_alredy_transformed(self, values, f: str = ""):

        if f == Nmea.name():

            p = values
            # p.shape = N * 3
            n = p.shape[0]

            p_mean = p.mean(axis=0, keepdims=True)
            # p_mean.shape = 1 * 3

            delta_p = p - p_mean
            # delta_p.shape = N * 3

            K = np.zeros([3, 3])
            for vec in delta_p:
                vec = np.expand_dims(vec, axis=1)
                test = np.dot(vec, vec.T)
                K += test

            K /= n
            # K.shape = 3 * 3
            SKO = np.sqrt(np.diag(K))
            fake_SKO = SKO.copy()
            for i in range(fake_SKO.shape[0]):
                if fake_SKO[i] == 0:
                    fake_SKO[i] = 1

            REV_SKO = np.diag(1 / fake_SKO)
            f = np.dot(REV_SKO, K)
            R = np.dot(f, REV_SKO)
            Q = np.sum((delta_p > (3 * SKO)), axis=0)

            stat_info = {
                "MEAN": p_mean[0],
                "COV_MATRIX": K,
                "SKO": SKO,
                "FAKE_SKO": fake_SKO,
                "REV_SKO": REV_SKO,
                "COR_MATRIX": R,
                "More than 3 sigma": Q
            }

            return stat_info

    def count(self, values, f: str = ""):

        form = Factory.create(f)
        if f == Nmea.name():

            p = self.convert(form, values)
            return self.count_alredy_transformed(p, f)

    def count_comparing(self, v1, v2, f: str = ""):

        form = Factory.create(f)
        if f == Nmea.name():

            s1 = set([datetime.time(hour = el["GPGGA"]["TIME"].hour,
                                    minute=el["GPGGA"]["TIME"].minute,
                                    second=el["GPGGA"]["TIME"].second) for el in v1])
            s2 = set([datetime.time(hour=el["GPGGA"]["TIME"].hour,
                                    minute=el["GPGGA"]["TIME"].minute,
                                    second=el["GPGGA"]["TIME"].second) for el in v2])

            inter = s1.intersection(s2)

            new_v1 = []
            new_v2 = []
            for i in range(0, len(v1)):

                if datetime.time(hour = v1[i]["GPGGA"]["TIME"].hour,
                                    minute = v1[i]["GPGGA"]["TIME"].minute,
                                    second = v1[i]["GPGGA"]["TIME"].second) in inter:
                    new_v1.append(v1[i])

            for i in range(0, len(v2)):

                if datetime.time(hour = v2[i]["GPGGA"]["TIME"].hour,
                                    minute = v2[i]["GPGGA"]["TIME"].minute,
                                    second = v2[i]["GPGGA"]["TIME"].second) in inter:
                    new_v2.append(v2[i])

            renew_v1 = []
            renew_v2 = []
            for i in range(len(new_v1)):
                if (("MSL_ALTITUDE" in new_v1[i]["GPGGA"].keys() and "MSL_ALTITUDE" in new_v2[i]["GPGGA"].keys())
                or ("MSL_ALTITUDE" not in new_v1[i]["GPGGA"].keys() and "MSL_ALTITUDE" not in new_v2[i]["GPGGA"].keys())) and \
                (("LONGITUDE" in new_v1[i]["GPGGA"].keys() and "LONGITUDE" in new_v2[i]["GPGGA"].keys())
                or ("LONGITUDE" not in new_v1[i]["GPGGA"].keys() and "LONGITUDE" not in new_v2[i]["GPGGA"].keys())) and \
                (("LATITUDE" in new_v1[i]["GPGGA"].keys() and "LATITUDE" in new_v2[i]["GPGGA"].keys())
                or ("LATITUDE" not in new_v1[i]["GPGGA"].keys() and "LATITUDE" not in new_v2[i]["GPGGA"].keys())):

                    renew_v1.append(v1[i])
                    renew_v2.append(v2[i])

            p1 = self.convert(form, renew_v1)
            p2 = self.convert(form, renew_v2)
            p = p1 - p2
            return self.count_alredy_transformed(p, f)
