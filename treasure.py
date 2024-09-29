line1 = [" ","️ ","️ "]
line2 = [" "," ","️ "]
line3 = [" "," "," "]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ")
#Options for A.
if position == "A1":
 line1[0] = "X"

if position == "A2":
 line2[0] = "X"

if position == "A3":
 line3[0] = "X"
#Options for B.
if position == "B1":
 map_B_1 = line1[1] = "X"

elif position == "B2":
 map_B_2 = line2[1] = "X"

elif position == "B3":
 map_B_3 = line3[1] = "X"
#Options for C.
if position == "C1":
 map_C_1 = line1[2] = "X"

elif position == "C2":
 map_C_2 = line2[2] = "X"

elif position == "C3":
 map_C_3 = line3[2] = "X"
print(f"{line1}\n{line2}\n{line3}")

