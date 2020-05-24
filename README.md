# Name
 SkipAdYoutube

# Overview
 本プロジェクトはYoutubeの「広告をスキップ」を自動でクリックしてくれるツールです。  
 ブラウザでYoutubeを開き、動画再生中に広告が表示されれば代わりにクリックします。  
 家事をしながらゆっくり音楽を視聴したいのに、余計な広告が割り込みまくって面倒、  
 という時などに使えます。  

# Requirement
 ・python3、python3-venv  
   python2以前のバージョンでは動作確認していません。  
   setup.shもpython3、python3-venvは既にインストール済みという前提で組んでいます。  
   python3、python3-venvがない場合はユーザー様各自でパッケージ管理ソフトからインストールをして下さい。  
 ・python-selenium  
   後述するWebDriverをpythonから制御するためのパッケージです。   
   これはrequirements.txtを用いてpipでインストールさせています。  
　・Selenium WebDriverを本アプリに同梱しています。  
     Chrome用のドライバー:chromedriver(81.0.4044.138 linux 64bit)  
     Firfox用のドライバー:geckodriver(v0.26.0-linux 64bit)  

# Download
  ルートフォルダ "SkipAdYoutube" ごと好きな場所に格納して下さい。

# Setup
 コンソールでSkipAdYoutubeフォルダ直下をカレントディレクトリとし、以下を実行して下さい。
 
   bash setup.sh
 
 本シェルスクリプトは以下の処理を行います。  
 ・SkipAdYoutube 内部にpythonのvenvで仮想環境を作成します。その仮想環境上にseleniumパッケージをダウンロードします。  
 ・デスクトップにショートカットを自動で作成します。chromeが端末にインストールされていれば  
   chrome用のショートカットを、firefoxがインストールされていればfirefox用のショートカットを作成します。  
　＊SkipAdYoutubeの配置場所をショートカット作成後に移動した場合、パスがずれてしまいます。  
   ショートカットを再作成したい場合には、もう一度setup.shを実行してみて下さい。  

# Usage
 ・ショートカットを使用する場合  
   デスクトップ上のショートカットをクリックするだけです。  

 ・ショートカットを使わず直接起動する場合  
   コンソールでSkipAdYoutubeフォルダ直下をカレントディレクトリとし、以下を実行して下さい。  

     bash run.sh 引数１  

   "引数１"　とある箇所には chrome もしくは firefox と入力して下さい。  
   入力したブラウザが開きます。  
   ブラウザの起動後は、普段通りに使用して下さい。  
　　終了する場合も、ブラウザを閉じるだけで良いです。  

# Note
 前提：
- osはlinux(64bit)のみ対応しています。macやwindowsでは動作保証しません。  
- ChromeとFireFoxに対応しています。他ブラウザは未対応です。  
- 当ツールは人が手動で「広告をスキップ」をクリックする作業を自動化したものです。  
　　手動でクリックできないものまでスキップすることは不可能です。  
　　よって以下の状態でなければ正しく動作しません。  
　　　ブラウザの画面を表示していること。  
　　　ブラウザ以外の画面でブラウザが隠れていないこと。  
　　　マウスでクリックしてスキップできる広告であること。  
　　　　（カウントダウン中の間や、そもそもスキップさせるリンクが表示されない場合は不可能）  
- seleniumは本来ブラウザアプリのテスト自動化用のツールです。ブラウザによっては画面上に  
  「自動テストソフトウェアによって制御されています。」といったメッセージが表示されますが、  
  動作上は問題ありません。  
- 複数同時起動した場合には対応していません。  

# Structure

- `SkipAdYoutube/SkipAdYoutube.py` プログラム本体です。 (entry point)
- `SkipAdYoutube/chromedriver`     同梱されているドライバです。
- `SkipAdYoutube/geckodriver`      同梱されているドライバです。
- `SkipAdYoutube/requrements.txt`  pythonの依存ライブラリのリストです。依存ライブラリのインストール時に参照されます。
- `SkipAdYoutube/SkipAdYoutube_chrome.desktop`  chrome版のデスクトップファイルです。ショートカットの実行元となります。
- `SkipAdYoutube/SkipAdYoutube_firefox.desktop`  firefox版のデスクトップファイルです。ショートカットの実行元となります。
- `SkipAdYoutube/setup.sh`  依存ライブラリの自動インストール用のスクリプトです。
- `SkipAdYoutube/run.sh`    ショートカットからの起動時に実行されるファイルです。SkipAdYoutube.pyを実行します。

# Lisense
  SkipAdYoutube version 1.0.0  
  (c) 2020 OKKyu allrights reserved under MIT license.  

  ライセンスの対象  
  SkipAdYoutube.py  
  setup.sh  
  run.sh  
  requrements.txt  

  注意：chrome-driver及びgechodriverはOKKyuの著作物ではありません。  
     それぞれ以下のダウンロード元に著作権があります。  
　　　　<https://sites.google.com/a/chromium.org/chromedriver/downloads>  
　　　　<https://github.com/mozilla/geckodriver/releases>  

# Author
OKKyu
