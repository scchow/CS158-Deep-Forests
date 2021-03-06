from load_data import load_data
from constants import *
import random
import numpy as np

from sklearn.base import BaseEstimator

class TitleFinder(BaseEstimator):
    def __init__(self, feature_names):
        self.feature_names = feature_names
        self.indices = {}

        title_words = ["martian", "gone", "girl", "goldfinch","shades", "grey", "gone", "girl", "fault", "stars", "unbroken", "train", "hunger", "games"]
        for title in title_words:
            if title in self.feature_names:
                self.indices[title] = self.feature_names.index(title)

    def fit(self, X, y):
        """
        does nothing for this simple baseline
        """
        return self

    def predict(self, X):
        n,d = X.shape
        y = np.zeros(n)

        for row in range(n):
            data = np.asarray(X[row,:].todense()).reshape([-1])
            if data[self.indices["martian"]] > 0:
                y[row] = 0
            elif data[self.indices["goldfinch"]] > 0:
                y[row] = 1
            elif data[self.indices["shades"]] > 0 and data[self.indices["grey"]] >0:
                y[row] = 2
            elif data[self.indices["gone"]] > 0 and data[self.indices["girl"]] > 0:
                y[row] = 3
            elif data[self.indices["fault"]] > 0 and data[self.indices["stars"]] > 0:
                y[row] = 4
            elif data[self.indices["unbroken"]] > 0:
                y[row] = 5
            elif data[self.indices["girl"]] > 0 and data[self.indices["train"]] > 0:
                y[row] = 6
            elif data[self.indices["hunger"]] > 0 and data[self.indices["games"]] > 0:
                y[row] = 7
            else:
                y[row] = random.randint(0,7)
                
        return y
            
            

    


