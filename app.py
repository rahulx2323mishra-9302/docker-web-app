from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.close()
        return "✅ Flask App Connected to PostgreSQL via Docker Compose"
    except Exception as e:
        return f"❌ Database Connection Failed: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)