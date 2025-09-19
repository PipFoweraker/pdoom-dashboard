# Backend Setup Guide

## Prerequisites
- Python 3.7 or newer
- pip (Python package manager)

## Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd pdoom-dashboard
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install flask
   ```

## Running the Backend
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. The backend will run at http://127.0.0.1:5000

## Notes
- This server is for development only. For production, use a WSGI server like Gunicorn or uWSGI.
- Debug mode is enabled by default for development.
