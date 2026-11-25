class Architecture:
  def calculate_volume(self, l, w, h):
    vol = l* w*h
    return vol
  def calculate_perimeter(self, l, w, h):
    return 2*(l+w)
  def calculate_four_walls_area(self, l, w, h):
    return 2*h*(l+w)
  def calculate_floor_area(self,l,w):
      return l*w

#Creating Objects
bedroom =Architecture()
drawing_room = Architecture()
kitchen = Architecture()
washroom = Architecture()

l = int(input("Length:"))
w = int(input("Width"))
h = int(input("Height"))

#Bedroom Calculations
print("=====Bedroom====")
print("Volume:", bedroom.calculate_volume(l,w,h), "cubic meters")
print("Perimeter:", bedroom.calculate_perimeter(l,w,h),"meters")
print("Four walls Area:", bedroom.calculate_four_walls_area(l,w,h), "square meters")
print("Floor Area:", bedroom.calculate_floor_area(l,w), "square meters")

#Drawing Room Calculations
print("=====Drawing Room====")
print("Volume:", drawing_room.calculate_volume(5,4,3), "cubic meters")
print("Perimeter:", drawing_room.calculate_perimeter(5,4,3),"meters")
print("Four walls Area:", drawing_room.calculate_four_walls_area(5,4,3), "square meters")
print("Floor Area:", drawing_room.calculate_floor_area(5,4), "square meters")

#Kitchen Calculations
print("=====Kitchen====")
print("Volume:", kitchen.calculate_volume(5,4,3), "cubic meters")
print("Perimeter:", kitchen.calculate_perimeter(5,4,3),"meters")
print("Four walls Area:", kitchen.calculate_four_walls_area(5,4,3), "square meters")
print("Floor Area:", kitchen.calculate_floor_area(5,4), "square meters")

#Washroom Calculations
print("=====Washroom====")
print("Volume:", washroom.calculate_volume(5,4,3), "cubic meters")
print("Perimeter:", washroom.calculate_perimeter(5,4,3),"meters")
print("Four walls Area:", washroom.calculate_four_walls_area(5,4,3), "square meters")
print("Floor Area:", washroom.calculate_floor_area(5,4), "square meters")