import argparse

parser = argparse.ArgumentParser()

parser.add_argument('infile', type=argparse.FileType('r'))
parser.add_argument('-medals', nargs=2)
parser.add_argument('-output', '--output')
parser.add_argument('-total')
parser.add_argument('-overall', nargs='+')
parser.add_argument('-interactive', nargs='*')

args = parser.parse_args()



interactive = False
def medals(table_medalists, send_country = None, send_year = None):
    list_medalists = []
    medals_amount = {'gold': 0, 'silver': 0, 'bronze': 0}
    if not interactive:
        country = args.medals[0]
        year = args.medals[1]
    else:
        country = send_country
        year = send_year

    county_existence = 0
    year_existence = 0
    for i in range(len(table_medalists)):
        player = table_medalists[i].split('\t')
        player[-1] = ''.join(list(player[-1])[:-1])
        if country == player[6] or country == player[7]:
            if year == player[9] and player[-1] != 'NA':
                list_medalists.append(player[1] + ' - ' + player[-3] + ' - ' + player[-1])
                if player[-1] == 'Gold':
                    medals_amount['gold'] += 1
                elif player[-1] == 'Silver':
                    medals_amount['silver'] += 1
                elif player[-1] == 'Bronze':
                    medals_amount['bronze'] += 1
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


def total(table_totals, send_year = None):
    list_medalists = []
    list_countries = []
    dict_countries = {}
    result = []
    if not interactive:
        year = args.total
    else:
        year = send_year

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
        print("There was no olympics during this year.")
    else:
        for i in range(len(list_countries)):
            result.append(
                f"{list_countries[i]} - gold {dict_countries[list_countries[i]]['gold']} - silver {dict_countries[list_countries[i]]['silver']} - bronze {dict_countries[list_countries[i]]['bronze']}")
            print(
                f"{list_countries[i]} - gold {dict_countries[list_countries[i]]['gold']} - silver {dict_countries[list_countries[i]]['silver']} - bronze {dict_countries[list_countries[i]]['bronze']}")
    return result



def output(medalist_list, outfile):
    with open(outfile, 'w') as file:
        for player in medalist_list:
            file.write(player + '\n')


def overall(info, countries):
    l_results = []
    for team in countries:
        team_year_stat = {}

        for player in info[1:]:
            player = player.split('\t')

            if (player[6] == team or player[7] == team) and player[-1] != "NA\n":

                if player[9] in team_year_stat:
                    team_year_stat[player[9]] += 1
                else:
                    team_year_stat[player[9]] = 1

        year_more = 0
        count_medals = 0

        for year in team_year_stat:
            if team_year_stat[year] == max(team_year_stat.values()):
                year_more = year
                count_medals = team_year_stat[year]
                break

        print(f"{team} best year is: {year_more}, count of medals: {count_medals}")
        l_results.append(f"{team} best year is: {year_more}, count of medals: {count_medals}")
    return l_results

def country_statistic(info, country):

    l_results = []
    team_year_stat = {}

    count_gold = 0
    count_silver = 0
    count_bronze = 0

    for player in info[1:]:
        player = player.split('\t')

        if (player[6] == country or player[7] == country)  and player[-1] != "NA\n":
            if "Gold" in player[-1]:
                count_gold += 1
            elif "Silver" in player[-1]:
                count_silver += 1
            else:
                count_bronze += 1

            if int(player[9]) in team_year_stat:
                team_year_stat[int(player[9])] += 1
            else:
                team_year_stat[int(player[9])] = 1

    year_more = 0
    count_medals_more = 0

    year_less = 0
    count_medals_less = 0

    for year in team_year_stat:
        if team_year_stat[year] == max(team_year_stat.values()):
            year_more = year
            count_medals_more = team_year_stat[year]

        if team_year_stat[year] == min(team_year_stat.values()):
            year_less =  year
            count_medals_less = team_year_stat[year]



    where_first_game = ""

    for player in info[1:]:
        player = player.split('\t')

        if player[6] == country and min(team_year_stat) == int(player[9]):
            where_first_game = player[11]

    print(f"{country} first olympic game is at {min(team_year_stat)} in {where_first_game}")
    l_results.append(f"{country} first olympic game is at {min(team_year_stat)} in {where_first_game}")

    print(f"{country} best year is: {year_more}, count of medals: {count_medals_more}")
    l_results.append(f"{country} best year is: {year_more}, count of medals: {count_medals_more}")

    print(f"{country} terrible year is: {year_less}, count of medals: {count_medals_less}")
    l_results.append(f"{country} best year is: {year_less}, count of medals: {count_medals_less}")

    print(f"Gold: {count_gold}, Silver: {count_silver}, Bronze: {count_bronze}")
    l_results.append(f"Gold: {count_gold}, Silver: {count_silver}, Bronze: {count_bronze}")

    return l_results


with args.infile as file:
    lines = file.readlines()

    if args.medals != None:
       result_players = medals(lines)
       if args.output != None:
           output(result_players, args.output)



    elif args.overall !=None:
        countries = args.overall
        overall_list = overall(lines, countries)

        if args.output != None:
            output(overall_list, args.output)

    elif args.interactive != None:
        interactive = True
        while True:
            command = input('Enter command: ')
            args = command.split(" ")
            if args[0] == '-medals':
                result_players = medals(lines, args[1], args[2])
                if args[-2] == '-output':
                    output(result_players, args[-1])

            elif args[0] == '-overall':
                if '-output' in args:
                    countries = args[1: args.index('-output')]
                else:
                    countries = args[1:]

                overall_list = overall(lines, countries)
                if '-output' in args:
                    output(overall_list, args[-1])
            elif args[0] == '-total':
                result_country = total(lines, args[1])
                if args[-2] == '-output':
                    output(result_country, args[-1])
            else:
                if '-output' in command:
                    stat_res = country_statistic(lines, command.split(" ")[0])
                    if args[-2] == '-output':
                        output(stat_res, args[-1])
                else:
                     country_statistic(lines, command)

    elif args.total != None:
        result_country = total(lines)
        if args.output != None:
            output(result_country, args.output)

    else:
        print('You entered a wrong argument')
