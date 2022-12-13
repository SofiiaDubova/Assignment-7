import sys

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
if 5 <= len(sys.argv) <= 7 and len(sys.argv) != 6:
    open_file = sys.argv[1]
    with open(open_file, 'r') as file:
        lines = file.readlines()
        if sys.argv[2] == '-medals':
            result_players, player_medals = medals(lines)
            for e in result_players:
                print(e)
            print(player_medals)
            if sys.argv[5] == '-output':
                output(result_players, sys.argv[6])
        else:
            print('You entered a wrong argument')
else:
    print('You did not enter all the arguments.')
