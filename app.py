import os
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

import task

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get('name', 'John doe')
    result = task.hello.delay(name)
    result.wait()
    return render_template('index.html', celery=result)

@app.route("/ping")
def salt_ping():
    result = task.ping.delay()
    result.wait()
    return 'ok',200 

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
