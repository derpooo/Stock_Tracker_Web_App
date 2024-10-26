# Stock Tracker Web App

This is a simple web-based stock tracker app built with **Flask** and **Matplotlib**. The app allows users to input a stock ticker and date range, fetches historical stock price data from Yahoo Finance using **yfinance**, and plots the stock price trend over time.

## Features

- User-friendly web interface to enter stock ticker and date range.
- Fetches historical stock price data from Yahoo Finance.
- Displays a line plot of stock prices over the selected time period.
- Clean and consistent design using a basic CSS file.
- The stock plot is generated dynamically and displayed on the result page.

## Tech Stack

- **Python 3.9+**
- **Flask**: Lightweight web framework for building the app.
- **Matplotlib**: For creating and saving stock price plots.
- **yfinance**: For fetching historical stock data.
- **HTML/CSS**: For the user interface.

## Setup Instructions

### Prerequisites

- Python 3.9 or higher
- `pip` (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/stock-tracker-app.git
   cd stock-tracker-app
   
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Run the app:**
   ```bash
   python app.py
   
5. **Open your browser and navigate to http://127.0.0.1:5000/.**

## Usage

1. Enter the stock ticker symbol (e.g., AAPL for Apple) and the desired date range in the form.
2. Submit the form to view the stock price plot for the specified date range.
3. A dynamically generated plot will be displayed showing the stock prices over time.

## Example Workflow

- Enter stock ticker: AAPL
- Select a start date: 2023-01-01
- Select an end date: 2023-12-31
- Click "Submit"
- The app will fetch historical stock prices from Yahoo Finance, generate a plot, and display it on the results page.

## Screenshots

**Index Page**
![1](https://github.com/user-attachments/assets/52d482d9-98c6-42c0-b1cd-93387477ec9d)

**Result Page**
![2](https://github.com/user-attachments/assets/519f1c0c-d097-4db2-b060-3648469d7300)

## Dependencies

The dependencies are listed in the requirements.txt file. To install them, simply run:
   ```bash
   pip install -r requirements.txt
   ```

**Main libraries:**

- `Flask`: Web framework for building the interface.
- `Matplotlib`: For plotting stock price charts.
- `yfinance`: To fetch historical stock price data.

## License

This project is licensed under the MIT License.

## Future Features

- Integration of technical indicators like RSI and Bollinger Bands.
- Price alerts, portfolio tracking, and news feed.


