from easytello import tello
my_drone=tello.Tello()
my_drone.takeoff()
print(my_drone.get_battery())
my_drone.curve(20,40,60,20,20,40,40)
my_drone.land()