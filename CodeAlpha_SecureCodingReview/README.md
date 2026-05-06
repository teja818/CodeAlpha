# Secure Coding Review

## 📌 Project Overview

This project was developed as part of the CodeAlpha Cyber Security Internship.

The objective of this project is to perform a secure coding review on a Python-based login system by identifying security vulnerabilities and implementing secure coding practices to fix them.

The project demonstrates:
- SQL Injection vulnerability
- Login bypass attacks
- Secure parameterized queries
- Secure coding remediation techniques

---

## 🚀 Features

✅ Vulnerable login system demonstration  
✅ SQL Injection attack simulation  
✅ Secure login system implementation  
✅ Parameterized query protection  
✅ SQLite database integration  
✅ Secure coding analysis  
✅ Vulnerability remediation  

---

## 🛠️ Technologies Used

- Python 3
- SQLite3
- Bandit Security Scanner
- Visual Studio Code

---

## 📂 Project Structure

```bash
CodeAlpha_SecureCodingReview/
│
├── vulnerable_login.py
├── secure_login.py
├── users.db
├── README.md
└── screenshots/
```

---

## ⚠️ Vulnerable Login System

The vulnerable version uses unsafe SQL query construction:

```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```

This allows attackers to perform SQL Injection attacks.

---

## 🚨 SQL Injection Example

Example malicious input:

```sql
' OR '1'='1
```

This bypasses authentication in the vulnerable application.

---

## ✅ Secure Login System

The secure version uses parameterized queries:

```python
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
```

This prevents SQL Injection attacks.

---

## ▶️ Installation

### Install Required Packages

```bash
pip install bandit
pip install flask
```

---

## ▶️ How to Run

### Run Vulnerable Version

```bash
python vulnerable_login.py
```

### Run Secure Version

```bash
python secure_login.py
```

---

## 🔍 Security Analysis Using Bandit

Run Bandit scanner:

```bash
bandit vulnerable_login.py
```

Bandit helps identify insecure coding practices and vulnerabilities.

---

## 📌 Sample Output

### Vulnerable Login

```text
Login Successful!
```

### Secure Login

```text
Invalid Credentials!
```

---

## 📸 Project Screenshots

Add screenshots inside the screenshots folder and display them here.

Example:

```markdown
![SQL Injection Demo](screenshots/sql_injection.png)
![Secure Login](screenshots/secure_login.png)
```

---

## 📚 Concepts Learned

- Secure Coding Practices
- SQL Injection Attacks
- Parameterized Queries
- Authentication Security
- Vulnerability Assessment
- Security Remediation

---

## 🎯 Internship Task Objective

The objective of this task is to:
- Identify security vulnerabilities in code
- Analyze insecure coding practices
- Implement secure coding solutions
- Improve application security

---

## 👨‍💻 Author

**Ch. Tej Avinash Reddy**  
Cyber Security Intern — CodeAlpha

---

## 📜 Disclaimer

This project is created for educational and internship purposes only.

The vulnerable code should NOT be used in real-world applications.
