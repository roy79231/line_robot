from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('AsOX917jb6jbQ1reNk8ULDpi96oQxSQ3jYhR/d0X/2BmP8GiIoBAXply+QSyZpG50fx160O7kMpwlk8O9/dCPLYfFMTESjgwAPrRI1revFHnRIRDEWWZ4ZznqwnoLDK85lF+ldSxB6FEUtW+hFqXfQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('85a710ba736235a975b7e8e33655772c')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s = '你吃飯了嗎?'
    r = '我看不懂你說什麼'

    if msg == 'hi' :
        r = 'hi'
    elif msg == '你吃飯了嗎':
        r = '還沒'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()