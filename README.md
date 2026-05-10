# 📊 Superstore BI Dashboard

A retail analytics dashboard I built to practice the full data analyst workflow — 
from raw data to SQL queries to a live interactive dashboard.

## 🔗 Live Demo
👉 [Click here to open the dashboard](https://superstore-bi-dashboard-mjaz6ca4kvwzrpm5dxocmw.streamlit.app/)

## 💡 What I wanted to answer
Working on this project, I asked myself the kind of questions a real business analyst would:
- Which region is underperforming despite high sales volume?
- Which product categories are actually profitable vs just popular?
- Is there a seasonal pattern in revenue we can predict from?

## 🔍 What I found
- The **Central region** brings in decent revenue but has by far the lowest profit margin — a red flag worth investigating
- **Technology products** generate 45% of all profit while being only 36% of sales — the business should double down here
- **Office Supplies** is underrated — high profit margin, consistent demand
- Every year, revenue spikes in **Q4** — useful for inventory and staffing planning

## 🛠️ How I built it
I loaded the raw CSV into a SQLite database, wrote SQL queries to aggregate 
the key metrics, then built the dashboard in Streamlit with Plotly charts.

| Tool | What I used it for |
|------|--------------------|
| Python & Pandas | Cleaning and transforming the data |
| SQL / SQLite | Storing and querying aggregated metrics |
| Plotly | Building the interactive charts |
| Streamlit | Turning it all into a live web app |

## 🚀 Run it yourself
```bash
git clone https://github.com/Nedjmou07/superstore-bi-dashboard.git
cd superstore-bi-dashboard
pip install -r requirements.txt
streamlit run app.py
```

## 👋 About me
I'm Nedjemeddine, a Data Science graduate looking for opportunities in Europe.
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/nedjemeddine-agti-072662316/)!