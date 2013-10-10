from app import app, db

@app.route('/')
def hello():
    return "HI!"