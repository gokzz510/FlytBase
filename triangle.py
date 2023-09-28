from flyt_python import api
import time
drone = api.navigation(timeout = 120000)
time.sleep(5.0)
drone.take_off(10.0) #take off at altitude 10m
print("in initial point")
drone.position_set(8.0, 6.0, 0, relative=True)
print("To top vertex A")
drone.position_set(-8.0, 6.0, 0, relative=True)
print("To bottom right vertex B")
drone.position_set(0, -10, 0, relative=True)
print("To the initial vertex C")
drone.land(async=False)
drone.disconnect()
