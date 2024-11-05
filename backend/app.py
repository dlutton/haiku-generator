from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the POST request
    data = request.json  # Assuming the frontend is sending JSON data
    input_text = data.get('input', '')  # Retrieve the input value

    if input_text:
        # Here you can process the input text if necessary
        # For now, let's just send it back in the response
        response = {'message': f'Input received: {input_text}'}
        return jsonify(response), 200
    else:
        return jsonify({'error': 'No input provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
