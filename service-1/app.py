from flask import Flask, render_template 
import requests

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
   combo = requests.get("http://service-4:5003/backend")  
   return render_template('index.html', combo=combo.text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
