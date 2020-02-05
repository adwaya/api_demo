from flask import Flask, jsonify

app = Flask(__name__)

info = [
    {
        'service_name': 'myapplication',
        'version': '1.0.0',
        'git_commit_sha': '2a9daebb29f4f5df31cd263a8c5b1082d7c7bcf9',
        'environment': {
            'service_port': '8080',
            'log_level': 'INFO'
        }
    }
]

#GET /info
@app.route('/info')
def get_info():
    return jsonify({'info': info})

app.run(port=5000)
