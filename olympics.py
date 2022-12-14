import sys

def total(file):
    list_medalists = []
    list_countries = []
    dict_countries = {}
    result = []
    year = sys.argv[4]
    for i in range(len(file)):
        country = file[i].split('\t')
        country[-1] = ''.join(list(country[-1])[:-1])
        if country[9] == year and country[-1] != 'NA':
            countries = country[6] + "  " + country[-1]
            list_medalists.append(countries.split('  '))
    for i in range(len(list_medalists)):
        for j in range(len(list_medalists[i])):
            if list_countries.count(list_medalists[i][0]) == 0:
                list_countries.append(list_medalists[i][0])
    for i in range(len(list_countries)):
        if list_medalists[i][1] == 'Bronze':
            dict_countries[list_medalists[i][0]]['bronze'] += 1
        elif list_medalists[i][1] == 'Silver':
            dict_countries[list_medalists[i][0]]['silver'] += 1
        elif list_medalists[i][1] == 'Gold':
            dict_countries[list_medalists[i][0]]['gold'] += 1
    if len(list_medalists) == 0:
        print('There was no olympics during this year.')
    else:
        for i in range(len(list_countries)):
            result.append(f"{list_countries[i]} - gold {dict_countries[list_countries[i]]['gold']} - silver {dict_countries[list_countries[i]]['silver']} - bronze {dict_countries[list_countries[i]]['bronze']}")
            print(f"{list_countries[i]} - gold {dict_countries[list_countries[i]]['gold']} - silver {dict_countries[list_countries[i]]['silver']} - bronze {dict_countries[list_countries[i]]['bronze']}")
        return result


def medals(file):
    list_medalists = []
    medals_amount = {'bronze': 0, 'silver': 0, 'gold': 0}
    country = sys.argv[3]
    year = sys.argv[4]
    county_existence = True
    year_existence = True
    for i in range(len(file)):
        player = file[i].split('\t')
        player[-1] = ''.join(list(player[-1])[:-1])
        if country == player[6] or country == player[7]:
                if year == player[9]:
                        if player[-1] != 'NA':
                            list_medalists.append(player[1] + ' - ' + player[-3] + ' - ' + player[-1])
                            if player[-1] == 'Bronze':
                                medals_amount['bronze'] += 1
                            elif player[-1] == 'Silver':
                                medals_amount['silver'] += 1
                            elif player[-1] == 'Gold':
                                medals_amount['gold'] += 1
                else:
                    year_existence = True
        else:
            county_existence = True
        if len(list_medalists) == 10 or county_existence == False or year_existence == False:
            break
    print(year_existence)
    if len(list_medalists) < 10:
        if county_existence == False:
            print('There is no such country.')
        elif year_existence == False:
            print('There was no olympics during this year.')
        else:
            print('The country has less than 10 medals.')
    return list_medalists, medals_amount

def output(medalist_list, outfile):
    with open(outfile, 'a') as file:
        for player in medalist_list:
            file.write(player + '\n')
if len(sys.argv) >= 4:
    open_file = sys.argv[1]
    with open(open_file, 'r') as file:
        lines = file.readlines()
        if sys.argv[2] == '-medals':
            result_players, player_medals = medals(lines)
            for e in result_players:
                print(e)
            print(player_medals)
            if sys.argv[-2] == '-output':
                output(result_players, sys.argv[-1])
        elif sys.argv[2] == '-total':
            result_country = total(lines)
            if sys.argv[-2] == '-output':
                output(result_country, sys.argv[-1])
        else:
            print('You entered a wrong argument')
else:
    print('You did not enter all the arguments.')
