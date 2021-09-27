print(''''---------------------------
hallo welkom bij de cluedo try outs.
We gaan je vandaag een paar vragen stellen waar je j of n kan beantwoorden.
dit kan je vertellen welke rol precies bij je past.
''')
k = input('heb je meer dan 24 kinderen? \n')
i = input("heb je een mbo dipbloma in acteren? j/n \n").lower()
if i and k =="j":
    k = input('heb je een militaire achtergrond?').lower()
    if k =='j':
        vraag3 = input('heb je ooit iets gestolen? ').lower()
        if vraag3 == 'ja':
            b = input('heb je ooit iets verdachts gedaan? ' )
            if b =='j':
               print('Je mag op auditie voor de rol van Kolonel van Geelen')
    if k =='n':
        o = input('heeft u een overleden vader? ' )
        if o =='j':
            q = ("bent u familie met een over Dr.Swart? \n  ")
            if q =='j':
                print('Je mag op auditie voor de rol van Mevrouw de Wit')
else: 

    print('je voldoet helaat niet aan de eisen, mijn excuses')
