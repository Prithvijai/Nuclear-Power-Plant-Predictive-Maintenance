from datetime import datetime

from pushbullet import Pushbullet
 
 

API_KEY = "o.dbb6zr91Dzv7vbZER528t573v5vialgO"
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", int(current_time[3:5]))
#pywhatkit.sendwhatmsg("+917010943514","Geeks For Geeks!",int(current_time[0:2]),2+int(current_time[3:5]))
pb = Pushbullet(API_KEY)
push = pb.push_note("Alert","Error in nuclear plant")

