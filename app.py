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
    r = '我看不懂你說什麼'

    if msg == '1' :
        r = '隨著時代的變遷，程式已經成為大家都會的東西，高一曾經接觸過程式，但當初因為更愛好生物，所以選擇醫藥衛生學群，但到高三我發現生物與我想像中有點落差，於是我開始學習程式想要進理工學群類的，此機器人正是我其中一個學習成果。'
    elif msg == '2':
        r = '過程可以算是相當坎坷，由於影片是2~3年前，因此在過程中偶爾會出現內容不符的現象，但遇到困難我選擇先上網查詢，藉由網路上的資訊解決問題，在製作的過程中，我也學到很多新知識，包括對於連接伺服器的概念...等等。'
    elif msg == '3':
        r = '在學習的過程，我能明顯感受到我的進步，而且我非常喜歡debug的環節，慢慢摸索到最後找到答案的過程使我有成就感，不單單是處理作業，我也喜歡自己打出些有趣的程式，盡管沒什麼實質作用，但卻能使我非常開心，我希望未來我依然能利用我所學的程式，來使我工作更加順利。'
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()