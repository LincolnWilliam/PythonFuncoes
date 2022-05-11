def anoSeculo():

    if ano >=1 and ano <=100:
        print('Corresponde ao Século:',romanosDict[1])
    elif ano >= 101 and ano <= 200:
        print('Corresponde ao Século: ',romanosDict[2])
    elif ano >= 201 and ano <= 300:
        print('Corresponde ao Século: ',romanosDict[3])
    elif ano >= 301 and ano <= 400:
        print('Corresponde ao Século: ',romanosDict[4])
    elif ano >= 401 and ano <= 500:
        print('Corresponde ao Século: ',romanosDict[5])
    elif ano >= 501 and ano <= 600:
        print('Corresponde ao Século: ',romanosDict[6])
    elif ano >= 601 and ano <= 700:
        print('Corresponde ao Século: ',romanosDict[7])
    elif ano >= 701 and ano <= 800:
        print('Corresponde ao Século: ',romanosDict[8])
    elif ano >= 801 and ano <= 900:
        print('Corresponde ao Século: ',romanosDict[9])
    elif ano >= 901 and ano <= 1000:
        print('Corresponde ao Século: ',romanosDict[10])
    elif ano >= 1001 and ano <= 1100:
        print('Corresponde ao Século: ',romanosDict[11])
    elif ano >= 1101 and ano <= 1200:
        print('Corresponde ao Século: ',romanosDict[12])
    elif ano >= 1201 and ano <= 1300:
        print('Corresponde ao Século: ',romanosDict[13])
    elif ano >= 1301 and ano <= 1400:
        print('Corresponde ao Século: ',romanosDict[14])
    elif ano >= 1401 and ano <= 1500:
        print('Corresponde ao Século: ',romanosDict[15])
    elif ano >= 1501 and ano <= 1600:
        print('Corresponde ao Século: ',romanosDict[16])
    elif ano >= 1601 and ano <= 1700:
        print('Corresponde ao Século: ',romanosDict[17])
    elif ano >= 1701 and ano <= 1800:
        print('Corresponde ao Século: ',romanosDict[18])
    elif ano >= 1801 and ano <= 1900:
        print('Corresponde ao Século: ',romanosDict[19])
    elif ano >= 1901 and ano <= 2000:
        print('Corresponde ao Século: ',romanosDict[20])
    elif ano >= 2001 and ano <= 2100:
        print('Corresponde ao Século: ',romanosDict[21])
    elif ano >= 2101 and ano <= 2200:
        print('Corresponde ao Século: ',romanosDict[22])
    elif ano >= 2201 and ano <= 2300:
        print('Corresponde ao Século: ',romanosDict[23])
    elif ano >= 2301 and ano <= 2400:
        print('Corresponde ao Século: ',romanosDict[24])
    elif ano >= 2401 and ano <= 2500:
        print('Corresponde ao Século: ',romanosDict[25])
    elif ano >= 2501 and ano <= 2600:
        print('Corresponde ao Século: ',romanosDict[26])
    elif ano >= 2601 and ano <= 2700:
        print('Corresponde ao Século: ',romanosDict[27])
    elif ano >= 2701 and ano <= 2800:
        print('Corresponde ao Século: ',romanosDict[28])
    elif ano >= 2801 and ano <= 2900:
        print('Corresponde ao Século: ',romanosDict[29])
    elif ano >= 2901 and ano <= 3000:
        print('Corresponde ao Século: ',romanosDict[30])
    else:
        print('Valor invalido!')

try:
        print('########## sistema irá retornar o século do ano informado \nem algarismo romano em um limite de até o ano 3000 ##########')
        ano = 0
        ano = int(input('informe o Ano : '))
        seculo = (ano / 100) + 1

except ValueError:
    print('valor  é invalido, só aceita númericos!')

romanosDict =\
        {
                1: "I",
                2: "II",
                3: "III",
                4: "IV",
                5: "V",
                6: "VI",
                7: "VII",
                8: "VIII",
                9: "IX",
                10: "X",
                11: "XI",
                12: "XII",
                13: "XIII",
                14: "XIV",
                15: "XV",
                16: "XVI",
                17: "XVII",
                18: "XVIII",
                19: "XIX",
                20: "XX",
                21: "XXI",
                22: "XXII",
                23: "XXIII",
                24: "XXIV",
                25: "XXV",
                26: "XXVI",
                27: "XXVII",
                28: "XXVIII",
                29: "XXIX",
                30: "XXX",

            }

anoSeculo()
