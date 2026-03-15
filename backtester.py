import numpy as np
import pandas as pd


class Backtester:

    def __init__(self, transaction_cost=0.0001):

        self.tc = transaction_cost


    def run(self, price, signals):

        returns = price.pct_change().fillna(0)

        vol = returns.rolling(500).std()

        position = np.zeros(len(price))

        for i in range(1, len(price)):

            if signals["long"].iloc[i]:
                position[i] = 1 / (vol.iloc[i] + 1e-6)

            elif signals["short"].iloc[i]:
                position[i] = -1 / (vol.iloc[i] + 1e-6)

            elif signals["exit"].iloc[i]:
                position[i] = 0

            else:
                position[i] = position[i-1]

        strat_returns = position * returns

        costs = np.abs(np.diff(position, prepend=0)) * self.tc

        strat_returns = strat_returns - costs

        equity = (1 + strat_returns).cumprod()

        results = pd.DataFrame({

            "returns": strat_returns,
            "equity": equity,
            "position": position
        })

        return results
