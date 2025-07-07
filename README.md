# chevron-anomaly-detection

# Chevron Equipment Anomaly Detection & Log Correlation

This project simulates a real-world use case of detecting sensor anomalies in oilfield equipment and matching them with operator log messages using Machine Learning and LLM-based summarization.

## Use Case Summary

- Simulates hourly sensor readings (temperature, pressure, vibration).
- Detects anomalies using IsolationForest.
- Generates operator logs related to equipment behavior.
- Matches logs to anomalies using time window, equipment, and semantic similarity.
- Summarizes matched logs using OpenAI GPT-3.5 via LangChain.
- Interactive dashboard built with Streamlit.
- 
## Project Structure

├── chevron_uc.ipynb # Main notebook
├── app.py # Streamlit UI
├── matched_anomalies.csv # Final output
├── requirements.txt # Python packages
└── README.md # Project overview


---

## 🚀 How to Run

Install requirements
pip install -r requirements.txt
streamlit run app.py

Kumar Nitish
Principal Data Scientist
Chevron Use Case Simulation
