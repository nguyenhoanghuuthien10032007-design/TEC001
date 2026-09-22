talent=float(input("Enter talent:"))
pound= float (input ("Enter pound:"))
lot= float(input("Enter lot;"))
T= talent*20*32*13
P= pound*32*13.3
L= lot*13.3
sum= T+P+L
kg= sum/1000
grs = (kg - int (kg)) *1000
print(f"Sum is: {sum}, KG is:{int(kg)}, Gram is: {grs: .2f}")