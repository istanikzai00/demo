# POC Flask App

This is a simple Flask app that provides a web control panel to simulate CPU load.

## Features
- 🚀 Button to increase CPU load (triggers ASG scale out)
- 🛑 Button to stop CPU load (lets ASG scale in)
- Runs on port **5000**

## Run Locally
```bash
# Clone repo
git clone https://github.com/YOUR-USERNAME/my-flask-app.git
cd my-flask-app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py
