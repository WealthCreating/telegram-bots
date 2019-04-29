from time import sleep
import chrome
import os
import sys

i = 1
bots = [
    {
        'name': 'tether',
        'interval': 60
    }
]

def run():
    sleep(1)
    i += 1
    if i % 600 == 0:
        chrome.refresh()

    for bot in bots:
        if bot['interval'] % i == 0:
            bot['name'].run()



if __name__ == '__main__':
    chrome = chrome.Chrome()
    run()
