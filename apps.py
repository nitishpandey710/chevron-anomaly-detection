# app.py
import streamlit as st
import pandas as pd
from PIL import Image

# Load data
df = pd.read_csv("matched_anomalies_with_logs.csv", parse_dates=['anomaly_time', 'log_time'])


logo = Image.open("chevron.JPG")
st.image(logo, width=150)  # You can change the width as needed

st.set_page_config(page_title="Anomaly Log Matcher", layout="wide")
st.title(" Chevron :Anomaly to Operator Log Matching")
st.markdown("This dashboard shows matched anomalies with operator logs, similarity scores, and summaries.")

# Sidebar filters
st.sidebar.header("🔎 Filter Options")

# Equipment filter
equipment_options = sorted(df['equipment'].unique().tolist())
selected_equipment = st.sidebar.multiselect("Select Equipment(s)", options=equipment_options, default=equipment_options)

# Date range filter
min_date = df['anomaly_time'].min().date()
max_date = df['anomaly_time'].max().date()
selected_date = st.sidebar.date_input("Anomaly Date Range", [min_date, max_date])

# Similarity slider
similarity_cutoff = st.sidebar.slider("Minimum Similarity Score", min_value=0.0, max_value=1.0, value=0.4, step=0.05)

# Apply filters
filtered_df = df[
    (df['equipment'].isin(selected_equipment)) &
    (df['anomaly_time'].dt.date >= selected_date[0]) &
    (df['anomaly_time'].dt.date <= selected_date[1]) &
    (df['similarity'] >= similarity_cutoff)
]

# Show results
st.markdown(f"### 🧾 Showing {len(filtered_df)} matched records")
st.dataframe(filtered_df[['anomaly_time', 'equipment', 'log_message', 'summary', 'similarity']].sort_values(by='similarity', ascending=False), use_container_width=True)


# Download button
st.download_button("⬇ Download Filtered CSV", filtered_df.to_csv(index=False), file_name="filtered_matched_logs.csv")
