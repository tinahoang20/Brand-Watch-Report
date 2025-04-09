# 🚀 Brand Watch Report – Ogilvy Data Assignment

**Facebook + Instagram Performance Analysis** of **Coca-Cola**, **Pepsi** & **Fanta**  
📍 Vietnam | 🗓️ Nov 2024 – Mar 2025 | 💼 Built for Ogilvy Vietnam

---

![Brand Watch Dashboard](https://github.com/tinahoang20/Brand-Watch-Report/blob/main/assets/demo_dashboard.png)

---

## 📌 Project Overview

This project simulates a real-world marketing analysis challenge by **transforming raw social media data** into valuable insights and brand strategies.

✅ **Brands analyzed**: Coca-Cola Vietnam, Pepsi Vietnam, and Fanta Vietnam  
✅ **Platforms**: Facebook (public fan pages)  
✅ **Timeframe**: November 2024 – March 2025

---

## 📁 Folder Structure

```
Brand-Watch-Report/
├── data/                       # Cleaned & combined datasets
│   ├── crawl_coke_data.csv
│   ├── crawl_pepsi_data.csv
│   ├── crawl_fanta_data.csv
│   ├── content_analysis.csv
│   └── content_with_sentiment.csv
│
├── notebooks/                 # Modular notebooks per analysis step
│   ├── 01_crawl_script.ipynb
│   ├── 02_content_analysis.ipynb
│   ├── 03_brand_comparison.ipynb
│   ├── 04_sentiment_analysis.ipynb
│   └── 05_final_summary.ipynb
│
├── streamlit_app/             # Interactive dashboard app
│   └── app.py
│
├── assets/                    # Screenshots for README
│   └── demo_dashboard.png
│
├── requirements.txt
└── README.md
```

---

## ✨ Key Features

| Feature                 | Description |
|------------------------|-------------|
| 🔍 **Data Crawling**     | Scrape brand posts with Selenium from official pages |
| 📊 **Content Analysis**  | Word count, post type, hashtag frequency, posting time |
| 💬 **Sentiment Scoring** | TextBlob-based polarity classification |
| 📈 **Engagement Metrics**| Simulated metrics for likes, shares, comments |
| 🧠 **Strategic Insights**| Data-backed content & tone recommendations |
| 📱 **Streamlit Dashboard**| Real-time interactive filtering and insights |

---

## 💻 Streamlit Live Preview

> Coming soon via [Streamlit Cloud](https://streamlit.io/cloud)  
> (Or run locally below 👇)

```bash
# Run the dashboard locally
git clone https://github.com/tinahoang20/Brand-Watch-Report.git
cd Brand-Watch-Report
pip install -r requirements.txt
streamlit run streamlit_app/app.py
```

---

## 📊 Dashboard Preview

Here’s a quick look at the interactive dashboard:

![Streamlit App Demo](https://github.com/tinahoang20/Brand-Watch-Report/blob/main/assets/demo_dashboard.png)

---

## 🛠 Tech Stack

- **Python**: `pandas`, `numpy`, `seaborn`, `matplotlib`
- **Web Scraping**: `Selenium`
- **NLP**: `TextBlob`, `NLTK`
- **Dashboard**: `Streamlit`
- **Visualization**: `WordCloud`, `Plotly`, `Seaborn`

---

## 📈 Strategic Learnings (Examples)

| Brand | Strengths                            | Weaknesses                          | Strategy Suggestion                          |
|-------|--------------------------------------|-------------------------------------|----------------------------------------------|
| Coke  | Consistent tone, strong UGC          | Limited emotional storytelling      | Add more storytelling / campaign variety     |
| Pepsi | Engaging campaigns, strong visuals   | Slightly negative sentiment in some| Improve tone, personalize content            |
| Fanta | Fun tone, strong brand identity      | Less frequency, inconsistent formats| Standardize content, leverage trends         |

---

## 👩‍💻 About Me

Hi! I'm **Tina Hoàng**, a data-driven marketing analyst passionate about brand stories, digital strategy, and performance insights.

- 📬 [LinkedIn](https://www.linkedin.com/in/your-profile)
- 🐙 GitHub: [@tinahoang20](https://github.com/tinahoang20)
- ✉️ Email: tina.hoang20@example.com

---

## 🔐 Disclaimer

This project was created as part of a **recruitment test for Ogilvy Vietnam**.  
All content and brand mentions are used **purely for academic & demonstration purposes only**.


---


## 📬 Contact

Feel free to reach out via email or LinkedIn if you'd like to collaborate or ask anything about the project.

📨 tina.hoang20@example.com

🔗 https://github.com/tinahoang20

📧 Email: hngocanh357@gmail.com

🔗 LinkedIn: [Tina Hoang](https://www.linkedin.com/in/im-hoangngocanh)

---

