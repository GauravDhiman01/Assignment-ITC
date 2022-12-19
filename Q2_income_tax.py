Rate=20/100
Standard_Deduction=10000
Dependants=int(input("Enter the number of dependents : "))
Gross_Income=int(input("Enter the gross income : "))
Taxable_Income=Gross_Income-Standard_Deduction-(Dependants*3000)

Tax=Taxable_Income*Rate

print("The Taxable income is : %d \nThe tax is : %d " % (Taxable_Income,Tax))

print("\nThe tax rate is 20%")