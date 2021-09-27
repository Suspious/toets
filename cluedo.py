print(''''---------------------------
hallo welkom bij de cluedo try outs.
We gaan je vandaag een paar vragen stellen waar je j of n kan beantwoorden.
dit kan je vertellen welke rol precies bij je past.
''')

locatie = input('kan je zelf naar de locatie in rotterdam komen?j/n\n').lower()
opleiding = input('heb je een mbo niveau 4 opleiding gedaan in acteren.?j/n\n').lower()
if opleiding and locatie =='j':
    gender = input('ben u een man of vrouw?\n')
    