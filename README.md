# 入退室管理システムのサンプル

- [入退室管理システムのサンプル](#入退室管理システムのサンプル)
- [システム概要図](#システム概要図)
- [仕様](#仕様)
  - [正常系の仕様](#正常系の仕様)
  - [異常系の仕様](#異常系の仕様)
- [詳細な環境構築手順](#詳細な環境構築手順)
  - [Raspberry Piとは](#raspberry-piとは)
    - [何ができるのか](#何ができるのか)
  - [組み立て](#組み立て)
    - [絶対必要なもの](#絶対必要なもの)
    - [OSをインストール](#osをインストール)
    - [本体の組み立て](#本体の組み立て)
  - [ソフトウェアのセットアップ](#ソフトウェアのセットアップ)
    - [CUI(キーボード操作のみ)でアクセスする](#cuiキーボード操作のみでアクセスする)
    - [接続方法](#接続方法)
  - [GUI(マウス操作)でRaspberry Piにアクセス](#guiマウス操作でraspberry-piにアクセス)
    - [【マジで重要】次回も VNC で接続するための設定](#マジで重要次回も-vnc-で接続するための設定)
    - [MC2wifi に接続](#mc2wifi-に接続)
    - [日本語を入力できるようにする](#日本語を入力できるようにする)
    - [gitのインストール](#gitのインストール)
    - [seleniumのインストール](#seleniumのインストール)
    - [cronのセットアップ](#cronのセットアップ)
    - [WiFiの自動接続の設定](#wifiの自動接続の設定)
    - [正確な時刻にする](#正確な時刻にする)
    - [自動起動設定](#自動起動設定)

# システム概要図



# 仕様

## 正常系の仕様

- [ ] 入室時に「おはようございます」退室時に「お疲れ様でした」と音声が再生される

- [ ] 音声が再生された後にカードリーダに学生証をタッチすると動作する

- [ ] 1日に複数回入退室を繰り返しても正常に動作する

- [ ] 退室を忘れた場合は、その日の23:50に退室したことにする

- [ ] 年明け直後1/1 0:00に新しいフォルダが生成される(フォルダ名の例：2022)

- [ ] 1ヶ月毎の0:10に新しいスプレッドシートが生成される(ファイル名の例：2022-08)

- [ ] 1つのスプレッドシートに1ヶ月分のシートが毎日0:20に追加される(8/22のシート名の例：22)

- [ ] リアルタイムで入室・退室をSlackに学生番号とともに投稿できる

- [ ] リアルタイムで入室・退室をスプレッドシートに時刻、学生番号を送信できる

- [ ] 教職員のカードでも正常に動作する

## 異常系の仕様

- [ ] 異常が起こるとエラー音を出力する

- [ ] 学生証以外のカードをタッチするとエラー音を出力する

- [ ] 定期的にネットワークは繋がっているか確認を行い、繋がっていない場合、自動的に接続する

- [ ] 突如、電源が落ちて再起動してもアプリのプロセスを自動起動する

- [ ] 想定外のバグでも停止を回避するため、毎日午前3時にRaspberry Piは再起動される

- [ ] Raspberry Pi内の時間で入退室時間を記録し、スプレッドシートに記入される


# 詳細な環境構築手順

もし不具合があれば殿山(gp20a087@oecu.jp)までご連絡ください。

## Raspberry Piとは

Raspberry Pi(ラズベリーパイ)とは、シングルボードコンピュータと呼ばれる**小型のコンピュータ**のこと。1台が5千円から1万円程度で安価なため、趣味や業務の試作品の開発でよく使われる。日本では、通称「**ラズパイ**」と呼ばれる。

### 何ができるのか

カードリーダと接続することで学生証を読み取り、入退室管理システムを作れる。

【過去の事例】
[情報通信工学部主催の『研究室入退室管理システム』ハッカソンが開催されました](https://www.osakac.ac.jp/news/2021/2259)


Bluetoothの電波をカウントすることで食堂の混雑度を計測することができる。

【過去の事例】
[情報工学科1・2年生の学生有志が学内食堂の混雑緩和を目的としたアプリを開発しました](https://www.osakac.ac.jp/news/2021/2395)

その他、カメラや二酸化炭素、温度センサーなど様々なモジュールを使うことができる。

## 組み立て

### 絶対必要なもの

- Raspberry Pi本体
- Raspberry Piのケース
- マイクロSDカード
- PC(Windows, Mac, Linuxのどれでも良い)
- LANケーブル
- **マイクロSDカードのアダプター**

※　**マイクロSDカードのアダプター**は付属してない場合が多い。持っていない場合は、先生や先輩に借りられるかを確認するか、Amazonで購入する。

![](https://i.imgur.com/edGErjc.jpg)

### OSをインストール

マイクロSDカードをパッケージから取り出して、アダプタに差し込む。
Windows PCでは、警告が出る場合もあるが「何もしない」を選択する。

[Raspberry Pi OSの公式サイト](https://www.raspberrypi.com/software/)にてインストーラーである「Raspberry Pi Imager」をダウンロードしインストールする。

![](https://i.imgur.com/MseLRcL.png)

Windowsの場合、「Download for Windows」を選択し、インストールする。

Mac OSの場合、「Download for macOS」を選択し、インストールする。

ＯSはRaspberry Pi OS(32-bit)を選択。

![](https://i.imgur.com/PjKd5Zl.png)

「CHOOSE STRAGE」に差し込んだSDカードを選択。

SDカードの名前がわからない場合、一回SDカードを抜き、消えたものがSDカードとなる。

![](https://i.imgur.com/AA2EnJK.png)


WRITEをクリック。
「SDカードの中身消しちゃうけどいい？」という意味の警告が出るが「Yes」を選択。

パスワードを求められるので自身のPCのパスワードを入力する。

![](https://i.imgur.com/wSZaEJE.png)

OSのインストールが完了したら「CONTINUE」を押す。
これでSDカードにRaspberry Pi OSをインストールすることに成功した。

![](https://i.imgur.com/7bpQWTj.png)

### 本体の組み立て

新品の場合、茶色い箱の中に「ドライバー」「保護ケース」「ヒートシンク」「CPUファン」「保護ケースのすべり止め」「組み立て手順書」「電源アダプタ」がある。

![](https://i.imgur.com/HhcL3oN.jpg)

赤い箱の中にRaspberry Piの基盤が入っている。
壊さないように注意して取り扱う。

![](https://i.imgur.com/QnMmJG3.jpg)


茶色い箱の中にある手順書どうりに組み立てる。

![](https://i.imgur.com/W7RuxNb.jpg)


CPUファンは静音モードとなるようにアタッチメントをピンに刺す。
<font color="red"><u>**プラス極とマイナス極が正しく挿入しているかしっかり確認する。**</u></font>

![](https://i.imgur.com/9hH8v83.jpg)

OSをインストールしたマイクロSDカードを画像の所に差し込む。

この時、力任せに差し込まない。

![](https://i.imgur.com/pZ5jXFZ.jpg)


Raspbery Piの裏側からみるとこのようになっている。

![](https://i.imgur.com/4RLka3o.jpg)


組み立てたらこのようになる。
保護ケースを閉めてRaspberry Piの組み立ては完了。

![](https://i.imgur.com/8Akr1QX.jpg)

## ソフトウェアのセットアップ



### CUI(キーボード操作のみ)でアクセスする

sshでラズパイにアクセスする。ssh(エスエスエイチ)とは、Secure Shellの略で、ネットワークに接続された機器を遠隔操作するための通信方法。

下記URLから「Tera Term」をインストールする。
※「ポータブル版」ではない。
https://forest.watch.impress.co.jp/library/software/utf8teraterm/

### 接続方法

<font color="red">**【重要】まず、Raspberry PiとPCをLANケーブルで接続しておく。**</font>

<font color="red">**Windowsの場合、Raspberry Pi OSを入れたマイクロSDの「bootフォルダ」内に「ssh.txt」を作っておく**</font>

![](https://i.imgur.com/DMa9cGo.png)

ホスト名：`raspberrypi.local`

デフォルトの設定なら下記を設定する。

ユーザー名：`pi`
パスフレーズ：`raspberry`


![](https://i.imgur.com/EvVfbBD.png)

成功画面例：
![](https://i.imgur.com/qcaGnfb.png)


## GUI(マウス操作)でRaspberry Piにアクセス

VNCを使用可能にする。
VNC(Virtual Network Computing)とは、ネットワークを通じて別のコンピュータに接続し、そのデスクトップ画面を呼び出して操作することができるリモートデスクトップソフトのこと。


[公式サイト](https://www.realvnc.com/en/connect/download/viewer/) からWindows版の「VNC Viewer」をインストールする。


「Tera Term」で下記のコマンドを実行

`sudo`(スードゥー)とは、管理者(rootユーザー, スーパーユーザー)として実行するためのコマンドのこと。一般ユーザーでは実行できないコマンドを実行できるようになる。

```shell=
sudo nano /boot/config.txt
```

「`#`」を消し、保存する。

![](https://i.imgur.com/BsD4m5u.png)


↓`nano`の操作
https://www.fabshop.jp/nano-beginners/

```shell=
#hdmi_force_hotplug=1
```

```shell=
sudo raspi-config
```

![](https://i.imgur.com/SCN61ie.png)

I3のInterface Optionsを選択

![](https://i.imgur.com/DdjM1Bw.png)

左矢印キーで「Yes」を選択する

![](https://i.imgur.com/YSMETDT.png)

Advanced Options で Resolution から 1920x1080 に設定する。

右矢印キーで「Finish」を選択する。

再起動する。

```shell=
sudo reboot
```

VNC Viewerを開き`raspberrypi.local`を入力する

![](https://i.imgur.com/9Zi0Nej.png)

:warning:注意
<font color="red">**大学で接続する場合は、MC2wifiのプロキシに阻まれるため、MC2wifiの接続を切っておく。**</font>

`eduroam`なら阻まれることはない。

![](https://i.imgur.com/QOKeZvW.png)

「Continue」を選択する。

![](https://i.imgur.com/851XMRD.png)

下記の画像の通りのUsernameとPasswordを入力する。
Remember passwordにチェックを入れておくと次回からpasswordを入力しなくて良いのでオススメ。

![](https://i.imgur.com/ONpy3w5.png)

成功画面例：
「OK」を選択する。

![](https://i.imgur.com/OiosXDU.jpg)

「Next」を選択する。

![](https://i.imgur.com/g7or0Ba.jpg)

「Country」は<font color="red">Japan</font>を選択。

![](https://i.imgur.com/B9sWSjG.jpg)


「Password」を入力し「Next」を押す。
<font color="red">**:warning:Passwordは絶対に忘れない事。**</font>

![](https://i.imgur.com/RZ8pYYz.jpg)

画面の比率があっていない場合、「This screen shows a black border around the desktop」、または、「Ther taskbar does not fit onto the screen」にチェックを入れる。

![](https://i.imgur.com/n5P0hE8.jpg)

<font color="blue">**アップデートは後から行うので「Skip」を選択する。**</font>

:::info
💡アップデートは後でも出来る!
:::

以下の画面まで進み「Restart」を選択する。

![](https://i.imgur.com/Rs42Udw.jpg)


### 【マジで重要】次回も VNC で接続するための設定

Raspberry Piでウィンドウ右上にあるメニューボタン（横棒が縦に3つ並んだマーク）から [Option] を開き、 [Security] タブの [Authentication] をUnix passwordからVNC passwordに変更。

[OK] をクリックするとパスワードの設定を求められるので入力。

設定したパスワードでもう一度接続を試みると、無事接続できるようになっている。

### MC2wifi に接続

WiFi は、`MC2wifi`を選択し、

```
OECUwireless
```

と入力する。

ブラウザを開き、[http://www.mc2.osakac.ac.jp](http://www.mc2.osakac.ac.jp/)を検索しWifiに接続する。

![](https://i.imgur.com/sitVcuV.png)


### 日本語を入力できるようにする

ターミナルを開き以下のコマンドを1行ずつ入力する。

最新の状態にアップデートする。

```shell=
sudo apt update　-y
sudo apt upgrade　-y
```

ibus-mozcは、日本語インプットメソッドエディタ (IME)のこと。このモジュールで日本語入力ができるようになる。

```shell=
sudo apt install ibus-mozc -y
```

再起動

```
sudo reboot
```

初めは、入力モードが直接入力になっているので、「ひらがな」に変更する。


![](https://i.imgur.com/IyKghOm.png)

参考 URL：
https://www.indoorcorgielec.com/resources/raspberry-pi/raspberry-pi-input-japanese/

### gitのインストール

Git(ギット)は、ソースコードを管理するソフト。

```shell=
sudo apt install git -y
sudo apt install python3-pip libglib2.0-dev chromium-chromedriver postfix
```

右矢印キーで「了解」を選択する。

以下の画面で「インターネットサイト」を選択する。

![](https://i.imgur.com/yxI3zuw.png)

そのままEnterを押す。

![](https://i.imgur.com/71EYCPn.png)



### seleniumのインストール

Selenium(セレニウム)は、Webブラウザの操作を自動化するためのフレームワーク。

pip3は、Pythonのパッケージ管理ツール。

```shell=
sudo pip3 install selenium
```

### cronのセットアップ

cron(クーロン, クロン)とは、特定のコマンドやスクリプトを定時実行するために使われるコマンドのこと。

:warning:**cronの注意点。**
<font color="red">**絶対パスを使う。相対パスは絶対使わない**</font>

**絶対パス**とは、フルパスとも呼ばれており、ルートディレクトリと呼ばれる階層構造の頂点から目的地までの経路を表している。ユーザが現在どのフォルダで作業中であっても、常に同じスタート地点から、常に同じ経路の表示になる。

**相対パス**とは、ユーザが現在作業しているフォルダから目的のフォルダまでの経路。

今現在の場所を確認したい時のコマンド
```shell=
pwd
```

cronを起動する。

<font color="green">active(running)</font>となっているかを確認する。

```shell=
sudo /etc/init.d/cron start
sudo /etc/init.d/cron status
```

エディターは、`/bin/nano`で数字で選択する。


**nanoでは、Ctrl+Oで保存。Ctrl+Xで終了する。**

Ctrl+Xでエディターを終了しておく。

```shell=
crontab -e
```

ホームディレクトリに移動する。

```shell=
cd
```

`/home/pi`になっていることを確認。

```shell=
pwd
```

`Ctrl+O`で保存。`Ctrl+X`で退出。

```shell=
nano hello.py
```

```python=
print("Hello!")
```

cronでは、「`* * * * *`」の5箇所を指定して、様々なタイミングの起動時間を設定する。左から「分」「時」「日」「月」「曜日」を指定する。

```
# cronの起動時間設定
* * * * * （起動したい処理）
| | | | |
| | | | |- 曜日
| | | |--- 月
| | |----- 日
| |------- 時
|--------- 分
```

1分毎に実行。念の為、事前にスクリプトを実行できるかを確認しておくこと。

`Ctrl+O`で保存。`Ctrl+X`で退出。

```shell=
*/1 * * * * sudo /usr/bin/python3 /home/pi/hello.py
```

書き込まれているかを確認

```shell=
crontab -l
```
```shell=
sudo nano /etc/rsyslog.conf
```

コメント(`#`)を削除。先頭に空白が残らないように注意する。

```shell=
cron.*                          /var/log/cron.log
```

`Ctrl+O`で保存。`Ctrl+X`で退出。

```shell=
sudo /etc/init.d/rsyslog restart
sudo nano /etc/default/cron
```

コメント(`#`)を削除し、下記のように編集。先頭に空白が残らないように注意する。

```shell=
EXTRA_OPTS='-L 15'
```

cronを再起動する。

```shell=
sudo /etc/init.d/cron restart
```

実行されているかを確認。Ctrl+Cで終了。

```shell=
tail -f /var/log/cron.log
```


### WiFiの自動接続の設定

プロジェクトなどで長く放置する場合、さまざまなことが原因で接続が切れてしまう。ここでは、電源が引き抜かれても再度コンセントに差すだけで MC2wifi に繋がる設定を行う。

まず、既存の wpa_supplicant を停止する。

```shell=
sudo killall wpa_supplicant
```

```shell=
sudo dhcpcd wlan0 down
sudo dhcpcd wlan0 up
sudo reboot
```

（Wifiの設定ファイルを編集する）
identityに「**学籍番号**」を入力する。
passwordは入力者本人の「**パスワード**」を入力する。
```shell=
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=JP

network={
	ssid="MC2wifi1x"
	psk="OECUwireless"
	proto=RSN
	key_mgmt=WPA-EAP
	pairwise=CCMP
	auth_alg=OPEN
	eap=PEAP
	identity="学籍番号"
	password="パスワード"
	phase1="peaplabel=0"
	phase2="auth=MSCHAPV2"
	disabled=1
}

network={
	ssid="MC2wifi"
	psk="OECUwireless"
	key_mgmt=WPA-PSK
}
```
（Wifiのモジュールが自動で接続できるようにする。）
```shell=
sudo nano /etc/network/interfaces
```

```
# interfaces(5) file used by ifup(8) and ifdown(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d

auto wlan0
allow-hotplug wlan0
iface wlan0 inet manual
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```

無線 LAN を ON にする。`sudo ifup wlan0`は古いコマンドなので使えない

```shell=
sudo reboot
sudo ifconfig wlan0 down
sudo ifconfig wlan0 up
```

ホームディレクトリに戻る

```
cd
```

OSのアップデート

```
sudo apt update && sudo apt upgrade -y
```

必要なパッケージをインストール

```
sudo apt install git python3-pip libglib2.0-dev chromium-chromedriver postfix
```

```
git clone 
```

Raspberry Pi OSは、実は、sudoが必要なので注意。

```
sudo pip3 install -r ./access-loger/requirements.txt
```

access-loggerフォルダ直下に.envファイルを作成する

```
sudo nano ./access-loger/.env
```

### 正確な時刻にする

NTP（Network Time Protocol）は、ネットワークを介して時刻同期を行うプロトコル。

Raspberry Pi は、RTC(リアルタイムクロック)を持っていない。

リアルタイムクロックは、コンピュータなどが内蔵する時計や、その機能が実装されている集積回路(IC)のこと。システムの電源が切られていてもバッテリバックアップなどにより「時刻」を刻み続けることできる。しかし、Raspberry Pi は、OSがタイマーにより「時間」を測定しするので、シャットダウンすると時刻情報が失われる。

NTPデーモンの設定ファイル`timesyncd.conf`を設定する。

```
sudo nano /etc/systemd/timesyncd.conf
```

一番最後に追記する。

```
NTP=ntp.jst.mfeed.ad.jp ntp.nict.jp
FallbackNTP=time.google.com
```

NTPを有効化。

```
sudo timedatectl set-ntp true
```

```
sudo systemctl daemon-reload
sudo systemctl restart systemd-timesyncd.service
```

```
sudo systemctl status systemd-timesyncd
```

緑色で`active(running)`になっているかを確認。


### 自動起動設定

```
mkdir .config/autostart
```

```
sudo nano .config/autostart/raspi_scan.desktop
```

raspi_scan.desktop内にターミナルを自動起動する設定を書く。

```
[Desktop Entry]
Exec=lxterminal
Type=Application
Name=Rasp_Scan
Terminal=true
```

ターミナルの設定を追記

```
sudo nano ~/.bashrc
```

```
cd /home/pi/access-logger
sudo /usr/bin/python3 main.py
```

設定の反映が成功すれば、「Access Logger」が起動する

```
source ~/.bashrc
```

再起動すると、「Access Logger」が自動起動する。 MC2wifiも自動でつながる。以上。
