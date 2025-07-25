[![Render](https://img.shields.io/badge/Hosted%20on-Render-blue)](https://crackcaesar.onrender.com/)
# CrackCaesar


> A minimal Flask web app to decode Caesar cipher messages into plaintext.

---

## 🔍 What is CrackCaesar?

CrackCaesar is a lightweight web interface that takes a Caesar-encrypted message and converts it into readable plaintext using brute-force or shift-based logic.

---

## 🚀 Features

- 🌐 Simple web UI built with Flask
- 🔓 Brute-force Caesar cipher decoding (all 25 shifts)
- ✏️ Optional: Input known shift value (if you know it)
- 📜 Clean, minimal output for readability

---

## 🛠️ Tech Stack

- Python 3
- Flask
- HTML/CSS (minimal)

---

## 📂 Project Structure

```

/CrackCaesar/
├── app.py            # Main Flask app
├── templates/
│   └── index.html    # Web frontend
└── README.md

````

---

## ⚙️ How to Run Locally

1. **Clone the Repo**

```bash
git clone https://github.com/akash1512485/CrackCaesar
cd CrackCaesar
````

2. **Create a Virtual Environment**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the App**

```bash
python app.py
```

Then open your browser at `http://127.0.0.1:5000/`.

---

## 🧠 How It Works

* If no shift is provided: the app attempts all 25 possible Caesar shifts and shows all possible plaintexts.
* If a shift is given: it directly decrypts using that shift.

---

## 📝 Future Improvements

* Detect English words to auto-pick most likely plaintext
* Add dark mode toggle
* Add encryption mode (reverse functionality)


---

> Made with 💻 by Akash Chaudhari
