from fraction import CommonFraction

a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
fr1 = CommonFraction(a, b)

fr1 += CommonFraction(2, 5)
fr1 *= CommonFraction(5, 6)
fr1 += 2
#fr1 *= CommonFraction(5, 0)
print(fr1)
