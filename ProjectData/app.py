# module defines an application to curate a playlist

import pandas as pd


from helper import helper
from db_operations import db_operations

import mysql.connector
# import uuid


password = 'j97L(NL"39w2xM`6'
conn = mysql.connector.connect(

                                    host="34.136.134.242",
                                    # host = "localhost",
                                    user="root",
                                    password=password,
                                    auth_plugin='mysql_native_password',
                                    database='cpsc408')
cursor = conn.cursor()

# cursor.execute("SHOW TABLES")
# myresults = cursor.fetchall()
# for r in myresults:
    # print(r)

# def remove_comma():
#     with open('Ligue1/L1Fixtures.csv', 'r') as r, open('Ligue1/L.csv', 'w') as w:
#         for num, line in enumerate(r):
#             if num > 0:
#                 newline = line[:-2] + "\n" if "\n" in line else line[:-1]
#             else:
#                 newline = line
#             w.write(newline)
# remove_comma()

SeriaATable = helper.data_cleaner("SeriaA/SATable.csv")
premTable = helper.data_cleaner("Prem/PLTable.csv")
Ligue1Table = helper.data_cleaner("Ligue1/L1TableEdit.csv")
BundesligaTable = helper.data_cleaner("Bundesliga/BLTable.csv")
LaLigaTable = helper.data_cleaner("LaLiga/LaLigaTable.csv")

SeriaAFixtures = helper.data_cleaner("SeriaA/SAFixtures.csv")
PremFixtures = helper.data_cleaner("Prem/PLFixturesEdit.csv")
LaLigaFixtures = helper.data_cleaner("LaLiga/LLFixtures.csv")
BundesligaFixtures = helper.data_cleaner("Bundesliga/BLFixturesEdit.csv")
Ligue1Fixtures  = helper.data_cleaner("Ligue1/L1FixturesEdit.csv")

SeriaANationalities = helper.data_cleaner("SeriaA/SANationalities.csv")
PremNationalities = helper.data_cleaner("Prem/PLNationalities.csv")
LaLigaNationalities = helper.data_cleaner("LaLiga/LLNationalities.csv")
BundesligaNationalities = helper.data_cleaner("Bundesliga/BLNationality.csv")
Ligue1Nationalities  = helper.data_cleaner("Ligue1/L1Nationalities.csv")

PREMMANAGERS = helper.data_cleaner("Prem/PLManagers.csv")





# function inserts data into table if it is empty
def pre_process(TABLE,data):
    attribute_count = len(data[0])
    # placeholders = ("?,"*attribute_count)[:-1]
    placeholders = ("%s,"*attribute_count)[:-1]

    # print(placeholders)
    query = "INSERT INTO "+TABLE+ " VALUES("+placeholders+")"


    print(query)
    print(attribute_count)

    cursor.executemany(query,data[1:])

    conn.commit()



def start_screen():
    print("Welcome to your APP!")


# show user options
def options():
    print("Select from the following menu options:\n1 Find Top 6 of a league\n" \
    "2 Find top goal scorer on a team\n" "3 Find the 5 players with the most yellow or red cards\n" "4 Download a teams schedule as a csv\n"\
    "5 Find the team with the most distinct nationalities represented on their team\n" "6 Update a players age \n""7 Add a new player to a league\n" \
    "8 Delete a player from a league\n""9 Show average match attendance per league\n" "10 Show best offensive players by a stat\n" "11 Exit\n")

    return helper.get_choice([1,2,3,4,5,6,7,8,9,10,11])

#top 6 of a league
def League_Top6():
    features = ['BundesligaTable','LaLigaTable','Ligue1Table','PremTable','SeriaATable'] # features to show the user
    choices = {}
    for i in range(len(features)):
        print(i,features[i])
        choices[i] = features[i]
    index = helper.get_choice(choices.keys())
    # print(features[index])
    query = "SELECT Squad, FinalRank FROM "+ features[index] + " LIMIT 6"
    print()
    print("Top 6 teams: ")

    execute = cursor.execute(query)
    teams = cursor.fetchall()
    print ("{:<25} {:<3}".format('Team','Rank'))
    # print("TEAM       YellowCards RedCards Player")
    for team in teams:
        # for ind in player:
        #     iter = 0
            # print(ind)
        # name = str(player).strip("'',()'").split("\\",1)
        # name = name[0]
        print ("{:<25} {:<3}".format(team[0],team[1]))

    print()

