# 🔐 Secure Password Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-High%20Entropy-red?style=for-the-badge)

> **"Security starts with a strong password."**

A lightweight, command-line interface (CLI) tool designed to generate cryptographically strong passwords. This utility helps users create high-entropy credentials to protect their digital assets against brute-force attacks.

---

## 🚀 Features

* **High Entropy:** Generates passwords using a mix of uppercase, lowercase, numbers, and special symbols.
* **Customizable Length:** Users can define the password length (Default: 12 characters).
* **Smart Validation:** Ensures that the generated password contains at least one character from each category.
* **Multiple Options:** Generates 3 different password variations at once for user convenience.
* **Error Handling:** Robust input validation to prevent crashes.

---

## 🛠️ Installation & Usage

You don't need to install any external libraries. Just clone the repo and run it!

### 1. Clone the Repository
```bash
git clone [https://github.com/willbyers1/secure-password-generator.git](https://github.com/willbyers1/secure-password-generator.git)
cd secure-password-generator
Run the Script
python secure_pass.py
```
📸 Preview
Here is how the tool looks in action:

Plaintext
--- 🔒 Secure Password Generator (By Will) ---
Generates high-entropy passwords for better security.

Enter password length (Default: 12): 16

Generated Passwords:
------------------------------
Option 1: 9#mK$pL2@nQz!xR4
Option 2: aB7&yU1%wE9*rT5^
Option 3: Zx3(cV4)bN5?mM6<
------------------------------
Tip: Keep your passwords safe and use a manager!
🧠 Code Logic
The script utilizes Python's random and string modules to ensure randomness:

Character Pools: Creates lists for Letters (A-Z, a-z), Digits (0-9), and Symbols (!@#...).

Mandatory Inclusion: Forces the inclusion of at least one character from each pool to meet complexity requirements.

Shuffling: Uses random.shuffle() to prevent predictable patterns.

🔜 Future Improvements (To-Do)
[ ] Add a Graphical User Interface (GUI) with Tkinter.

[ ] Add an option to save passwords to an encrypted file.

[ ] Allow users to exclude specific characters.

🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request if you have ideas to make the algorithm even more secure.

Fork the Project

Create your Feature Branch (git checkout -b feature/NewFeature)

Commit your Changes (git commit -m 'Add some NewFeature')

Push to the Branch (git push origin feature/NewFeature)

Open a Pull Request
