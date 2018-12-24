# Created by Ramy Farah
# Final Project 
import Players
import Validation
import sys
def main():
    #bring data from files and store in following lists
    activeGuardAttributes = []
    activeGuards = []
    hofGuardAttributes = []
    hofGuards = []
    activeFowardAttributes = []
    activeFowards = []
    hofFowardAttributes = []
    hofFowards = []
    activeCenterAttributes = []
    activeCenters = []
    hofCenterAttributes = []
    hofCenters = []
     #import active guard txt file and instantiate active guards
    try:
        with open('ActiveGuard.txt', 'r') as infile:
            attributes = infile.readlines()
            for line in attributes:
                line = line.rstrip() # strip spacing 
                activeguardattributes = line.split() # split will create a list with each word as an elemen
                activeguard = createActiveGuard(activeguardattributes)
                activeGuards.append(activeguard)
    except IOError:
       print('an error has occurred reading the file.')
       print('the program will now exit.')
       sys.exit()
    except:
       print('an error has occurred.')
       print('the program will now exit.')
       sys.exit()
      #import active foward txt file and instantiate active foward
    try:
        with open('ActiveFoward.txt', 'r') as infile:
            for line in infile:
                line = line.rstrip() # strip spacing 
                activeFowardAttributes = line.split() # split will create a list with each word as an element
                activefoward = CreateActiveFoward(activeFowardAttributes)
                activeFowards.append(activefoward)
            print(activeFowards)
    except IOError:
       print('an error has occurred reading the file.')
       print('the program will now exit.')
       sys.exit()
    except:
       print('an error has occurred.')
       print('the program will now exit.')
       sys.exit()
         #import active center txt file and instantiate active center
    try:
        with open('ActiveCenter.txt', 'r') as infile:
            for line in infile:
                line = line.rstrip() # strip spacing 
                activeCenterAttributes = line.split() # split will create a list with each word as an element
                activecenter = CreateActiveCenter(activeCenterAttributes)
                activeCenters.append(activecenter)
    except IOError:
       print('an error has occurred reading the file.')
       print('the program will now exit.')
       sys.exit()
    except:
       print('an error has occurred.')
       print('the program will now exit.')
       sys.exit()
    # menu/header
    print('Ramy\'s NBA Stats Program')
    print('-------------------------\n\n')
    while True:
        print('Main Menu:')
        print('\n1. Player Search')
        print('2. Edit Player')
        print('3. Leaderboards')
        print('4. Exit Program')
        choice = input('Enter your selection: ')
        choice = Validation.validateNumber(choice)
        choice = Validation.valNumRange(choice, 1, 5)
        # validate choice (will catch numbers outside of 1-5)
        if choice == 1:
            print()
            playersList = activeGuards + activeCenters #+ activeFowards
            desiredPlayer = findplayer(playersList)
            if isinstance(desiredPlayer, Players.ActiveGuard):
                DisplayActiveGuard(desiredPlayer)
            elif isinstance(desiredPlayer, Players.ActiveForward):
                DisplayActiveForward(desiredPlayer)
            elif isinstance(desiredPlayer, Players.ActiveCenter):
                DisplayActiveCenter(desiredPlayer) 
            #use player inder function then display player function
        elif choice == 2:
            print('not implemented')
        elif choice == 3:
            print('not implemented')
        elif choice == 4:
            print('not implemented')
            # use for loop and append desired state to new list then sort 
        else:
            print('not implemented')

# build findplayer function
def createActiveGuard(attributes):
    firstName = attributes[0]
    lastName = attributes[1]
    jerseyNum = attributes[2]
    height = attributes[3]
    draftYear = attributes[4]
    weight = attributes[5]
    college = attributes[6]
    points = attributes[7]
    assists = attributes[8]
    ftpct = attributes[9]
    twoPtPct = attributes[10]
    threePtPCt = attributes[11]
    per = attributes[12]
    offRating = attributes[13]
    defRating = attributes[14]
    age = attributes[15]
    steals = attributes[16]
    turnovers = attributes[17]
    yearsExp = attributes[18]
    team = attributes[19]
    activeGuard = Players.ActiveGuard(firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoPtPct, threePtPCt, per, offRating, defRating, age, steals, turnovers, yearsExp, team)
    return activeGuard