# create a player
def create_player():
    print("What league does the player play in?")
    features = ['BundesligaPlayers','LaLigaPlayers','Ligue1Players','PremPlayers','SeriaAPlayers'] # features to show the user
    choices = {}
    for i in range(len(features)):
        print(i,features[i])
        choices[i] = features[i]
    index = helper.get_choice(choices.keys())
    player = []
    name = input("What is the players name?\n")
    player.append(name)
    country = input('What is the 3 letter code for players Country?\n')
    player.append(country,)
    position = input("What is the players position? ex: MF DF or FW\n")
    player.append(position)
    team = input("What team does the player play for?\n")
    player.append(team)

    # country =
    incomplete = True
    while incomplete:
        age = input("How old is the player?\n")
        try:
            mark = int(age)
            player.append(mark)
            incomplete = False
        except ValueError:
            print('\nYou did not enter a valid integer for age')

    notDone = True
    while notDone:
        born = input("What year was the player born in?\n")

        try:
            b = int(born)
            player.append(b)
            notDone = False
        except ValueError:
            print('\nYou did not enter a valid integer for year born')
            # sys.exit(0)

    # print(player)
    one = str(player).replace('[','(')
    two = one.replace(']',')')
    # print(two)
    query = "INSERT INTO " + features[index] + " (Player, Nation, Position, Squad,Age,Born) " + "VALUES " + two
    print(query)
    cursor.execute(query)
    conn.commit()

# # option 2, search table for top goal scorer on a team
def search_by_league():
    features = ['BundesligaTable','LaLigaTable','Ligue1Table','PremTable','SeriaATable'] # features to show the user
    choices = {}
    for i in range(len(features)):
        print(i,features[i])
        choices[i] = features[i]
    index = helper.get_choice(choices.keys())

    query = "SELECT Squad FROM "+ features[index]

    print("Teams in League:")

    teams1 = cursor.execute(query)

    myresults = cursor.fetchall()
    for r in myresults:
        print(r)
    print()

    print("Which team would you like to see top scorer for? ")

    choices2 = {}
    for j in range(len(teams)):
        print(j,teams[j])
        choices2[j] = teams[j]
    index2 = helper.get_choice(choices2.keys())
    teamSelected = str(choices2[index2])

    teamSelected = teamSelected.strip("',()'")
    print("TEAM SELECTED "+teamSelected)
    print()

    query2 = "SELECT TopTeamScorer FROM " + features[index]+ " WHERE Squad LIKE '%" + teamSelected +"%'"

    print("TOP GOAL SCORER FOR " + teamSelected)

    cursor.execute(query2)
    player = cursor.fetchone()
    player = str(player)
    player = player.strip("',()'")
    print(player)
    print()

#find dirtiest player
def dirtiest_player():
    features = ['YellowCards','RedCards'] # features to show the user
    choices = {}
    print("Players with most Yellow or RedCards?")

    for i in range(len(features)):
        print(i,features[i])
        choices[i] = features[i]
    index = helper.get_choice(choices.keys())
    # print(features[index])
    query = '''
    SELECT Player,Squad,YellowCards,RedCards FROM BundesligaPlayers as BP
    UNION ALL
    SELECT Player,Squad,YellowCards,RedCards FROM LaLigaPlayers as LL
    UNION ALL
    SELECT Player,Squad,YellowCards,RedCards FROM SerieAPlayers
    UNION ALL
    SELECT Player,Squad,YellowCards,RedCards FROM PremPlayers
    UNION ALL
    SELECT Player,Squad,YellowCards,RedCards FROM Ligue1Players
    ORDER BY
    '''+ features[index]+" DESC LIMIT 5"




    cursor.execute(query)
    dirtiestPlayers = cursor.fetchall()
    # print(dirtiestPlayers)
    print()
    print ("{:<30} {:<25} {:<13} {:<13}".format('Player','Team','Yellow Cards','Red Cards'))

    for player in dirtiestPlayers:

        name = str(player).strip("'',()'").split("\\",1)
        name = name[0]
        print ("{:<30} {:<25} {:<13} {:<13}".format(name,player[1],player[2],player[3]))


    print()

