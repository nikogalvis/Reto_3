#Sesion de Practica
class Complex():
  def __init__(self, real: float, imaginary: float):
    self.real = real
    self.imaginary = imaginary

  def __add__(self, no: "Complex") -> "Complex":
    result_real = self.real + no.real
    result_imaginary = self.imaginary + no.imaginary
    return Complex(result_real, result_imaginary)
  
  def __sub__(self, no: "Complex") -> "Complex":
    result_real = self.real - no.real
    result_imaginary = self.imaginary - no.imaginary
    return Complex(result_real, result_imaginary)
  
  def __mult__(self, no: "Complex") -> "Complex":
    result_real = self.real*no.real - self.imaginary*no.imaginary
    result_imaginary = self.real*no.imaginary + self.imaginary*no.real
    return Complex(result_real, result_imaginary)

  def __truediv__(self, no: "Complex") -> "Complex":
    denominator = no.real**2 + no.imaginary**2
    result_real = (self.real*no.real + self.imaginary*no.imaginary)/(denominator)
    result_imaginary = (self.real*no.real - self.real*no.imaginary)/(denominator)
    return Complex(result_real, result_imaginary)
  
  def __mod__(self) -> "Complex":
    return Complex((self.real**2 + self.imaginary**2)**0.5, 0)


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(x + y)
    print(x - y)
    print(x*y)
    print(x/y)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
