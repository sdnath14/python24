# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 
# Write your code below this row 👇
totalheight=0
for height in student_heights:
  totalheight+=height
print(f"total height={totalheight}") 

numberofstudent=0
for number in student_heights:
  numberofstudent+=1
print(f"total student={numberofstudent}") 

avgheight=round(totalheight/numberofstudent)
print(f"average height={avgheight}")