def avg_attendance_league(): #uses subquery
    query = '''
SELECT l.leagueName, AVG(a.Attendance) as AvgAttendance
FROM
(SELECT Attendance,LeagueID FROM BUNDESLIGAFIXTURES as BP
    UNION ALL
    SELECT Attendance, LeagueID FROM LALIGAFIXTURES as LL
    UNION ALL
    SELECT Attendance, LeagueID FROM SERIEAFIXTURES
    UNION ALL
    SELECT Attendance, LeagueID FROM PREMFIXTURES
    UNION ALL
    SELECT Attendance, LeagueID FROM LIGUE1FIXTURES) AS a
    INNER JOIN Leagues l ON a.LeagueID = l.LeagueID
    GROUP BY l.leagueName;
    '''
    cursor.execute(query)
    results = cursor.fetchall()

    print()
    print ("{:<20} {:<5}".format('League','Average Attendance'))


    for r in results:
        league = r[0]
        attendance = r[1]
        print ("{:<20} {:<5}".format(league,attendance))
    print()

def team_diversity(): #uses subQuery
    features = ['Most','Least'] # features to show the user
    choices = {}
    for i in range(len(features)):
        print(i,features[i])
        choices[i] = features[i]
    index = helper.get_choice(choices.keys())

    # print(features[index])
    if index== 0:
        features[index] = "DESC"
    else:
        features[index] = "ASC"
    query = '''
    SELECT a.Squad,COUNT(DISTINCT (a.Nation)) as diversity FROM
    (SELECT * FROM BundesligaPlayers as BP
    UNION ALL
    SELECT * FROM LaLigaPlayers as LL
    UNION ALL
    SELECT * FROM SerieAPlayers
    UNION ALL
    SELECT * FROM PremPlayers
    UNION ALL
    SELECT * FROM Ligue1Players
    ) a
    GROUP BY a.Squad
    ORDER BY diversity
    ''' + features[index] + " LIMIT 5"

    d = cursor.execute(query)
    diversity = cursor.fetchall()

    print()
    print ("{:<25} {:<3}".format('Team','Different Nations on Team'))

    for r in diversity:
        print ("{:<25} {:<3} ".format(r[0],r[1]))

# add LeagueIDs
def add_leagues():

    four = "ALTER TABLE PremPlayers ADD LeagueID INTEGER DEFAULT (4);"

    two ="ALTER TABLE LaLigaPlayers ADD LeagueID INTEGER DEFAULT (2);"

    one ="ALTER TABLE BundesligaPlayers ADD LeagueID INTEGER DEFAULT (1);"

    three ="ALTER TABLE Ligue1Players ADD LeagueID INTEGER DEFAULT (3);"

    five = "ALTER TABLE SerieAPlayers ADD LeagueID INTEGER DEFAULT(5);"

    cursor.execute(one)
    cursor.execute(two)
    cursor.execute(three)
    cursor.execute(four)
    cursor.execute(five)




# option 8 delete a player
def delete_player():
    print("What league is the player in? Please enter the number next to the League")
    features = ['BundesligaPlayers','LaLigaPlayers','Ligue1Players','PremPlayers','SerieAPlayers'] # features to show the user
    choices = {}
    for i in range(len(features)):
        print(i,features[i])
        choices[i] = features[i]
    index = helper.get_choice(choices.keys())
    playerName = input("Select player you want to delete:\n")
    if doesPlayer_exist(playerName,features[index]):
        print("DELETING RESULTS")
        query = "DELETE FROM " + features[index] + " WHERE Player LIKE '%" + playerName +"%'"

        cursor.execute(query)
        conn.commit()
        print("Player(s) have been deleted. ")
    else:
        print("Did not delete player.\n")

