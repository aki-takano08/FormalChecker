# 正装度チェッカー
簡潔に紹介する予定

# DEMO

動画か、図解を乗せる予定🙈

# 必要なライブラリ
### pythonの標準ライブラリ
* glob
* sys
* datetime
* shutil
* os
### ライブラリ、フレームワーク
* keras.models
* numpy
* tensorflow
* keras.preprocessing.image
* flask
* PIL
* werkzeug.utils


# インストール方法と使い方
ローカルにtensorflowをインストールする。

```bash
# バージョンを指定してインストールする
$ pip install tensorflow==1.13.1
```
## クローンしてライブラリのインストールをする

```bash
# gitをローカルにクローンする
$ git clone https://github.com/aki-takano08/FormalChecker.git  
# クローンしたディレクトリに移動する
$ cd FormalChecker  
# pipを使って必要なライブラリをインストールする
$ pip install -r requirements.txt
```
### H5ファイルのをGoogleDriveからダウンロードする。
`1_x_entropy_acc.h5`をダウンロードして、ディレクトリ直下に追いて下さい。   
（100mb超えていたのでgithubにプッシュ出来ませんでした。）  
※urlは個別にお伝えします
###  実行する
```bash
$ python main.py
```
ipアドレスを教えてくれるので、そこにブラウザでアクセスすればOK!
# Note

注意点などがあれば書く

# Author

* 作成者
* 所属

# License
