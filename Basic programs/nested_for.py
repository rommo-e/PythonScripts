# As an example we can define first a list of elements for 4 different teams
# They have to play agaisnt each other but they can't play agaisnt it self

teams = ['Dragons' , 'Unicorns' , 'Bears', 'Bulls']

for home_team in teams:
    for away_team in teams:
        if away_team != home_team:
            print(home_team +" vs " + away_team)

