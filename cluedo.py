print(''''---------------------------
hallo welkom bij de cluedo try outs.
We gaan je vandaag een paar vragen stellen waar je j of n kan beantwoorden.
dit kan je vertellen welke rol precies bij je past.
''')
lijst ='ja','j','yes','y'
lijstnee ='nee','n','nooit','no','nein'
locatie = input('kan je zelf naar de locatie in rotterdam komen?j/n\n').lower()
opleiding = input('heb je een mbo niveau 4 opleiding gedaan in acteren.?j/n\n').lower()
if opleiding and locatie in lijst:
    gender = input('ben u een man of vrouw?\n')
    if gender =='man':
        while gender:
        #hierzo ben ik bezig met die kolonel ofso
            militair = input('heb je een militaire achter grond?\n')
            if militair in lijst:
                gestolen = input("heb je ooit iets gestolen? \n")
                if gestolen in lijst:
                    verdacht = input('heb je ooit iets verdachts gedaan? \n' )
                    if verdacht in lijst:
                        print('Je mag op auditie voor de rol van Kolonel van Geelen')
                        break
            dominee = input("weet je hoe een dominee speelt?\n")
            if dominee in lijst:
                rol = input('weet jij hoe je je rol moet spelen\n')
                if rol in lijst:
                    leeftijd3 = input('ben jij ouder dan 40')
                    if leeftijd3 in lijst:
                        print("Je mag op auditie voor de rol van Dominee Groenewoud")
                        break
            pimpel = input('kan jij praten als een professor?\n')
            if pimpel in lijst:
                doen = input("heb je enig idee wat proffesors doen?\n ")
                if doen in lijst:
                    dinosaurussen = input('weet je van dinosaurussen?\n')
                    if dinosaurussen in lijst:
                        print('Je mag op auditie voor de rol van Professor Pimpel')
                        break
    if gender =='vrouw':
        while gender:
            pruik =input('wil jij een pruik dragen mocht dat nodig zijn? \n')
            if pruik in lijst:
                getrouwd = input('ben je getrouwd met iemand \n')
                if getrouwd in lijst:
                    leeftijd = input('ben jij ouder dan 40?\n ')
                    if leeftijd in lijst:
                        print('Je mag op auditie voor de rol van Mevrouw de Wit\n')
                        break
            #dit is die van rosa
            jaloer = input('ben je snel jaloers?\n ')
            if jaloer in lijst:
                makeup = input('ben je bereid om make up op te doen?\n ')
                if makeup in lijst:
                    vermoeid = input('ben je snel vermoeid? \n')
                    if vermoeid in lijst:
                        print('Je mag op auditie voor de rol van Rosa Roodhart')
                        break
            #die van draet
            stoer = input('ben je een echte stoere vrouw?\n')
            if stoer in lijst:
                feest = input('hou jij van feest?\n ')
                if feest in lijst:
                    chantage = input('herken jij jezelf bij chantage? \n')
                    if chantage in lijst:
                        print('Je mag op auditie voor de rol van Mevrouw Blaauw van Draet')
                        break

                    
            


