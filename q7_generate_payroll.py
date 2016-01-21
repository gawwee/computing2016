name = input("Enter your name: ")
hours = int(input("Enter hours worked weekly: "))
rate = float(input("Enter pay per hour: "))
cpf = float(input("Enter CPF rate(%): "))

grosspay = hours * rate
cpfcontri = grosspay * cpf / 100
netpay = grosspay - cpfcontri

print("Payroll statement for " + name)
print("Number of hours worked in a week: " + str(hours))
print("Hourly pay rate: ${0:.2f}".format(rate))
print("Gross pay = ${0:.2f}".format(grosspay))
print("CPF contribution at {0}% = ${1:.2f}".format(cpf, cpfcontri))
print("\nNet pay = ${0:.2f}".format(netpay))
      
             
            
