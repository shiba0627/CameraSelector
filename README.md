# CameraSelector
webカメラのIDが毎回変わる問題への対処
## Setup & Run
Windows11, Python 3.11.9で動作確認をしています
```PowerShell
#PowerShell
# リポジトリのクローン
git clone https://github.com/shiba0627/CameraSelector.git
# カレントディレクトリはここ
cd CameraSelector
# 仮想環境作成
python -m venv venv_webcam
# 仮想環境アクティベート
.\venv_webcam\Scripts\activate 
# 必要なパッケージのインストール
python -m pip install -r requirements.txt 

# メインプログラムの実行
python main.py
```

## コマンドメモ
```PowerShell
#パッケージ一覧の出力
python -m pip freeze > requirements.txt 
# 一括ダウンロード
python -m pip install -r requirements.txt 
```