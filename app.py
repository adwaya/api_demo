from flask import Flask, jsonify

app = Flask(__name__)

info = [
    {
        'creator_name': 'adwaya',
        'version': '2.1',
        'species': 'humanoid',
        'entertainment': {
            'games': 'PUBG',
            'to-do': 'learning to think like a coder'
        }
    }
]

#GET /info
@app.route('/info')
def get_info():
    return jsonify({'info': info})

app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
