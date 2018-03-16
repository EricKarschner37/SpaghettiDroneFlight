import libardrone
import xbox

joy = xbox.Joystick();  # Initialize joystick
drone = libardrone.ARDrone();

while(True):
    if joy.A():
        drone.takeoff();
    #     print("A button pressed!")
    if joy.B():
        drone.land();
    if joy.Y():
        drone.hover();

    drone.move(joy.leftX(), joy.leftY(), joy.rightTrigger() - joy.leftTrigger(), joy.rightX());

    # Legacy code: do not remove until the new method is tested and usable

    
    # if joy.leftX() < 0:
    #     drone.move_left();
    # if joy.leftX() > 0:
    #     drone.move_right();
    # if joy.leftY() < 0:
    #     drone.move_backward();
    # if joy.leftY() > 0:
    #     drone.move_forward();
    # if joy.rightX() < 0:
    #     drone.turn_left();
    # if joy.rightX() > 0:
    #     drone.turn_right();
    # if joy.rightY() < 0:
    #     drone.move_down();
    # if joy.rightY() > 0:
    #     drone.move_up();
    # if joy.Guide() and joy.Start():
    #     drone.reset();