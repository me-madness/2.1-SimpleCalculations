money = float(input())
income_value = input()
outcome_value = input()

if income_value == ' USD':
    usd = 1.79549
    if outcome_value == ' EUR':
        eur = 1.95583
        outcome = usd * money
        out_new = outcome / eur
        out_site = round(out_new, 2)
        print(str(out_site) + ' ' + outcome_value)  
    elif  outcome_value == ' GBP':
        gbp = 2.53405
        outcome = usd * money
        out_new = outcome / gbp
        out_site = round(out_new, 2)
        print(str(out_site) + ' ' + outcome_value)
    else :
        outcome = usd * money
        out_site = round(outcome, 2)
        print(str(out_site) + ' ' + outcome_value)
elif income_value == ' EUR':
    eur = 1.95583
    if outcome_value == ' BGN':
        outcome = money * eur
        out_site = round(outcome, 2)
        print(str(out_site) + ' ' + outcome_value)
    elif  outcome_value == ' GBP':
        gbp = 2.53405
        outcome = money * eur
        out_new = outcome / gbp
        out_site = round(out_new, 2)
        print(str(out_site) + ' ' + outcome_value)
    else :
        usd = 1.79549
        outcome = money * eur
        out_new = outcome / usd
        out_site = round(out_new, 2)
        print(str(out_site) + ' ' + outcome_value)     
elif income_value == ' GBP':
    gbp = 2.53405
    if outcome_value == ' BGN':
        outcome = gbp * money
        out_site = round(outcome, 2)
        print(str(out_site) + ' ' + outcome_value)
    elif  outcome_value == ' EUR':
        eur = 1.95583
        outcome = gbp * money
        out_new = outcome / eur
        out_site = round(out_new, 2)
        print(str(out_site) + ' ' + outcome_value)
    else :
        usd = 1.79549
        outcome = gbp * money
        out_new = outcome / usd
        out_site = round(out_new, 2)
        print(str(out_site) + ' ' + outcome_value)
else :           
    if outcome_value == ' USD':
        usd = 1.79549
        outcome = money / usd
        out_site = round(outcome, 2)
        print(str(out_site) + ' ' + outcome_value)
    elif  outcome_value == ' EUR':
        eur = 1.95583
        outcome = money / eur
        out_site = round(outcome, 2)
        print(str(out_site) + ' ' + outcome_value)
    else :
        gbp = 2.53405
        outcome = money / gbp
        out_site = round(outcome, 2)
        print(str(out_site) + ' ' + outcome_value)