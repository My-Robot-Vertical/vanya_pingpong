'''
Info:
https://zen.yandex.ru/media/id/5c1a663bb6a0da00aac86ae4/python-vstroennye-funkcii-chr--ord--30-5ce56aec25bf1600b3965727
https://python-scripts.com/threading
'''

from time import sleep
from threading import Thread

class test(Thread):
    
    def __init__(self,com): 
        Thread.__init__(self)
    
    def run(self): # Запуск потока
        # выполняется один раз
        sleep(1)
        print("test")

if __name__ == "__main__":
    #main()
    potok = test('com6')
    potok.start()
    print("main")
