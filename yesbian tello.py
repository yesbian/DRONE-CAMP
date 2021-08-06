from easytello import tello
my_drone=tello.Tello()
my_drone.takeoff()
print(my_drone.get_battery())
for i in range(25):
    my_drone.forward(40)
    my_drone.cw(20)
my_drone.land()