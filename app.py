from flask import Flask, render_template, request
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))  # default 5000 for local testing

def decrypter(text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    results = []

    for key in range(1, 26):  # Try all possible shifts (1-25)
        decrypted_text = ""
        for char in text.lower():
            if char in letters:
                index = (letters.index(char) - key) % 26  # Note the minus sign for decryption
                decrypted_text += letters[index]
            else:
                decrypted_text += char
        results.append((key, decrypted_text))

    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    processed_texts = None

    if request.method == 'POST':
        user_text = request.form['user_text']
        processed_texts = decrypter(user_text)

    return render_template('index.html', processed_texts=processed_texts)

if __name__ == "__main__":
    app.run(debug=True)