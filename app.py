from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, GitHub Team!"

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/dashboard')
def dashboard():
    return "Updated Dashboard API"

@app.route('/login')
def login():
    return "Login API"
