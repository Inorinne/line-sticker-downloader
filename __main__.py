import os, sys, time, requests, getopt
from colorama import init, Fore, Back, Style
try:
    opts, args = getopt.getopt(sys.argv[1:], 'hl:a', ['help','line=', 'anim'])
except Exception as e:
    print(str(e))
    sys.exit()
def line_downloader(ID):
    for x in ['stickerpack', 'stickers']:
        # 11221
        # animated 3080558
        url = "http://dl.stickershop.line.naver.jp/products/0/0/1/{:s}/iphone/{:s}@2x.zip".format(ID, x)
        # url = "http://ipv4.download.thinkbroadband.com/1GB.zip"
        r = requests.get(url, stream=True)
        PROG = 0
        if not r.ok: continue
        with open(os.path.basename(url), 'wb+') as f:
            try:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        PROG += len(str(chunk))
                        f.write(chunk)
                        sys.stdout.write('\r'+str(PROG))
                f.flush()
            finally:
                f.close()
for opt, arg in opts:
    if opt in ('-l', '--line'):
        line_downloader(arg)
        sys.exit()
    elif opt in ('-h', '--help'):
        init(convert=True)
        print('https://store.line.me/stickershop/product/{}/en'.format(Fore.GREEN+'3080558'+Fore.WHITE))
        print('-l [LINE ID] or --line=[LINE ID] to download the sticker.')
        print('{}E.g. line-sticker -l 3080558 or line-sticker --line=3080558'.format(Back.GREEN+Fore.WHITE))
        sys.exit()

input = input("Enter LINE ID: ")
if input: line_downloader(input)
else: os.system("py . -h")
