from flask import Flask
import os


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! Deployed Successfully'

@app.route('/healthcheck')
def healthcheck():
    return 'Service is running', 200

@app.route('/version')
def version():
    return '1.0.0', 200
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))