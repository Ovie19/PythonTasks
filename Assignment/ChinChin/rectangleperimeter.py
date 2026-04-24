length = int(input("Enter the length of the triangle: "))
breadth = int(input("Enter the breadth of the triangle: "))

if length != breadth:
    perimeter = (length + breadth) * 2
    print("The perimeter of the rectangle is", perimeter)
else:
    print("The inputs are invalid");
