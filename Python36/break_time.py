import webbrowser
import time
i = 1
print("Program is started"+time.ctime())
while i <= 3:
    time.sleep(5)
    webbrowser.open("http://www.cricinfo.com")
    i = i+1

    
