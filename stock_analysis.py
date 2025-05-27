import yfinance as yf
import matplotlib.pyplot as plt

# 下載 TSMC 的股價資料
stock = yf.download("TSM", start="2020-01-01", end="2023-12-31")

# 取出調整收盤價
adj_close = stock["Close"]

# 計算年化報酬率
start_price = adj_close.iloc[0]
end_price = adj_close.iloc[-1]
years = (stock.index[-1] - stock.index[0]).days / 365
annual_return = ((end_price / start_price) ** (1 / years)) - 1

print(f"年化報酬率：約 {(annual_return * 100).item():.2f}%")


# 繪圖
adj_close.plot(title="TSMC Stock Price")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.tight_layout()
plt.show()

