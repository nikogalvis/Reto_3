class Point:
   definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
   def __init__(self, x: float=0, y: float=0):
    self.x = x
    self.y = y
   
   def move(self, new_x: float, new_y: float):
    self.x = new_x
    self.y = new_y
   
   def reset(self):
    self.x = 0
    self.y = 0

   def __repr__(self):
      return f"Point({self.x}, {self.y})"
   
class Line:
   def __init__(self, start: "Point", end: "Point"):
      self.start = start
      self.end = end
      self.length = self.line_length()
      self.slope = self.line_slope()

   def vector_addition(self):
         return [self.end.x - self.start.x, self.end.y - self.start.y]
   
   def line_length(self):
      x = self.vector_addition()
      return ((x[0]**2) + (x[1]**2))**(0.5)
   
   def line_slope(self):
      if(self.end.x - self.start.x) == 0:
         return "La pendiente es infinita"
      return (self.end.y - self.start.y)/(self.end.x - self.start.x)
   
   def compute_horizontal_cross(self):
      return (self.start.y <= 0) and (self.end.y >= 0)
   
   def compute_vertical_cross(self):
      return (self.start.x <= 0) and (self.end.x >= 0)
   
   def __repr__(self):
      return f"Start {self.start}  End: {self.end}"

class Rectangle:
   def __init__(self, left_side: Line, top: Line):
      self.left_side = left_side
      self.top = top 
      

   def get_sides(self):
      f = self.left_side.start.x
      d = self.top.end.x
      g = self.left_side.start.y
      left = self.left_side
      up = self.top
      down = Line(start = self.left_side.start, end 
                  = Point(f+d, g))
      right = Line(start = Point(f+d, g),
                    end = self.top.end)
      return [f"Left side: {left}", f"Top: {up}", 
              f"Bottom: {down}", f"Right side:{right}"]
   
   def compute_area(self):
      return self.left_side.length*self.top.length
   
   def compute_perimeter(self):
      return 2*(self.top.length + self.left_side.length)
    
   def print_sides(self):
      for i in self.get_sides():
         print(i)

data_1 = Rectangle(left_side = Line(start = Point(0,0), 
                  end = Point(0,4)), top = Line(start = Point(0,4), end = Point(5,4)))

data_1.print_sides()
print(data_1.compute_area())
print(data_1.compute_perimeter())
