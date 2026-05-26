# WhatsApp Chatbot using Flask + Twilio 🚀

A cloud-hosted WhatsApp chatbot built using Python Flask, Twilio WhatsApp Sandbox, and Render deployment.

This bot can automatically reply to user messages on WhatsApp with predefined responses.

---

# 📌 Features

- WhatsApp chatbot integration
- Automatic replies
- Flask backend
- Twilio Sandbox integration
- Cloud deployment using Render
- Custom Telugu/English responses
- Webhook handling

---

# 🛠️ Tech Stack

- Python
- Flask
- Twilio API
- WhatsApp Sandbox
- Render
- GitHub

---

# 📂 Project Structure

```bash
sms_project/
│
├── app.py
├── requirements.txt
├── render.yaml
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git

cd YOUR_REPOSITORY_NAME
```

---

## 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python app.py
```

Server runs on:

```bash
http://127.0.0.1:5000
```

---

# 🌐 Twilio WhatsApp Sandbox Setup

## Step 1

Create a Twilio account:

```text
https://www.twilio.com/
```

---

## Step 2

Go to:

```text
Messaging → Try it out → Send a WhatsApp message
```

---

## Step 3

Join Sandbox from your mobile:

Send:

```text
join reach-reader
```

to:

```text
+1 415 523 8886
```

---

## Step 4

Add your webhook URL in Sandbox settings:

```text
https://YOUR_RENDER_URL.onrender.com/
```

Method:

```text
POST
```

---

# ☁️ Deployment on Render

## Step 1

Push project to GitHub.

---

## Step 2

Create account on Render:

```text
https://render.com/
```

---

## Step 3

Create:

```text
New Web Service
```

---

## Step 4

Connect GitHub repository.

---

## Step 5

Render automatically deploys the Flask app.

---

# 💬 Example Bot Replies

| User Message | Bot Reply |
|---|---|
| hi | Hello Vijju! 🚀 |
| bye | Goodbye 👋 |
| thinnava | haa! thinnaanu , nuvvu thinnaava |
| cheppaali | maadhi emundhi antha normal ey ! |

---

# 📸 Project Demo

- Automatic replies
- Telugu conversation support
- Cloud hosted chatbot

---

# ⚠️ Important Notes

- This project uses Twilio WhatsApp Sandbox
- Users must join sandbox before using the bot
- Free Render hosting may sleep after inactivity
- First request after sleep may take time

---

# 🚀 Future Improvements

- OpenAI AI integration
- Database support
- User authentication
- Voice message support
- Multi-language support
- NLP chatbot

---

# 👨‍💻 Author

## Vijju

Computer Science Student | Data Analytics Aspirant

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub!
