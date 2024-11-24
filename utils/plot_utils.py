import matplotlib.pyplot as plt

def plot_gold_prices(data):
    """Plot gold prices over time."""
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Price'], label='Gold Price')
    plt.xlabel('Date')
    plt.ylabel('Price (RON)')
    plt.title('Gold Prices Over Time')
    plt.legend()
    return plt
