from easytello import tello
import getch
my_drone=tello.Tello()
isonground=True
print(my_drone.get_battery())
my_drone.set_speed(60)
while True:
    Keybind=getch.getch()
    if Keybind=="w":
        my_drone.forward(60)
    elif Keybind=="a":
        my_drone.ccw(20)
    elif Keybind=="s":
        my_drone.back(40)
    elif Keybind=="d":
        my_drone.cw(20)
    elif Keybind==" ":
        if isonground==True:
            my_drone.takeoff()
            isonground=False
        else:
            my_drone.land()
            isonground=True
    elif Keybind=="3":
        my_drone.flip("f")
    elif Keybind=="4":
        my_drone.flip("b")
    elif Keybind=="5":
        my_drone.flip("r")
    elif Keybind=="6":
        my_drone.flip("l")
    elif Keybind=="u":
        my_drone.up(20)
    elif Keybind=="j":
        my_drone.down(20)
    elif Keybind=="m":
        my_drone.emergency()
    elif Keybind=="o":
        my_drone.left(20)
    elif Keybind=="p":
        my_drone.right(20)