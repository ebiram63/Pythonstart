import pyscreenshot as ImageGrab
import schedule
from datetime import datetime
import time



def take_screen():
    print("grab start......")
    t = str(datetime.now())[-7:]
    name = f"sc_{t}.png"
    sc = ImageGrab.grab()
    sc.save(name)
    print("grab end......")



schedule.every(2).seconds.do(take_screen)


while True:
    schedule.run_pending()
    time.sleep(1)
try:
    schedule.run_pending(1)
    time.sleep(1)
except:
    pass