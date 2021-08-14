from math import sqrt

def quadratic_formula(a,b,c):
    x = (-b + sqrt((b*b)-4*a*c))/(2 * a)
    y = (-b - sqrt((b*b)-4*a*c))/(2 * a)
    print('Your first value is: {} and your second value is: {}'.format(x,y))
print(quadratic_formula(int(input("input an a: ")), int(input("input an b: ")), int(input("input an c: "))))
input('Press ENTER to exit')