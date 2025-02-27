from flask import Flask, render_template, request, session
import requests
import time

# Google Custom Search API Credentials
API_KEY = "YOUR_API"
CX = "YOUR_CX"

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Session tracking

# Function to enforce daily query limit
def check_query_limit():
    if "query_count" not in session:
        session["query_count"] = 0
        session["last_query_time"] = time.time()

    # Reset the query count after 24 hours
    if time.time() - session["last_query_time"] > 86400:  # 86400 seconds = 24 hours
        session["query_count"] = 0

    if session["query_count"] >= 100:
        return False  # Limit reached, deny further queries
    session["query_count"] += 1
    session["last_query_time"] = time.time()
    return True  # Allow query

# Function to check if news exists online
def check_news_online(query):
    if not check_query_limit():
        return "❌ Daily query limit reached. Please try again tomorrow."

    search_url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}"
    response = requests.get(search_url)
    results = response.json()

    if "items" in results:
        return "✅ The news was found online! It is likely real."
    return "❌ No results found. This news might be fake."

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        news_text = request.form.get("news_text")
        if news_text:
            result = check_news_online(news_text)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
