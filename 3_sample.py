class Car:
    pass

class Boat:
    pass

if __name__ == '__main__':

  q = int(input())
  queries = []
  for _ in range(q):
      args = input().split()
      vehicle_type, params = args[0], args[1:]
      if vehicle_type == "car":
          max_speed, speed_unit = int(params[0], params[1])
          print("car with the maximum speed of ",max_speed,speed_unit)

      elif vehicle_type == "boat":
          max_speed = int(params[0])
          print("Boat with the maximum speed of ",max_speed,'knots')

      else:
          raise ValueError("invalid vehicle type")