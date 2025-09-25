renda = float(input('insira o valor da sua renda'))
cal_renda4000 = (renda-4500)
cal_renda3000 = (renda-3000)-cal_renda4000
cal_renda2000 = (renda-2000)-cal_renda3000-cal_renda4000

r4000 = (renda-4500)*0.28 + cal_renda2000*0.08 + cal_renda3000*0.18
if renda > 2000:
    if renda >2000 and renda<=3000:
        cal_renda2000 = (renda-2000)
        r2000 = (cal_renda2000)*0.08
        print(f'{r2000:.2f}')
    elif renda >3000 and renda <=4500:
        cal_renda3000 = (renda-3000)
        cal_renda2000 = (renda-2000)-cal_renda3000
        r3000 = ((cal_renda3000)*0.18) + ((cal_renda2000)*0.08)
        print(f'{r3000:.2f}')
    elif renda>4500:
        print(f'{r4000:.2f}')
else:
    print('isento')