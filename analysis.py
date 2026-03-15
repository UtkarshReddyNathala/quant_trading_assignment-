import numpy as np
import matplotlib.pyplot as plt


def performance_metrics(results):

    r = results["returns"]

    total_return = results["equity"].iloc[-1] - 1

    annual_return = (1 + total_return) ** (252) - 1

    sharpe = np.sqrt(252 * 390) * r.mean() / r.std()

    peak = results["equity"].cummax()

    drawdown = (results["equity"] - peak) / peak

    max_dd = drawdown.min()

    win_rate = (r > 0).sum() / len(r)

    metrics = {

        "Total Return": total_return,
        "Annual Return": annual_return,
        "Sharpe Ratio": sharpe,
        "Max Drawdown": max_dd,
        "Win Rate": win_rate
    }

    return metrics, drawdown


def plot_results(price, spread, signals, results, drawdown):

    plt.figure(figsize=(10,4))
    plt.plot(spread)
    plt.title("Spread")
    plt.savefig("results/spread.png")


    plt.figure(figsize=(10,4))
    plt.plot(results["equity"])
    plt.title("Equity Curve")
    plt.savefig("results/equity_curve.png")


    plt.figure(figsize=(10,4))
    plt.plot(drawdown)
    plt.title("Drawdown Curve")
    plt.savefig("results/drawdown_curve.png")


    plt.figure(figsize=(10,4))
    plt.plot(price)

    buy = signals["long"]
    sell = signals["short"]

    plt.scatter(price.index[buy], price[buy], marker="^")
    plt.scatter(price.index[sell], price[sell], marker="v")

    plt.title("Trading Signals")

    plt.savefig("results/signals.png")
