# plotter.py
import matplotlib.pyplot as plt

def plot_exchange_rates(rates):
    plt.figure(figsize=(10, 5))
    plt.plot(rates, marker='o')
    plt.title('UAH to USD Exchange Rate From 2000 to 2023')
    plt.xlabel('Years since 2000')
    plt.ylabel('Exchange Rate (UAH to USD)')
    plt.xticks(range(len(rates)), range(2000, 2000 + len(rates)))
    plt.grid(True)
    plt.show()
