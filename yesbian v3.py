from easytello import tello
my_drone=tello.Tello()
my_drone.takeoff()
print(my_drone.get_battery())
my_drone.up(20)
my_drone.cw(2)
my_drone.forward(225)
my_drone.up(125)
my_drone.forward(250)
my_drone.land()
my_drone.takeoff()
my_drone.up(40)
my_drone.down(30)