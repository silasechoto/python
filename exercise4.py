maths = int(input("maths:"))
english = int(input("english:"))
kiswahili = int(input("kiswahili:"))
chemistry = int(input("chemistry:"))
physics = int(input("physics:"))
total = maths + english + kiswahili + chemistry + physics
print(total)
average = total/5
print(average)
if average > 100:
    print("invalid")
elif average < 0:
    print("out of range")
elif average < 39:
    print("grade = E")
elif average < 50:
    print("grade = D")
elif average < 60:
    print("grade = C")
elif average < 70:
    print("grade =B")
elif average > 79:
    print("grade = A")
else:
    print("invalid input")
    print("grades")





# 0 to 39 = E
# 40 to 50 = D
# 51 to 60 = C
# 61 to 70 = B
# 70 to 100 = A





