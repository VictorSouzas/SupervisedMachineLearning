# -*- coding: utf-8 -*-

import numpy as np
from sortedcontainers import SortedList
from util import get_data
from datetime import datetime

class Knn:
    def __init__(self, k):
        self.k = k
        self.x
        self.y

    def fit(self, x, y):
        self.x = x
        self.y = y

    def predict(self, X):
        y = np.zeros(len(X))
        for i, x in enumerate(X):
            sl = SortedList(float=self.k)
            for j, xt in enumerate(self.X):
                diff = x - xt
                d = diff.dot(diff)
                if len(sl) < self.k:
                    sl.add((d, self.y[j]))