from datetime import datetime, timedelta
from time import sleep
import chrome
from bots import btc_candle, tether


if __name__ == '__main__':

    chrome = chrome.Chrome()
    for i in range(1, 10**10):
        sleep(1)
        # Restart browser every hour
        if i % 3600 == 0:
            chrome.refresh()

        # Run tether bot every 2 min
        if i % 120 == 0:
            tether.run(chrome)

        # Run btc_candle bot at 23:59:00 UTC
        now = datetime.utcnow()
        if now.hour == 23 and now.minute > 58:
            btc_candle.run(now)
            sleep(60)
            btc_candle.run(now + timedelta(seconds=60))
