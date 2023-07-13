import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock price dataset
df = pd.read_csv('aaplldataset.csv') 

# Select a specific stock
stock_name = 'AAPL'  # Replace with the stock symbol you want to analyze
stock_data = df[df['Name'] == stock_name].reset_index(drop=True)

# Extract historical closing prices
closing_prices = stock_data['close']

# Calculate daily returns
returns = np.log(closing_prices / closing_prices.shift(1)).dropna()

# Calculate average daily return and standard deviation
mu = returns.mean()
sigma = returns.std()

# Define parameters for the simulation
simulations = 1000
forecast_horizon = 252  # Number of trading days in a year

# Perform Monte Carlo simulation
simulated_prices = pd.DataFrame()
for i in range(simulations):
    # Generate random daily returns based on mean and standard deviation
    daily_returns = np.random.normal(mu, sigma, forecast_horizon)
    
    # Calculate the simulated price path
    price_path = closing_prices.iloc[-1] * np.exp(np.cumsum(daily_returns))
    
    # Append the simulated price path to the DataFrame
    simulated_prices[i] = price_path

# Plot the historical prices and simulated price paths
# Plotting the simulated price paths
plt.figure(figsize=(10, 6))
for i in range(simulations):
    plt.plot(simulated_prices[i], alpha=0.3)

plt.xlabel("Time")
plt.ylabel("Price")
plt.title("Simulated Stock Price Paths")
plt.show()
