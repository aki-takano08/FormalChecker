# -*- coding: UTF-8 -*-
from keras.models import model_from_json
import numpy as np
import tensorflow as tf
from keras.preprocessing.image import img_to_array, load_img
from flask import redirect, url_for, render_template, flash, request, abort
from flask import Flask
import os
from PIL import Image
import shutil
from flask import send_from_directory
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
# 画像のダウンロード
import glob
import sys
from datetime import datetime
app = Flask(__name__)
img_url =""
app.secret_key = b'_5y276"F4Q8z\n\xec]/'
label=['men_casual','men_suit']
SAVE_DIR = "./images"
if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

app.config['UPLOAD_FOLDER'] = SAVE_DIR


@app.route('/images/<path:path>')
def send_js(path):
    return send_from_directory(SAVE_DIR, path)

#　切り替え用
file_name='1_x_entropy_acc'

#load model and weights
json_string=open(file_name+'.json').read()
model=model_from_json(json_string)
model.load_weights(file_name+'.h5')
model._make_predict_function()
graph = tf.get_default_graph()


def model_run(data):
    temp_img=load_img(data,target_size=(224,224))
    temp_img_array=img_to_array(temp_img)
    temp_img_array=temp_img_array.astype('float32')/255.0
    temp_img_array=temp_img_array.reshape((1,224,224,3))
    #predict image
    global graph
    with graph.as_default():
        img_pred=model.predict(temp_img_array)
        np.set_printoptions(formatter={'float': '{:.2f}'.format})
        predict_percent = round(np.max(img_pred)*100,3)
        title = (label[np.argmax(img_pred)])
    return title,predict_percent



def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


########################################################


# アップロードされる拡張子の制限
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'PNG', 'JPG', 'JPEG'])
img1 =[]
img_url=""
title=""
predict_percent=0

# ファイルを受け取る方法の指定
@app.route('/', methods=['GET','POST'])
def index():
    
    if title =="":
        return render_template("index.html")
    else:
        return render_template("index.html",img_url=img_url, data=title, percentage=predict_percent)

@app.route('/upload', methods=['GET','POST'])
def upload():
    shutil.rmtree(SAVE_DIR)
    os.mkdir(SAVE_DIR)
    
    # # ファイルがなかった場合の処理
    if 'image' not in request.files:
        flash('ファイルがありません','failed')
        return redirect(request.url)
    img1 = request.files['image']
                # ファイルのチェック
    if img1 and allowed_file(img1.filename):
        img1_secure = secure_filename(img1.filename)
    else:
        flash('画像ファイルを入れてください','failed')
        return render_template("index.html")
        # sys.exit(1)
    
    Img =  Image.open(img1)
    dt_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
    save_path = os.path.join(SAVE_DIR, dt_now + "." + img1_secure)
    Img.save(save_path)

    img2 = glob.glob(save_path)
    img_url = img2[0]
    title,predict_percent = model_run(img1)
    #####################################
    
        
    return render_template('index.html',img_url=img_url, data=title, percentage=predict_percent)

if __name__ == '__main__':
    app.debug = True
    app.run()
    # import ssl
    # app.run(host='0.0.0.0', port=5955, ssl_context=('server.crt', 'server.key'), threaded=True, debug=True)
