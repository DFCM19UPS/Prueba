from robot_model import Robot_model
from robot_controller import Controller_Robot
from robot_view import View

model=Robot_model()
view=View()
controller=Controller_Robot(model, view)
controller.run()
