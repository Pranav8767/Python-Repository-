# 1.  def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

# 2. 
def total_marks(m1,m2,m3):
    return m1+m2+m3

def percentage(total):
    return total/3

def grade(per):
    if per >=70:
        print("grade A")
    elif per >= 60:
        print("grade B")
    elif per >= 50:
        print("grade C")
    elif per >=40:
        print("grade D")
    else:
        print("fail")