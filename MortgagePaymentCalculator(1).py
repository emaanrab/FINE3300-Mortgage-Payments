#Mortgage Payments Calculator Code
def mortgage_payments(principal, rate, amortization):
    #First: Convert quoted annual interest rate to periodic interest rate
    annual_rate = rate / 100  # Convert percentage to decimal
    rate_semi_annual = (1 + annual_rate / 2)  # Semi-annual rate

    #Second: Number of months for amortization
    months = amortization * 12

    #Third: PVA formula
    def pva(rate, n):
        return (1 - (1 + rate) ** -n) / rate

#Calculate the periodic interest rate for each payment type
    #Monthly payment (r = (1 + annual_rate / 2)^(2/12) - 1)
    ratemonthly = (rate_semi_annual ** (2 / 12)) - 1
    monthly_payment = principal / pva(ratemonthly, months)

    #Semi-monthly payment (r = (1 + annual_rate / 2)^(2/24) - 1)
    ratesemimonthly = (rate_semi_annual ** (2 / 24)) - 1
    semi_monthly_payment = principal / pva(ratesemimonthly, months * 2)

    #Bi-weekly payment (r = (1 + annual_rate / 2)^(2/26) - 1)
    ratebiweekly = (rate_semi_annual ** (2 / 26)) - 1
    bi_weekly_payment = principal / pva(ratebiweekly, months * 26 / 12)

    #Weekly payment (r = (1 + annual_rate / 2)^(2/52) - 1)
    rateweekly = (rate_semi_annual ** (2 / 52)) - 1
    weekly_payment = principal / pva(rateweekly, months * 52 / 12)

    #Rapid Bi-weekly payment (half of the monthly payment)
    rapid_bi_weekly_payment = monthly_payment / 2

    #Rapid Weekly payment (one-quarter of the monthly payment)
    rapid_weekly_payment = monthly_payment / 4

#Return results (two decimal places)
    return (
        round(monthly_payment, 2),
        round(semi_monthly_payment, 2),
        round(bi_weekly_payment, 2),
        round(weekly_payment, 2),
        round(rapid_bi_weekly_payment, 2),
        round(rapid_weekly_payment, 2)
        )

def main():

    #HEADING: Welcome user to the calculator
    print("\nWelcome to your Mortgage Payment Calculator!")
    
    #Ask the user for input
    principal = float(input("\nEnter the principal amount: "))
    rate = float(input("Enter the quoted interest rate (as a percentage, e.g., 4.85 for 4.85%): "))
    amortization = int(input("Enter the amortization period in years: "))

    #Calculate the payments using the mortgage_payments function
    payments = mortgage_payments(principal, rate, amortization)

    #Results
    print(f"\nUsing the principal amount of ${principal:,}, quoted rate of {rate}%, and amortization of {amortization} years, your payment schedule is as follows:")
    
    print(f"\nMonthly Payment: ${payments[0]:.2f}")
    print(f"Semi-monthly Payment: ${payments[1]:.2f}")
    print(f"Bi-weekly Payment: ${payments[2]:.2f}")
    print(f"Weekly Payment: ${payments[3]:.2f}")
    print(f"Rapid Bi-weekly Payment: ${payments[4]:.2f}")
    print(f"Rapid Weekly Payment: ${payments[5]:.2f}")

#Run main function
if __name__ == "__main__":
    main()

