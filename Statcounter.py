import numpy as np


class NavigationSignalReceiver:

    def __init__(self, values=None):
        self.values = values

    def set_values(self, values):
        self.values = values

    def count(self):
        pass

    def get_corr_matrix(self):
        pass

    def get_cov_matrix(self):
        pass

    def get_q(self):
        pass

