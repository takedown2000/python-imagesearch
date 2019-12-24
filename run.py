from imagesearch import imagesearch
from datetime import datetime
import time
import requests
import sys

def main():
    pingUrl = "{endpoint}?user={user}&vm_acc_no={vmAccNo}".format(user=sys.argv[1], vmAccNo=sys.argv[2], endpoint=sys.argv[3])

    while True:
        pos = imagesearch("/opt/imagesearch/img.png")
        dateNow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        if pos[0] != -1:
            try:
                r = requests.get(pingUrl)
                print('[', dateNow, ']', '\033[0;32m', 'PLAYING...', '\033[0m') #pos[0], pos[1]
            except:
                print('Ping EXCEPTION!')
        else:
            print('[', dateNow, ']', '\033[1;31m', 'STOPPED', '\033[0m')
        time.sleep(15)

if __name__ == "__main__":
    main()
