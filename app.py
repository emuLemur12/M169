from flask import Flask, render_template
from backend import get_users

app = Flask(__name__)

@app.route('/')
def hello():
    user_display_names = get_users('G_BVD_VMWare-HorizonClient 8.5.0.26981')
    return render_template('index.html', users=user_display_names)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
