# FINE3300-Mortgage-Payments-
FINE 3300 Assignment #1. Project objective is to create a calculator that calculates mortgage payments.

"""
FINE3300 Mortgage Payments

Project Overview: This program will calculate mortgage payments based on user inputs such as: Principal amount, Quoted interest rate, and Amortization period (in years)

Mortgage Rate Types in Canada:
In Canada, home mortgages can have either a fixed or variable interest rate.

- Fixed Rate Mortgage: 
  - The interest rate stays the same throughout the term of the mortgage, meaning your monthly payments will remain constant.
  - A new rate is renegotiated upon maturity, unless the outstanding principal balance is paid off in full.
  
- Variable Rate Mortgage: 
  - The interest rate can fluctuate during the term of the mortgage.
  - Some lenders adjust your payments based on the new rate, while others maintain the same payment and extend the amortization period to pay off the loan.

This assignment will focus on fixed-rate mortgages, where rates are quoted as semiannually compounded rates. 

The program calculates using the following payment schedules:
- Monthly Payments
- Semi-monthly Payments
- Bi-weekly Payments
- Weekly Payments
- Accelerated Bi-weekly Payments
- Accelerated Weekly Payments

Project Features: 
- User can input mortgage principle, interest rate, and amortization period. 
- Uses industry-standard formulas for Canadian fixed-rate mortgages.
- Displays payment amounts, rounded to the nearest penny.

How It Works:
1. The user is asked to input:
   - Principal Amount (e.g., $100,000)
   - Quoted Interest Rate (e.g., 5.5%)
   - Amortization Period in years (e.g., 25 years)

2. The program calculates the periodic interest rate for each schedule.
   Where 'n' depends on the payment frequency (e.g., 12 for monthly, 24 for semi-monthly).

3. Payment amounts are calculated using the Present Value of Annuity (PVA) formula:
   PVA(rate, n) = (1 - (1 + rate)^(-n)) / rate

Resources Used:
- Programming Language: Python
- Tools: Visual Studio Code, Git, GitHub
"""
