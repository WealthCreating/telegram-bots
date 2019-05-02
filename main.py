from time import sleep
from telegram import chrome, tether

i = 0


if __name__ == '__main__':

    chrome = chrome.Chrome()
    while True:
        sleep(1)
        i += 1
        if i % 2400 == 0:
            chrome.refresh()

        if i % 120 == 0:
            tether.run(chrome)
