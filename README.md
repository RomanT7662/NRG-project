# TrendEyes
This project is designed to collect global news, perform sentiment analysis on the articles, and display the results on a web interface. I built it using Python, Flask, NewsAPI, TextBlob, and Matplotlib.

# 📋 Features
- 🇺🇸 US News Collection: Retrieves up-to-date news articles from around the world using the NewsAPI.
- 🔍 Sentiment Analysis: Uses TextBlob to analyze the sentiment (polarity and subjectivity) and extract key phrases from each article.
- 📊 Data Visualization: Generates a histogram that visualizes the distribution of sentiment polarity with Matplotlib.
- 🌐 Web Interface: Displays news articles, sentiment scores, and the histogram in a user-friendly Flask web application.
# 🛠️ Installation and Setup
- Clone the repository
- Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
- Install dependencies:
pip install -r requirements.txt
- Download necessary TextBlob corpora:
python -m textblob.download_corpora
- Run the application:
python main.py
- Open your browser:
Visit https://8c40504d-a382-4977-b397-e216c106475a-00-14sh8lattfdzp.spock.replit.dev/ to see the project in action.

# ⚙️ Dependencies
Flask — for creating the web server and rendering the web interface.
Requests — for making HTTP requests to NewsAPI.
TextBlob — for sentiment analysis and key phrase extraction.
Matplotlib — for generating visualizations (the sentiment histogram).
# 🚀 How to Use
Run the application using python main.py.
Open your web browser and navigate to https://8c40504d-a382-4977-b397-e216c106475a-00-14sh8lattfdzp.spock.replit.dev/.
View the latest global news articles along with their sentiment scores and key phrases, and check out the sentiment distribution histogram.
# 📝 License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.

# 💡 Ideas for Improvement
Add filters to view news by categories or specific regions.
Implement time-series analysis to track changes in sentiment over time.
Enhance the visualization with interactive charts.
Provide options for users to customize search queries or sentiment thresholds.

Made with ❤️ for coding.
