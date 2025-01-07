from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/count', methods=['POST'])
def count_words():
    data = request.get_json()
    text = data.get('text', '')
    word_count = len(text.split())
    return jsonify(wordCount=word_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
