from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def home():
    return "WhatsApp Bot Running 🚀"

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():

    incoming_msg = request.values.get("Body", "").lower()

    response = MessagingResponse()
    msg = response.message()

    if incoming_msg == "hi":
        msg.body("Hello Vijju! 🚀")

    elif incoming_msg == "bye":
        msg.body("Goodbye 👋")

    elif incoming_msg == "thinnava":
        msg.body("haa! thinnaanu , nuvvu thinnaava !")
    elif incoming_msg == "ha thinnaanu !":
        msg.body("hmm ! inka enti mari sangathi")
    elif incoming_msg == "cheppaali":
        msg.body("maadhi emundhi antha normal ey !")
    elif incoming_msg == "haha":
        msg.body("haha ! Chaala happy unnaavu gah !")
    else:
        msg.body("I don't understand 😅")

    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)