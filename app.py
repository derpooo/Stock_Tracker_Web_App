# Import necessary libraries
import yfinance as yf
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for
import os

# Create a Flask instance
app = Flask(__name__)

# Step 1: Define a function to fetch stock data
def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Step 2: Define a function to plot stock prices and save the figure
def plot_stock_prices(stock_data, ticker):
    plt.figure(figsize=(10, 5))
    stock_data['Close'].plot(label=f'{ticker} Close Price', color='blue')

    # Calculate and plot moving averages
    stock_data['50_MA'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['200_MA'] = stock_data['Close'].rolling(window=200).mean()

    stock_data['50_MA'].plot(label='50-Day MA', color='green')
    stock_data['200_MA'].plot(label='200-Day MA', color='red')

    plt.title(f'{ticker} Stock Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)

    # Save the plot to a file in the static folder
    file_name = f'{ticker}_plot.png'
    file_path = os.path.join('static', file_name)
    plt.savefig(file_path)
    plt.close()  # Close the plot to avoid overwriting in the next request

    return file_name

# Step 3: Create a route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the form data
        ticker = request.form['ticker'].upper()
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        # Fetch stock data and plot it
        stock_data = fetch_stock_data(ticker, start_date, end_date)
        plot_filename = plot_stock_prices(stock_data, ticker)

        # Redirect to the result page with the stock plot
        return render_template('result.html', ticker=ticker, plot_filename=plot_filename)

    return render_template('index.html')

# Step 4: Create a result route to display the plot
@app.route('/result')
def result():
    return render_template('result.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
