from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the POST request
    data = request.json  # Assuming the frontend is sending JSON data
    input_text = data.get('input', '')  # Retrieve the input value

    # time.sleep(5)  # Delay for 3 seconds to test progress bar

    if input_text:
        response = client.chat.completions.create(
            model="ft:gpt-4o-mini-2024-07-18:personal:haiku-generation:AZkP9YR5",
            messages=[
                {"role": "system", "content": "You are a 5-7-5 syllable structure haiku generator."},
                {
                    "role": "user",
                    "content": "Write a haiku based on {input_text} that follows the 5-7-5 syllable structure."
                }
            ],
            temperature=0.8,
            max_tokens=50
        )

        haiku = response.choices[0].message.content
        return jsonify({'message': haiku}), 200
    else:
        return jsonify({'error': 'No input provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
