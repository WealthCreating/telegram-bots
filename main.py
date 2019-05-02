from time import sleep
from telegram import chrome, tether


def run(chrome, i):
    sleep(1)
    i += 1
    if i % 2400 == 0:
        chrome.refresh()

    if i % 120 == 0:
        tether.run(chrome)

    return run(chrome, i)


if __name__ == '__main__':
    chrome = chrome.Chrome()
    i = 0
    run(chrome, i)
