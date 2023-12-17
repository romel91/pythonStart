from math import pi

def radian_into_degree(radian):
  degrees = radian * (180 / pi)
  return degrees

angle_in_radians = float(input("Enter the angle in radians: "))
angle_in_degree = radian_into_degree(angle_in_radians)
print(f"{angle_in_radians} radians is equal to {angle_in_degree} degrees.")