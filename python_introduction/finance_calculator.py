#compound interest calculator
MI = int(input("enter your monthly income: "))  #Monthly Income
ME = int(input("enter your total monthly expenses: ")) #Monthly Expense
Monthly_Savings = MI - ME 
projected_savings = Monthly_Savings * 12 +(Monthly_Savings * 12 * 0.05) #Assuming a 5% annual return on savings

print("Your monthly savings are ", Monthly_Savings)
print("Projected savings after one year, with interest, is:","$" ,projected_savings)
