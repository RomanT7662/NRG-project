import os
import io
import base64
import requests
import matplotlib.pyplot as plt
from flask import Flask, render_template
from textblob import TextBlob
import nltk
nltk.download('punkt_tab', quiet=True)

app = Flask(__name__, template_folder='templates')

API_KEY = "33b57c0c6f7e4b41b487061f36da49a3"
BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news(country="us", category="technology"):
    """Gets list of news from NewsAPI.org."""
    params = {
        "country": country,
        "category": category,
        "apiKey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("articles", [])
    return []

def analyze_text(text):
    """We return polarity, subjectivity and key phrases."""
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return {
        "polarity": sentiment.polarity,
        "subjectivity": sentiment.subjectivity,
        "keywords": list(blob.noun_phrases)
    }

def create_plot(sentiments):
    """
    We build a histogram of polarity distribution,
    save it in a buffer and encode it in base64.
    """
    plt.figure(figsize=(8,6))
    plt.hist(sentiments, bins=20, color='skyblue', edgecolor='black')
    plt.title('Sentiment Polarity Distribution')
    plt.xlabel('Polarity')
    plt.ylabel('Frequency')
    plt.tight_layout()

    # Save the figure in a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)

    # Encode in base64 to embed in HTML
    encoded_img = base64.b64encode(buf.read()).decode('utf-8')
    return encoded_img

@app.route('/')
def index():
    # Get news and analyze it
    articles = fetch_news()
    analyses = []
    sentiments = []

    for article in articles:
        text = article.get('description') or article.get('title') or ""
        analysis = analyze_text(text)
        analyses.append(analysis)
        sentiments.append(analysis["polarity"])

    # Create a base64 image of the histogram
    encoded_plot = create_plot(sentiments)

    # Render the HTML template from the 'templates' folder
    return render_template(
        'index.html', 
        articles=articles, 
        analyses=analyses, 
        plot_data=encoded_plot,
        zip=zip  
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=True)
