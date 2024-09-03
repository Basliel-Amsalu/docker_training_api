# email_service.py
from flask import Flask, request
from observer import Observer


class EmailService(Observer):
    def update(self, event_type: str, data: dict):
        print(f"EmailService: Sending email for event {event_type} with data {data}")
        return "", 204


app = Flask(__name__)
email_service = EmailService()


@app.route("/update", methods=["POST"])
def update():
    event_payload = request.json
    email_service.update("UserRegistration", event_payload)
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7001)
