import chrome
from time import sleep


i = 0

def run():
    sleep(1)
    i += 1
    if i % 600 == 0:
        chrome.refresh()

    if i % 60 == 0:
        tether.run(chrome)



if __name__ == '__main__':
    chrome = chrome.Chrome()
    run()
