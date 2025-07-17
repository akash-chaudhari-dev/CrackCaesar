from flask import Flask, render_template, request
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))  # default 5000 for local testing

def ecrypter(text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    results = []

    for key in range(0, 26):  # 1 to 25
        encrypted_text = ""
        for char in text.lower():
            if char in letters:
                index = (letters.index(char) + key) % 26
                encrypted_text += letters[index]
            else:
                encrypted_text += char  # Keep spaces, punctuation, numbers etc.
        results.append((key, encrypted_text))

    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    processed_texts = None

    if request.method == 'POST':
        user_text = request.form['user_text']
        processed_texts = ecrypter(user_text)

    return render_template('index.html', processed_texts=processed_texts)

if __name__ == "__main__":
    app.run(debug=True)
