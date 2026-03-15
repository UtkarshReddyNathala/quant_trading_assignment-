from data_loader import load_data, clean_data
from pair_selection import find_best_pair
from strategy import PairStrategy
from backtester import Backtester
from analysis import performance_metrics, plot_results


DATA_PATH = "data.csv"


def main():

    prices = load_data(DATA_PATH)

    prices = clean_data(prices)

    pair = find_best_pair(prices)

    print("Best Pair:", pair)

    strategy = PairStrategy()

    spread, signals = strategy.generate_signals(prices, pair[0], pair[1])

    backtester = Backtester()

    results = backtester.run(prices[pair[0]], signals)

    metrics, drawdown = performance_metrics(results)

    print("\nPerformance Metrics\n")

    for k, v in metrics.items():

        print(f"{k}: {v}")

    plot_results(prices[pair[0]], spread, signals, results, drawdown)


if __name__ == "__main__":
    main()
