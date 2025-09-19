from flask import Flask, jsonify
import pipeline

app = Flask(__name__)

@app.route('/')
def index():
    return "pdoom-dashboard backend is running."

@app.route('/api/data')
def get_data():
    # Use pipeline to fetch, validate, and transform data
    data = pipeline.serve_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
