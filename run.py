from imagesearch import imagesearch
from datetime import datetime
import time
import requests
import sys

def main():
    pingUrl = "{endpoint}?user={user}&vm_acc_no={vmAccNo}".format(user=sys.argv[1], vmAccNo=sys.argv[2], endpoint=sys.argv[3])

    pos = imagesearch("/opt/imagesearch/img.png")
    if pos[0] != -1:
        ping(pingUrl, 0)
    else:
        dateNow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print('[', dateNow, ']', '\033[1;31m', 'STOPPED', '\033[0m')

def ping(pingUrl, retry):
    if (retry > 3):
        print("PING EXCEPTION!")
        return

    try:
        r = requests.get(pingUrl, timeout=3)
        print(getMsg(retry))
    except:
        time.sleep(1)
        ping(user, vmAccNo, endpoint, retry + 1)

def getMsg(retry):
    dateNow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    if (retry > 0):
        return '[', dateNow, ']', '\033[0;32m', 'PLAYING...', '\033[0m', '\033[94m', '(PING RETRY:', retry, ')','\033[0m'

    return '[', dateNow, ']', '\033[0;32m', 'PLAYING...', '\033[0m'

if __name__ == "__main__":
    main()
