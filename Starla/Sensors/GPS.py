from sys import argv
import gps
import requests
import sys

sys.path.append("/home/pi/Starla")
from Sensors.Sensor import Sensor

class GPS(Sensor):
  def __init__(self):
    super().__init__()
    self.latitude = None
    self.longitude = None
    
    #Listen on port 2947 of gpsd
    self.session = gps.gps("localhost", "2947")
    self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

  def get_data(self):
    rep = self.session.next()
    try :
      if (rep["class"] == "TPV") :
        self.latitude = rep.lat
        self.longitude = rep.lon
      
    except Exception as e :
      print("Got exception " + str(e))
  
  def show_data(self):
    self.get_data()

    print("GPS")
    print("----------------")

    print("Latitude = ", self.latitude)
    print("Longiteude = ", self.longitude)
    print()
    
  def data_pack(self):
    self.get_data()
    return [self.latitude, self.longitude]