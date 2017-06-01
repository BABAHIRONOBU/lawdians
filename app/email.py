from threading import Thread

import requests, json
import copy
from flask import current_app, render_template, flash

from config import config

data = {
    "senderAddress": "jae.woo@blackrubystudio.com",
    "title": "샘플 타이틀",
    "body": "샘플 내용",
    "receiverList": [
        {
            "receiveMailAddr": "zaiyou12@gmail.com",
            "receiveName": "고객1",
            "receiveType": "MRT0"
        }
    ]
}
URL = "https://api-mail.cloud.toast.com/email/v1.0/appKeys/"
PLUS_URL = "/sender/mail"


def send_async_email(msg_data):

    url = URL + app.config["MAIL_APP_KEY"] + PLUS_URL
    with app.app_context():
        res = requests.post(url=url, json=msg_data)
        flash(res.text)


def send_email(title_template, body_template, user_email, username, **kwargs):
    msg_data = copy.deepcopy(data)
    msg_data["title"] = render_template(title_template + '.txt', **kwargs)
    msg_data["body"] = render_template(body_template + '.txt', **kwargs)
    msg_data["receiverList"][0]["receiveMailAddr"] = user_email
    msg_data["receiverList"][0]["receiveName"] = username

    app = current_app._get_current_object()
    url = URL + app.config["MAIL_APP_KEY"] + PLUS_URL
    res = requests.post(url=url, json=msg_data)