def team_csv():

    features = ['BundesligaTable','LaLigaTable','Ligue1Table','PremTable','SeriaATable'] # features to show the user
    choices = {}
    for i in range(len(features)):
        print(i,features[i])
        choices[i] = features[i]
    index = helper.get_choice(choices.keys())
    # print("INDEX: "+)
    query = "SELECT DISTINCT Squad FROM "+ features[index]

    print("Which team do you want to download schedule for:")

    t = cursor.execute(query)
    teams = cursor.fetchall()

    choices2 = {}
    for j in range(len(teams)):
        print(j,teams[j])
        choices2[j] = teams[j]
    index2 = helper.get_choice(choices2.keys())
    teamSelected = str(choices2[index2])

    teamSelected = teamSelected.strip("',()'")
    print("TEAM SELECTED "+teamSelected)
    print()

    fixtures = ['BUNDESLIGAFIXTURES','LALIGAFIXTURES','LIGUE1FIXTURES','PREMFIXTURES','SERIEAFIXTURES']
    q = "SELECT * FROM " + fixtures[index] + " WHERE HomeTeam LIKE '%" +teamSelected+ "%' OR AwayTeam LIKE'%" + teamSelected + "%'"
    # print(q)
    cursor.execute(q)
    myresults = cursor.fetchall()
    columns = ["MatchWeek" ,
    "DayofWeek",
    "Date" ,
    "LocalTimeofGame" ,
    "HomeTeam" ,
    "ExpectedHomeGoals",
    "Score" ,
    "ExpectedAwayGoals" ,
    "AwayTeam" ,
    "Attendance" ,
    "Venue" ,
    "Referee",
    "LeagueID" ]
    df = pd.DataFrame(myresults)
    df.columns = columns
    path = teamSelected+".csv"
    df.to_csv(path) #write to csv

# update age uses rollback
def update_age():
    print("What league is the player in? Please enter the number next to the League")
    features = ['BundesligaPlayers','LaLigaPlayers','Ligue1Players','PremPlayers','SerieAPlayers'] # features to show the user
    choices = {}
    for i in range(len(features)):
        print(i,features[i])
        choices[i] = features[i]
    index = helper.get_choice(choices.keys())
    playerName = input("Select player you want to update age of:\n")
    updateAge = input("What is the players current age: \n")
    tran = "START TRANSACTION;"
    cursor.execute(tran)
    if doesPlayer_exist(playerName,features[index]):
        print("UPDATING RESULTS")
        query = "UPDATE " + features[index] + " SET AGE = " +updateAge +" WHERE Player LIKE '%" + playerName +"%'"
        # print(query)


        cursor.execute(query)
        data = cursor.fetchall()
        check = "SELECT Player, AGE FROM " +features[index] +" WHERE Player LIKE '%" + playerName + "%'"
        # print(check)
        cursor.execute(check)
        player = cursor.fetchall()

        print("THIS IS THE CHANGE YOU JUST MADE, IF YES WILL COMMIT IF NO ROLLBACK")
        for r in player:
            print(r)


        YESNO= ['NO','YES']
        choices2 = {}
        for j in range(len(YESNO)):
            print(j,YESNO[j])
            choices2[j] = YESNO[j]
        index2 = helper.get_choice(choices2.keys())
        if index2 ==1:
            conn.commit()
            com = "COMMIT;"
            cursor.execute(com)
            print("COMMITTED.\n  ")
            # return True
        else:
            roll = "ROLLBACK;"
            # print(roll)
            print("ROLLED BACK\n")
            cursor.execute(roll)
            # print("will not delete any of these players, try again or be more specific.")

    else:
        print("Did not delete player.")



