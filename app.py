from flask import Flask
import os
import subprocess
import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Your full name (replace with your actual name)
    full_name = "Pratik Kumar"

    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"

    # Get current time in IST
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")

    # Get the top command output (first 10 lines)
    try:
        top_output = subprocess.check_output("top -b -n 1 | head -10", shell=True, text=True)
    except Exception as e:
        top_output = f"Error fetching top output: {e}"

    # Render response as HTML
    return f"""
    <html>
        <head><title>Htop Info</title></head>
        <body>
            <h1>System Info</h1>
            <p><strong>Name:</strong> {full_name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <h2>Top Output:</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
