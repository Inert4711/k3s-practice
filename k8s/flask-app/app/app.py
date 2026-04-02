from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to Production-Ready K8s App!",
        "status": "ok",
        "environment": "kubernetes"
    })

@app.route('/api/health')
def health():
    return jsonify({
        "status": "healthy",
        "version": "1.0.1",  
        "timestamp": "2026-03-17T12:00:00Z"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)