def CreateActiveFoward(attributes):
    firstName = attributes[0]
    lastName = attributes[1]
    jerseyNum = attributes[2]
    height = attributes[3]
    draftYear = attributes[4]
    weight = attributes[5]
    college = attributes[6]
    points = attributes[7]
    rebounds = attributes[8]
    assists = attributes[9]
    ftpct = attributes[10]
    twoPtPct = attributes[11]
    threePtPCt = attributes[12]
    per = attributes[13]
    offRating = attributes[14]
    defRating = attributes[15]
    age = attributes[16]
    steals = attributes[17]
    turnovers = attributes[18]
    blocks = attributes[19]
    team = attributes[20]
    yearsExp = attributes[21]
    ActiveFoward = Players.ActiveForward(firstName, lastName, jerseyNum, height, draftYear, weight, college, points, rebounds, assists, ftpct, twoPtPct, threePtPCt, per, offRating, defRating, age, steals, turnovers, blocks, team, yearsExp)
    return ActiveFoward 
def CreateActiveCenter(attributes):
    firstName = attributes[0]
    lastName = attributes[1]
    jerseyNum = attributes[2]
    height = attributes[3]
    draftYear = attributes[4]
    weight = attributes[5]
    college = attributes[6]
    points = attributes[7]
    assists = attributes[8]
    ftpct = attributes[9]
    twoPtPct = attributes[10]
    threePtPCt = attributes[11]
    per = attributes[12]
    offRating = attributes[13]
    defRating = attributes[14]
    age = attributes[15]
    blocks = attributes[16]
    offRebounds = attributes[17]
    defRebounds =attributes[18]
    yearsExp = attributes[19]
    team = attributes[20]
    activeCenter = Players.ActiveCenter(firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoPtPct, threePtPCt, per, offRating, defRating, age, blocks, offRebounds, defRebounds, yearsExp, team)
    return activeCenter
def findplayer(playersList):
    counter = 0
    desiredPlayer = input('Enter the full name of the player you would like to find: ')
    while True:
        for player in playersList:
            if str(player.getFullName()) == str(desiredPlayer):
                return(player)
        print('Player not found please check spelling and try again.')
        desiredPlayer = input('Enter the full name of the player you would like to find: ')
        counter += 1
        if counter == 1:
            with open('AddPlayers.txt', 'a') as outfile:
                outfile.write(str(desiredPlayer))
            print(desiredPlayer, 'has been placed in a list of players to add to program. \nThank You.')
            break
def DisplayActiveGuard(player):
    print('Name: ' + player.getFirstName() + ' ' + player.getLastName())
    print('#' + player.getJerseyNum())
    print('Weight: ' + player.getWeight())
    print('Age: ' + player.getAge())
    print('College: ' + player.getCollege())
    print('Drafted: ' + player.getDraftYear())
    print('Experience: ' + player.getYearsEXP())
    print('Team: ' + player.getTeam())
    print('\nSTATS\n' + '----------\n')
    print('PPG: ' + player.getPoints())
    print('Assists: ' + player.getAssists())
    print('Steals: ' + player.getSteals())
    print('Freethrow %: ' + player.getFTPct())
    print('2 Point %: ' + player.getTwoPtPct())
    print('3 Point %: ' + player.getThreePtPct())
    print('\nAdvanced:\n')
    print('PER: ' + player.getPER() + '\tOff. Rating: ' + player.getOffRating() + '\tDef. Rating: ' + player.getDefRating() + '\tTurnover%: ' + player.getTurnovers())
def DisplayHOFGuard(player):
    print('Name: ' + player.getFirstName() + ' ' + player.getLastName())
    print('#' + player.getJerseyNum())
    print('Weight: ' + player.getWeight())
    print('Age: ' + player.getAge())
    print('College: ' + player.getCollege())
    print('Drafted: ' + player.getDraftYear())
    print('Experience: ' + player.getYearsEXP())
    print('Year Retired: ' + player.getYearRetired())
    print('\nSTATS\n' + '----------\n')
    print('PPG: ' + player.getPoints())
    print('Assists: ' + player.getAssists())
    print('Steals: ' + player.getSteals())
    print('Freethrow %: ' + player.getFTPct())
    print('2 Point %: ' + player.getTwoPtPct())
    print('3 Point %: ' + player.getThreePtPct())
    print('\nAdvanced:\n')
    print('PER: ' + player.getPER() + '\tOff. Rating: ' + player.getOffRating() + '\tDef. Rating: ' + player.getDefRating() + '\tTurnovers: ' + player.getTurnovers())
