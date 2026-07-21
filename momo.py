momo = float(input("enter the total bill amount:"))
print("total bill amount is:", momo)
discount = int( momo - (momo * 0.1))
print("total bill amount after 10% discount is:", discount)
sharing = int(input("enter the amount of people sharing the bill:"))
print ("amount to be paid by each person is:", discount/sharing)
plate= int(input("enter the number of plates: "))
momocount = plate * 10
print("the each person will get",momocount//sharing,"pieces of momo")
print("the left over momo will be",momocount%sharing,"pieces of momo")



