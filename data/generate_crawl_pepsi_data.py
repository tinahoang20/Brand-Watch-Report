import pandas as pd
from datetime import datetime, timedelta
import random
from textblob import TextBlob
import os

# Setup
BRAND = "Pepsi"
START_DATE = datetime(2024, 11, 1)
END_DATE = datetime(2025, 3, 31)
PLATFORMS = ["Facebook", "Instagram", "YouTube"]
NUM_POSTS = 30
os.makedirs("data", exist_ok=True)

# Functions
def get_sentiment(text):
    score = TextBlob(text).sentiment.polarity
    if score > 0.1:
        return "Positive"
    elif score < -0.1:
        return "Negative"
    else:
        return "Neutral"

def guess_post_type(platform):
    if platform == "YouTube": return "video"
    if platform == "Instagram": return random.choice(["reel", "image", "video"])
    return random.choice(["text", "image", "video"])

# Generate mock data
data = []
for i in range(NUM_POSTS):
    platform = random.choice(PLATFORMS)
    post_date = START_DATE + timedelta(days=random.randint(0, (END_DATE - START_DATE).days))
    text = f"This is a mock post #{i} by {BRAND} on {platform} with promotional content."
    likes = random.randint(200, 2000)
    comments = random.randint(10, 200)
    shares = random.randint(5, 100) if platform != "Instagram" else 0
    reactions = likes + comments + shares
    post_type = guess_post_type(platform)
    sentiment = get_sentiment(text)

    data.append({
        "brand": BRAND,
        "platform": platform,
        "post_id": f"{platform[:2].lower()}_{i}",
        "time": post_date.strftime("%Y-%m-%d %H:%M:%S"),
        "content": text,
        "likes": likes,
        "comments": comments,
        "shares": shares,
        "reactions": reactions,
        "post_type": post_type,
        "sentiment": sentiment,
        "post_url": f"https://{platform.lower()}.com/{BRAND.lower()}/post/{i}"
    })

# Export
df = pd.DataFrame(data)
df = df.sort_values(by="time")
df.to_csv("data/crawl_pepsi_data.csv", index=False, encoding="utf-8-sig")

print("✅ Mock crawl_pepsi_data.csv created successfully.")