def DisplayActiveForward(player):
    print('Name: ' + player.getFirstName() + ' ' + player.getLastName())
    print('#' + player.getJerseyNum())
    print('Weight: ' + player.getWeight())
    print('Age: ' + player.getAge())
    print('College: ' + player.getCollege())
    print('Drafted: ' + player.getDraftYear())
    print('Experience: ' + player.getYearsEXP())
    print('Team: ' + player.getTeam())
    print('\nSTATS\n' + '----------\n')
    print('PPG: ' + player.getPoints())
    print('Assists: ' + player.getAssists())
    print('Steals: ' + player.getSteals())
    print('Blocks: ' + player.getBlocks())
    print('Freethrow %: ' + player.getFTPct())
    print('2 Point %: ' + player.getTwoPtPct())
    print('3 Point %: ' + player.getThreePtPct())
    print('\nAdvanced:\n')
    print('PER: ' + player.getPER() + '\tOff. Rating: ' + player.getOffRating() + '\tDef. Rating: ' + player.getDefRating() + '\tTurnovers: ' + player.getTurnovers())
def DisplayHOFForward(player):
    print('Name: ' + player.getFirstName() + ' ' + player.getLastName())
    print('#' + player.getJerseyNum())
    print('Weight: ' + player.getWeight())
    print('Age: ' + player.getAge())
    print('College: ' + player.getCollege())
    print('Drafted: ' + player.getDraftYear())
    print('Experience: ' + player.getYearsEXP())
    print('Year Retired: ' + player.getYearRetired())
    print('\nSTATS\n' + '----------\n')
    print('PPG: ' + player.getPoints())
    print('Assists: ' + player.getAssists())
    print('Steals: ' + player.getSteals())
    print('Blocks: ' + player.getBlocks())
    print('Freethrow %: ' + player.getFTPct())
    print('2 Point %: ' + player.getTwoPtPct())
    print('3 Point %: ' + player.getThreePtPct())
    print('\nAdvanced:\n')
    print('PER: ' + player.getPER() + '\tOff. Rating: ' + player.getOffRating() + '\tDef. Rating: ' + player.getDefRating() + '\tTurnovers: ' + player.getTurnovers())
def DisplayActiveCenter(player):
    print('Name: ' + player.getFirstName() + ' ' + player.getLastName())
    print('#' + player.getJerseyNum())
    print('Weight: ' + player.getWeight())
    print('Age: ' + player.getAge())
    print('College: ' + player.getCollege())
    print('Drafted: ' + player.getDraftYear())
    print('Experience: ' + player.getYearsEXP())
    print('Team: ' + player.getTeam())
    print('\nSTATS\n' + '----------\n')
    print('PPG: ' + player.getPoints())
    print('Assists: ' + player.getAssists())
    print('Blocks: ' + player.getBlocks())
    print('Offensive Rebounds: ' + player.getOffRebounds())
    print('Defensive Rebounds: ' + player.getDefRebounds())
    print('Freethrow %: ' + player.getFTPct())
    print('2 Point %: ' + player.getTwoPtPct())
    print('3 Point %: ' + player.getThreePtPct())
    print('\nAdvanced:\n')
    print('PER: ' + player.getPER() + '\tOff. Rating: ' + player.getOffRating() + '\tDef. Rating: ' + player.getDefRating())
def DisplayHOFCenter(player):
    print('Name: ' + player.getFirstName() + ' ' + player.getLastName())
    print('#' + player.getJerseyNum())
    print('Weight: ' + player.getWeight())
    print('Age: ' + player.getAge())
    print('College: ' + player.getCollege())
    print('Drafted: ' + player.getDraftYear())
    print('Experience: ' + player.getYearsEXP())
    print('Year Retired: ' + player.getYearRetired())
    print('\nSTATS\n' + '----------\n')
    print('PPG: ' + player.getPoints())
    print('Assists: ' + player.getAssists())
    print('Blocks: ' + player.getBlocks())
    print('Offensive Rebounds: ' + player.getOffRebounds())
    print('Defensive Rebounds: ' + player.getDefRebounds())
    print('Freethrow %: ' + player.getFTPct())
    print('2 Point %: ' + player.getTwoPtPct())
    print('3 Point %: ' + player.getThreePtPct())
    print('\nAdvanced:\n')
    print('PER: ' + player.getPER() + '\tOff. Rating: ' + player.getOffRating() + '\tDef. Rating: ' + player.getDefRating())
main()
