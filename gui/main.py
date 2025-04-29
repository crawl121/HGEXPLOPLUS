from flask import Flask, render_template, request, redirect, url_for
import os
import threading
from core.ssh_engine import start_attack
from utils.session import load_wordlists

app = Flask(__name__)

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output', 'success.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    ip_path = request.form['targets']
    user_path = request.form['userlist']
    pass_path = request.form['passlist']
    threads = int(request.form.get('threads', 5))
    port = int(request.form.get('port', 22))
    os_type = request.form.get('os', 'linux')
    payload = True if request.form.get('payload') == 'on' else False

    ip_list = load_wordlists(ip_path)
    user_list = load_wordlists(user_path)
    pass_list = load_wordlists(pass_path)

    # Run SSH attack in a background thread
    threading.Thread(target=start_attack, args=(ip_list, user_list, pass_list, port, threads, os_type, payload)).start()

    return render_template('result.html', message="Attack Started! Check output/success.json for results.")

if __name__ == '__main__':
    app.run(debug=True)