# find if player exists
def doesPlayer_exist(playerName,playerLeague):


    query = "SELECT Player, Squad,Nation,Age FROM "+playerLeague+ " WHERE Player LIKE '%" + playerName + "%'"

    cursor.execute(query)
    row = cursor.fetchall()
    conn.commit()


    if not row:
        print("There are no players with this name goodbye!\n")
        return False
    else:
        print("There are results\n")
        print ("{:<25} {:<20} {:<10}{:<3}".format('Player','Squad','Nation','Age'))
        for r in row:
            name = str(r).strip("'',()'").split("\\",1)
            name = name[0]
            # print(name,r[1],r[2],r[3])
            print ("{:<25} {:<20} {:<10} {:<3}".format(name,r[1],r[2],r[3]))

        print("Are these the player(s) you want? ")
        print("If yes it will make permanent changes TO ALL OF THEM. Enter 0 or 1:")
        YESNO= ['NO','YES']
        choices2 = {}
        for j in range(len(YESNO)):
            print(j,YESNO[j])
            choices2[j] = YESNO[j]
        index2 = helper.get_choice(choices2.keys())
        if index2 ==1:
            return True
        else:
            print("will not delete any of these players, try again or be more specific.")
            return False

#uses view
def best_players():

    features = ["FoulsDrawn" ,
    "Crosses" ,
    "Interceptions",
    "PKwon",
    "PKConceded",
    "OwnGoals" ,
    "BallsRecovered",
    "AerialsWon" ,
    "AerialsLost ",
    "WonPercentage "] # features to show the user
    choices = {}

    print("What stat do you want to view players by? ")
    for i in range(len(features)):
        print(i,features[i])
        choices[i] = features[i]
    index = helper.get_choice(choices.keys())



    view = '''
    CREATE VIEW players AS
    SELECT * FROM BundesligaPlayers as BP
    UNION ALL
    SELECT * FROM LaLigaPlayers as LL
    UNION ALL
    SELECT * FROM SerieAPlayers
    UNION ALL
    SELECT * FROM PremPlayers
    UNION ALL
    SELECT * FROM Ligue1Players
    '''
    cursor.execute(view)
    print("CREATED VIEW")
    query = "SELECT Player, Squad, " +features[index] + " FROM players ORDER BY " + features[index] + " DESC LIMIT 10"
    print(query)
    cursor.execute(query)
    stats = cursor.fetchall()
    # print(stats)
    print ("{:<25} {:<20} {:<15}".format('Player','Squad',features[index]))

    for s in stats:
        name = str(s).strip("'',()'").split("\\",1)
        name = name[0]
            # print(name,r[1],r[2],r[3])
        print ("{:<25} {:<20} {:<15} ".format(name,s[1],s[2]))



    deleteView = "DROP VIEW players;"
    cursor.execute(deleteView)
# main program

# pre_process("SeriaATable",SeriaATable)
# pre_process("PremTable",premTable)
# pre_process("Ligue1Table",Ligue1Table)
# pre_process("BundesligaTable",BundesligaTable)
# pre_process("LaLigaTable",LaLigaTable)


# pre_process("SerieAPlayers", SeriaANationalities)
# pre_process("PremPlayers",PremNationalities)
# pre_process("Ligue1Players",Ligue1Nationalities)
# pre_process("LaLigaPlayers",LaLigaNationalities)
# pre_process("BundesligaPlayers",BundesligaNationalities)

# pre_process("SERIEAFIXTURES", SeriaAFixtures)
# pre_process("PREMFIXTURES",PremFixtures)
# pre_process("LIGUE1FIXTURES",Ligue1Fixtures)
# pre_process("BUNDESLIGAFIXTURES",BundesligaFixtures)
# pre_process("LALIGAFIXTURES",LaLigaFixtures)

# add_leagues()

# pre_process("PREMMANAGERS",PREMMANAGERS)




start_screen()
while True:
    user_choice = options()
    if user_choice == 1:
        # search_by_artist()
        League_Top6()
    elif user_choice == 2:
        search_by_league()
    elif user_choice == 3:
        dirtiest_player()
    elif user_choice == 4:
        team_csv()
    elif user_choice == 5:
        team_diversity()
    elif user_choice ==6:
        update_age()
    elif user_choice ==7:
        create_player()
    elif user_choice == 8:
        delete_player()
    elif user_choice == 9:
        avg_attendance_league()
    elif user_choice == 10:
        best_players()
    elif user_choice == 11:
        print("Goodbye!")
        break
