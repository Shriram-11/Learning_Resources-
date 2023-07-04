import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock price dataset
df = pd.read_csv('all_stocks_5yr.csv')

# Convert the 'date' column to datetime data type
df['date'] = pd.to_datetime(df['date'])

# Select a specific stock
stock_name = 'AAL'
stock_data = df[df['Name'] == stock_name].reset_index(drop=True)

# Extract historical closing prices
closing_prices = stock_data['close']

# Calculate daily returns
returns = np.log(closing_prices / closing_prices.shift(1)).dropna()

# Calculate average daily return and standard deviation
mu = returns.mean()
sigma = returns.std()

# Define parameters for the simulation
num_simulations = 1000
forecast_horizon = len(pd.date_range(start='2020-01-01', end='2020-12-31', freq='B'))  # Number of trading days in 2020

# Perform Monte Carlo simulation
simulated_prices = pd.DataFrame(index=range(forecast_horizon), columns=range(num_simulations))
for i in range(num_simulations):
    # Generate random daily returns based on mean and standard deviation
    daily_returns = np.random.normal(mu, sigma, forecast_horizon)
    
    # Calculate the simulated price path
    price_path = closing_prices.iloc[-1] * np.exp(np.cumsum(daily_returns))
    
    # Store the simulated price path in the DataFrame
    simulated_prices[i] = price_path

# Calculate predicted future prices
predicted_prices = simulated_prices.mean(axis=1)

# Plot the historical prices and predicted future prices
plt.figure(figsize=(10, 6))
plt.plot(stock_data['date'], closing_prices, label='Historical Prices')
plt.plot(pd.date_range(start='2020-01-01', end='2020-12-31', freq='B'), predicted_prices, label='Predicted Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Monte Carlo Simulation: Predicted Stock Prices for {}'.format(stock_name))
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
