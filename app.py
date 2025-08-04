from flask import Flask, render_template_string, redirect, url_for
import threading

app = Flask(__name__)

# Global vars for CPU load simulation
stress_thread = None
running = False

# Modern Styled Template
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>POC Control Panel</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Roboto', sans-serif;
      background: linear-gradient(135deg, #667eea, #764ba2);
      height: 100vh;
      margin: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      color: white;
    }
    .container {
      background: rgba(0, 0, 0, 0.6);
      padding: 40px;
      border-radius: 15px;
      text-align: center;
      box-shadow: 0 8px 16px rgba(0,0,0,0.3);
      width: 350px;
    }
    h2 {
      margin-bottom: 30px;
      font-weight: 700;
      font-size: 24px;
    }
    button {
      width: 100%;
      padding: 15px;
      margin: 10px 0;
      border: none;
      border-radius: 8px;
      font-size: 16px;
      font-weight: bold;
      cursor: pointer;
      transition: transform 0.2s, opacity 0.2s;
    }
    button:hover {
      transform: scale(1.05);
      opacity: 0.9;
    }
    .btn-start {
      background-color: #4CAF50; /* green */
      color: white;
    }
    .btn-stop {
      background-color: #E53935; /* red */
      color: white;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>POC Control Panel</h2>
    <form action="/start" method="post">
      <button type="submit" class="btn-start">🚀 Increase CPU Load</button>
    </form>
    <form action="/stop" method="post">
      <button type="submit" class="btn-stop">🛑 Stop CPU Load</button>
    </form>
  </div>
</body>
</html>
"""

# Worker function to simulate CPU load
def cpu_stress():
    global running
    while running:
        _ = [x**2 for x in range(10_000)]

@app.route("/")
def index():
    return render_template_string(TEMPLATE)

@app.route("/start", methods=["POST"])
def start_load():
    global stress_thread, running
    if not running:
        running = True
        stress_thread = threading.Thread(target=cpu_stress)
        stress_thread.start()
    return redirect(url_for("index"))

@app.route("/stop", methods=["POST"])
def stop_load():
    global running
    running = False
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
