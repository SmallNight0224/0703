from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,ImageSendMessage
import random
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = Flask(__name__)

line_bot_api = LineBotApi('gThtNtgyKmz49kcApR6Gc/0sGvpbtPXlfJC85+p6bJ2ugBb4w0UDjj/HEpVUARLIcoLOyPHXY3VRrSwSgg6qKcgKIPZzxiAGe9o4sEoDCpNfRNlnTapgOPp3ww3Ps3K0fDOlFUddxfAaMcmm4a9lcQdB04t89/1O/w1cDnyilFU=')
line_handler = WebhookHandler('acde6b0819d2d8b86f8e932c394e7da9')

@app.route('/')
def home():
    return 'Hello World'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


def myG():
    myW=['你好','有下雨嗎','天氣如何']
    return random.choice(myW)



@line_handler.add(MessageEvent)
def handle_message(event):
    if (event.message.type == "image"):
        SendImage = line_bot_api.get_message_content(event.message.id)
        path = './static/'+event.message.id + '.jpg'
        with open(path, 'wb') as fd:
            for chenk in SendImage.iter_content():
                fd.write(chenk)
                   
        imageURL = path
        print('XXXXXXXXXXXXXXXXXXXXXX')        
        print(imageURL)

        img = Image.open(imageURL)
        ans=pytesseract.image_to_string(imageURL, lang="chi_tra+eng")
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=ans))     

@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    getA=event.message.text        

    if getA =='0' :        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(myG())))      
        
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="輸入0"))

if __name__ == "__main__":
    app.run()
