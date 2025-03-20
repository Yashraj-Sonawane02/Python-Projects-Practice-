import win10toast
import time
import win32com.client


speaker = win32com.client.Dispatch("SAPI.SpVoice")

toast = win10toast.ToastNotifier()
while True:
    
    toast.show_toast("Notification" , "Yashraj..Time to drink water..", duration = 5 , icon_path = "waterSYM.ico" , threaded = True)
    speaker.speak("it's time to drink water.")
    time.sleep(10)
