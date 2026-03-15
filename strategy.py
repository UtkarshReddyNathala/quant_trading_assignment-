import pandas as pd


class PairStrategy:

    def __init__(self, entry=2, exit=0.5, window=500):

        self.entry = entry
        self.exit = exit
        self.window = window


    def rolling_beta(self, y, x):

        cov = y.rolling(self.window).cov(x)
        var = x.rolling(self.window).var()

        return cov / var


    def generate_signals(self, prices, a, b):

        A = prices[a]
        B = prices[b]

        beta = self.rolling_beta(A, B)

        spread = A - beta * B

        mean = spread.rolling(self.window).mean()
        std = spread.rolling(self.window).std()

        z = (spread - mean) / std

        signals = pd.DataFrame(index=prices.index)

        signals["zscore"] = z

        signals["long"] = z < -self.entry
        signals["short"] = z > self.entry
        signals["exit"] = abs(z) < self.exit

        return spread, signals
