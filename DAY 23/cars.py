from turtle import Turtle
import random

class Cars:
      def __init__(self):
         self.all_cars=[]
         self.car_speed=4


      def create_random_car(self):
          random_chance=random.randint(1,6)
          if random_chance==1:
              new_car=Turtle()
              new_car.penup()
              new_car.shape('square')
              new_car.shapesize(1, 2, 1)
              new_car.color('green')
              new_car.left(180)
              random_y=random.randint(-250,250)
              new_car.goto(320, random_y)
              self.all_cars.append(new_car)

      def move_cars(self):
          for car in self.all_cars:
              car.forward(self.car_speed)

      def level_up(self):
          self.car_speed+=1

