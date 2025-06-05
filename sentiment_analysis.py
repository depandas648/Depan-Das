import re
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Sample Facebook Posts (Replace with actual data)
facebook_posts = [
    "I love the new features of this app! ❤️",
    "This is the worst experience ever! 😡",
    "The service was okay, but could be better.",
    "Absolutely fantastic! Best day ever! 😍",
    "I'm not sure if I like this or not."
]

# Function to clean text
def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r"@\w+|#\w+", "", text)  # Remove mentions and hashtags
    text = re.sub(r"[^\w\s]", "", text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    return text

# Function to get sentiment using VADER
def get_sentiment(text):
    score = analyzer.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Analyzing Sentiment of Facebook Posts
data = []
for post in facebook_posts:
    cleaned_text = clean_text(post)
    sentiment = get_sentiment(cleaned_text)
    data.append([post, sentiment])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Post", "Sentiment"])

# Display Sentiment Analysis Results
print(df)

# Plot Sentiment Distribution
sentiment_counts = df["Sentiment"].value_counts()
plt.figure(figsize=(6,4))
sentiment_counts.plot(kind="bar", color=["green", "red", "blue"])
plt.title("Sentiment Distribution of Facebook Posts")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()
