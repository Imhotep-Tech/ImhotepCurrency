import sys
import os

os.environ['EXCHANGE_API_KEY_PRIMARY'] = '12644ad30490895a4ffd9844'
os.environ['EXCHANGE_API_KEY_SECONDARY'] = '970289727569e4224d9109fc'

# Add the directory containing your Flask application to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Assuming your Flask application is named 'app' and the Flask instance is created in 'app.py'
from app import app as application  # Replace 'app' with the actual name of your Flask instance

# This will be the entry point for WSGI servers like Gunicorn
if __name__ == "__main__":
    application.run()
