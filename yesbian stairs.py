from easytello import tello
my_drone=tello.Tello()
my_drone.takeoff()
for i in range(5):
    Yesbian=int(my_drone.get_tof())
    my_drone.forward(35)
    if Yesbian>35:
        my_drone.down(20)  