def arab2rom(digit):
    edinicy = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    desyatki = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    sotni = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    tysyachi = ["","M","MM"]
    
    t = tysyachi[digit // 1000]
    s = sotni[digit // 100 % 10]
    d = desyatki[digit // 10 % 10]
    e =  edinicy[digit % 10]
    
    return t+s+d+e

digit=int(input())
print(arab2rom(digit))