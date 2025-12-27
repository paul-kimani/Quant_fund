import streamlit as st
import yfinance as yf
import pandas as pd
import altair as alt

# 1. SECURITY CHECK (Must be at the top)
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⛔ Access Restricted. Please log in first.")
    st.stop()

# NOTE: Do NOT use st.set_page_config here. It is inherited from app.py.

st.title("📊 Stock Peer Analysis")

# --- SUBLINKS / NAVIGATION ---
view_mode = st.sidebar.radio(
    "🔎 Analysis Module",
    ["Price Performance", "Correlation Matrix", "Raw Data Inspector"]
)

st.caption(f"Module: {view_mode}")

# --- GLOBAL CONFIG ---
STOCKS = ["AAPL", "AMD", "AMZN", "GOOGL", "META", "MSFT", "NVDA", "TSLA", "JPM", "V"]
DEFAULT_STOCKS = ["NVDA", "AMD", "MSFT"]

if "tickers_input" not in st.session_state:
    st.session_state.tickers_input = DEFAULT_STOCKS

# --- CONTROLS ---
col_controls, col_display = st.columns([1, 4])

with col_controls:
    tickers = st.multiselect("Select Tickers", options=STOCKS, default=st.session_state.tickers_input)
    horizon = st.selectbox("Time Horizon", ["1mo", "3mo", "6mo", "1y", "5y"], index=2)

if not tickers:
    st.warning("Select at least one ticker.")
    st.stop()

# --- DATA LOADING (Shared) ---
@st.cache_data(ttl=3600)
def load_data(symbol_list, period):
    # Added group_by='ticker' to ensure consistent formatting for single vs multiple tickers
    data = yf.download(symbol_list, period=period, progress=False)['Close']
    
    # Handle single ticker return structure (Series -> DataFrame)
    if isinstance(data, pd.Series):
        data = data.to_frame(name=symbol_list[0])
        
    # Drop empty columns and fill gaps
    data = data.dropna(axis=1, how='all')
    data = data.ffill().bfill()
    
    # Ensure the index is named 'Date' for the Altair chart later
    data.index.name = 'Date'
    
    return data

try:
    with st.spinner("Fetching market data..."):
        data = load_data(tickers, horizon)
        
    if data.empty:
        st.error("No data returned. Market API might be down or tickers are invalid.")
        st.stop()

    # Normalization (Rebase to 0%)
    normalized = (data / data.iloc[0]) - 1

    # --- VIEW 1: PRICE PERFORMANCE ---
    if view_mode == "Price Performance":
        # Metrics Logic
        with col_controls:
            st.markdown("### 🏆 Leaders")
            # Sort by total return
            final_returns = normalized.iloc[-1].sort_values(ascending=False)
            
            for stock, ret in final_returns.items():
                # Get the raw price for the metric
                current_price = data[stock].iloc[-1]
                st.metric(stock, f"${current_price:.2f}", f"{ret:.2%}")

        # Chart Logic
        with col_display:
            st.subheader("Relative Returns (Rebased to 0%)")
            
            # Reset index to make Date a column for Altair
            chart_data = normalized.reset_index().melt('Date', var_name='Ticker', value_name='Return')
            
            c = alt.Chart(chart_data).mark_line().encode(
                x='Date:T',
                y=alt.Y('Return', axis=alt.Axis(format='%')),
                color='Ticker',
                tooltip=['Date', 'Ticker', alt.Tooltip('Return', format='.2%')]
            ).properties(height=500, title="Performance Comparison")
            
            st.altair_chart(c, use_container_width=True)

    # --- VIEW 2: CORRELATION MATRIX ---
    elif view_mode == "Correlation Matrix":
        with col_display:
            st.subheader("🔗 Asset Correlations")
            st.markdown("""
            * **1.0 (Green):** Assets move perfectly together.
            * **-1.0 (Red):** Assets move in opposite directions (Hedge).
            """)
            
            # Calculate Correlation of daily returns
            corr_matrix = data.pct_change().corr()
            
            # Display with heatmap styling
            st.dataframe(
                corr_matrix.style.background_gradient(cmap="RdYlGn", axis=None, vmin=-1, vmax=1),
                use_container_width=True,
                height=400
            )

    # --- VIEW 3: RAW DATA ---
    elif view_mode == "Raw Data Inspector":
        with col_display:
            st.subheader("🔢 Historical Close Prices")
            st.dataframe(data.sort_index(ascending=False), use_container_width=True)
            
            # Download Option
            csv = data.to_csv().encode('utf-8')
            st.download_button(
                "📥 Download CSV",
                csv,
                "market_data.csv",
                "text/csv"
            )

except Exception as e:
    st.error(f"Error loading data: {e}")