from flask import Flask, render_template
from routes.chat_routes import chat_bp
from routes.data_routes import data_bp

app = Flask(__name__, template_folder="templates", static_folder="static")

app.register_blueprint(chat_bp)
app.register_blueprint(data_bp)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
