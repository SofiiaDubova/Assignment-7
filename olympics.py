import sys


def medals(table_medalists):
    if len(sys.argv) >= 5:
        list_medalists = []
        medals_amount = {'bronze': 0, 'silver': 0, 'gold': 0}
        country = sys.argv[3]
        year = sys.argv[4]
        county_existence = 0
        year_existence = 0
        for i in range(len(table_medalists)):
            player = table_medalists[i].split('\t')
            player[-1] = ''.join(list(player[-1])[:-1])
            if country == player[6] or country == player[7]:
                if year == player[9] and player[-1] != 'NA':
                    list_medalists.append(player[1] + ' - ' + player[-3] + ' - ' + player[-1])
                    if player[-1] == 'Bronze':
                        medals_amount['bronze'] += 1
                    elif player[-1] == 'Silver':
                        medals_amount['silver'] += 1
                    elif player[-1] == 'Gold':
                        medals_amount['gold'] += 1
                else:
                    year_existence += 1
            else:
                county_existence += 1
            if len(list_medalists) == 10:
                break
        if len(list_medalists) < 10:
            if county_existence == len(table_medalists):
                print('There is no such country.')
            elif year_existence == len(table_medalists) - county_existence:
                print('There was no olympics during this year.')
            else:
                print('The country has less than 10 medals.')
        else:
            for e in list_medalists:
                print(e)
            print(medals_amount)
        return list_medalists
    else:
        print('You did not enter all the arguments.')


def total(table_totals):
    if len(sys.argv) >= 4:
        list_medalists = []
        list_countries = []
        dict_countries = {}
        result = []
        year = sys.argv[3]
        for i in range(len(table_totals)):
            country = table_totals[i].split('\t')
            country[-1] = ''.join(list(country[-1])[:-1])
            if country[9] == year and country[-1] != 'NA':
                countries = country[6] + "   " + country[-1]
                list_medalists.append(countries.split('   '))
        for i in range(len(list_medalists)):
            for j in range(len(list_medalists[i])):
                if list_countries.count(list_medalists[i][0]) == 0:
                    list_countries.append(list_medalists[i][0])
        for i in range(len(list_countries)):
            dict_countries[list_countries[i]] = {'bronze': 0, 'silver': 0, 'gold': 0}
        for i in range(len(list_medalists)):
            if list_medalists[i][1] == 'Bronze':
                dict_countries[list_medalists[i][0]]['bronze'] += 1
            elif list_medalists[i][1] == 'Silver':
                dict_countries[list_medalists[i][0]]['silver'] += 1
            elif list_medalists[i][1] == 'Gold':
                dict_countries[list_medalists[i][0]]['gold'] += 1
        if len(list_medalists) == 0:
            print("В цьому році не проводилася олімпіада!")
        else:
            for i in range(len(list_countries)):
                result.append(
                    f"{list_countries[i]} - gold {dict_countries[list_countries[i]]['gold']} - silver {dict_countries[list_countries[i]]['silver']} - bronze {dict_countries[list_countries[i]]['bronze']}")
                print(
                    f"{list_countries[i]} - gold {dict_countries[list_countries[i]]['gold']} - silver {dict_countries[list_countries[i]]['silver']} - bronze {dict_countries[list_countries[i]]['bronze']}")
        return result
    else:
        print('You did not enter all the arguments.')


def output(medalist_list, outfile):
    with open(outfile, 'w') as file:
        for player in medalist_list:
            file.write(player + '\n')


open_file = sys.argv[1]
with open(open_file, 'r') as file:
    lines = file.readlines()
    if sys.argv[2] == '-medals':
        result_players = medals(lines)
        if sys.argv[-2] == '-output':
            output(result_players, sys.argv[-1])
    elif sys.argv[2] == '-total':
        result_country = total(lines)
        if sys.argv[-2] == '-output':
            output(result_country, sys.argv[-1])
    else:
        print('You entered a wrong argument')
