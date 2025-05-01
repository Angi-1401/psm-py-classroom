print("Side A:")
side_a = float(input())

print("Side B:")
side_b = float(input())

print("Side C:")
side_c = float(input())

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    print("Valid triangle")

    if side_a == side_b and side_b == side_c:
        print("Equilateral triangle")
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Invalid triangle")
