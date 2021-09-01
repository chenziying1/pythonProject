from flask import Flask



app = Flask(__name__)

print('模块在使用：',__name__)

from app import routes#py的循环引用