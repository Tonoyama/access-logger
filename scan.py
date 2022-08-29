import os
import pygame.mixer
from os.path import join, dirname
import time
import binascii
import nfc

sound_path = join(dirname(__file__), 'sound')

#入退室音源を再生
def sound(sound):
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(1)
    time.sleep(1)

#カード読み取り
def connected(tag):
    #読み取り可能なカードかを判定
    if isinstance(tag, nfc.tag.tt3.Type3Tag):
        #読み取り開始
        try:
            #カード情報読み取り
            service_code = 0x09CB
            sc = nfc.tag.tt3.ServiceCode(service_code >> 6 ,service_code & 0x3f)
            bc = nfc.tag.tt3.BlockCode(0,service=0)
            scandata = tag.read_without_encryption([sc],[bc])

            #書き込み用データ整形
            scanID = scandata[2:10].decode("utf-8")
            check = checkRecord(scanID)

            # 入室の場合、「おはようございます」

            # 退室の場合、「お疲れさまでした」


            #記録用ファイルに書き込み
            logRecord(scan_time,check,scanID)
            print(scan_time,check,scanID)

        #なにかエラーが起こった時
        except Exception as e:
            print("error: %s" % e)
    #読み取り可能なカードではないとき
    else:
        print("error: tag isn't Type3Tag")

    return True

check = 'in'
if check == 'in':
    hello_sound = sound_path + "/" + "ohayougozaimasu.mp3"
    sound(hello_sound)
elif check == 'out':
    bye_sound = sound_path + "/" + 'otukaresamadesita.mp3'
    sound(bye_sound)
else:
    error_sound = sound_path + "/" + 'error.mp3'
    sound(error_sound)

if __name__ == "__main__":
    #接続するデバイス情報
    clf = nfc.ContactlessFrontend('usb')
    while(True):
        clf.connect(rdwr={'on-connect': connected})