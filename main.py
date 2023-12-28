import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock "closing  price" and ***volume*** of Google!
""" )

#define the ticker symbol
tickerSymbol='GOOGL'
#get data on this ticker
tickerData=yf.Ticker(tickerSymbol)
#get historical prices for this ticker
tickerDF=tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
#see your data
tickerDF
#open High Low Close Volume Dividends Stock Spilts
st.write("""
## Closing  price vs Year
""" )
st.line_chart(tickerDF.Close)
st.write("""
## Volume vs Year
""" )
st.line_chart(tickerDF.Volume)
