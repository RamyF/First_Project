class Player:
    def __init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age):
        self._firstName = firstName
        self._lastName = lastName
        self._jerseyNum = jerseyNum
        self._height = height
        self._draftYear = draftYear
        self._weight = weight
        self._college = college
        self._points = points
        self._assists = assists
        self._ftpct = ftpct
        self._twoptpct = twoptpct
        self._threeptpct = threeptpct
        self._per = per
        self._offRating = offRating
        self._defRating = defRating
        self._age = age
    # getters 
    def getFirstName(self):
        return self._firstName
    def getLastName(self):
        return self._lastName
    def getJerseyNum(self):
        return self._jerseyNum
    def getHeight(self):
        return self._height
    def getDraftYear(self):
        return self._draftYear
    def getWeight(self):
        return self._weight
    def getCollege(self):
        return self._college
    def getPoints(self):
        return self._points
    def getAssists(self):
        return self._assists
    def getFTPct(self):
        return self._ftpct
    def getTwoPtPct(self):
        return self._twoptpct
    def getThreePtPct(self):
        return self._threeptpct
    def getPER(self):
        return self._per
    def getOffRating(self):
        return self._offRating
    def getDefRating(self):
        return self._defRating
    def getAge(self):
        return self._age
    def getFullName(self):
        return str(self._firstName + ' ' + self._lastName)
    # setters 
    def setFirstName(self, newFirst):
        self._firstName = newFirst
    def setLastName(self, newLast):
        self._lastName = newLast
    def setJerseyNum(self, newNum):
        self._jerseyNum = newNum
    def setHeight(self, newHeight):
        self._height = newHeight
    def setDraftYear(self, newDraftYear):
        self._draftYear = newDraftYear
    def setWeight(self, newWeight):
        self._weight = newWeight
    def setCollege(self, newCollege):
        self._college = newCollege
    def setPoints(self, newPoints):
        self._points = newPoints
    def setAssists(self, newAssists):
        self._assists = newAssists
    def setFTPct(self, newftpct):
        self._ftpct = newftpct
    def setTwoPtPct(self, twoptpct):
        self._twoptpct = twoptpct
    def setThreePtPct(self, newthreeptpct):
        self._threeptpct = newthreeptpct
    def setPER(self, newPER):
        self._per = newPER
    def setOffRating(self, newOffRating):
        self._offRating = newOffRating
    def setDefRating(self, newDefRating):
        self._defRating = newDefRating
    def setAge(self, newAge):
        self._age = newAge
class Guard(Player):
    def __init__ (self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age, steals, turnovers):
        Player.__init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age)
        self._steals = steals
        self._turnovers = turnovers
    # getters 
    def getSteals(self):
        return self._steals
    def getTurnovers(self):
        return self._turnovers
    # setters
    def setSteals(self, newSteals):
        self._steals = newSteals
    def setTurnovers(self, newTurnovers):
        self._turnoverPct = newTurnovers
class ActiveGuard(Guard):
    def __init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age, steals, turnovers, yearsExp, team):
        Guard.__init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age, steals, turnovers)
        self._yearsExp = yearsExp
        self._team = team

    # getters
    def getYearsEXP(self):
        return self._yearsExp
    def getTeam(self):
        return self._team
    # setter 
    def setYearsEXP(self, newYearsEXP):
        self._yearsExp = newYearsEXP
    def setTeam(self, newTeam):
        self._team = newTeam
class HOFGuard(Guard):
    def __init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age, steals, turnovers, yearsExp, yearRetired):
        Guard.__init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age, steals, turnovers)
        self._yearsExp = yearsExp
        self._yearRetired = yearRetired

    # getters
    def getYearsEXP(self):
        return self._yearsExp
    def getYearRetired(self):
        return self._yearRetired
    # setters
    def setYearsEXP(self, newYearsEXP):
        self._yearsExp = newYearsEXP
    def setYearRetired(self, newRetireYear):
        self._yearRetired = newRetireYear
class Forward(Player):
    def __init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age, steals, turnovers, blocks):
        Player.__init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age)
        self._steals = steals
        self._turnovers = turnovers
        self._blocks = blocks
        

    # getters
    def getSteals(self):
        return self._steals
    def getTurnovers(self):
        return self._turnovers
    def getBlocks(self):
        return self._blocks

    # setter
    def setSteals(self, newSteals):
        self._steals = newSteals
    def setTurnovers(self, newTurnovers):
        self._turnoverPct = newTurnovers 
    def setBlocks(self, newBlocks):
        self._blocks = newBlocks  
class ActiveForward(Forward):
    def __init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, rebounds, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age, steals, turnovers, blocks, team, YearsEXP):
        Forward.__init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age, steals, turnovers, blocks)
        self._yearsEXP = YearsEXP
        self._team = team
        self._rebounds = rebounds
    # getter
    def getYearsEXP(self):
        return self._yearsEXP
    def getTeam(self):
        return self._team
    def getRebounds(self):
        return self._rebounds
    # setter 
    def setYearsEXP(self, newYearsEXP):
        self._yearsEXP = newYearsEXP
    def setTeam(self, newTeam):
        self._team = newTeam
    def setRebounds(self, newRebounds):
        self._rebounds = newRebounds
class HOFFoward(Forward):
    def __init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, rebounds, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age, steals, turnovers, blocks, YearsEXP, yearRetired):
        Forward.__init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age, steals, turnovers, blocks)
        self._yearRetired = yearRetired
        self._yearsEXP = YearsEXP
        self._rebounds = rebounds

    # getter
    def getYearRetired(self):
        return self._yearRetired
    def getYearsEXP(self):
        return self._yearsEXP
    def getRebounds(self):
        return self._rebounds

    # setter
    def setYearRetired(self, newRetireYear):
        self._yearRetired = newRetireYear
    def setYearsEXP(self, newYearsEXP):
        self._yearsEXP = newYearsEXP
    def setRebounds(self, newRebounds):
        self._rebounds = newRebounds
class Center(Player):
    def __init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age, blocks, offRebounds, defRebounds):
        Player.__init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age)
        self._blocks = blocks
        self._defRebounds = defRebounds
        self._offRebounds = offRebounds
    # getters
    def getBlocks(self):
        return self._blocks
    def getDefRebounds(self):
        return self._defRebounds
    def getOffRebounds(self):
        return self._offRebounds
    # setters
    def setBlocks(self, newBlocks):
        self._blocks = blocks
    def setDefRebounds(self, newDefRebounds):
        self._defRebounds = newDefRebounds
    def setOffRebounds(self, newOffRebounds):
        self._offRebounds = newOffRebounds
class ActiveCenter(Center):
    def __init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age, blocks, offRebounds, defRebounds, yearsEXP, team):
        Center.__init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age, blocks, offRebounds, defRebounds)
        self._yearsEXP = yearsEXP
        self._team = team

    # getter
    def getYearsEXP(self):
        return self._yearsEXP
    def getTeam(self):
        return self._team
    # setter 
    def setYearsEXP(self, newYearsEXP):
        self._yearsEXP = newYearsEXP
    def setTeam(self, newTeam):
        self._team = newTeam
class HOFCenter(Center):
    def __init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age, blocks, offRebounds, defRebounds, yearsEXP, yearRetired):
        Center.__init__(self, firstName, lastName, jerseyNum, height, draftYear, weight, college, points, assists, ftpct, twoptpct, threeptpct, per, offRating, defRating, age, blocks, offRebounds, defRebounds)
        self._yearRetired = yearRetired
        self._yearsEXP = yearsEXP

    # getter
    def getYearRetired(self):
        return self._yearRetired
    def getYearsEXP(self):
        return self._yearsEXP
    # setter
    def setYearRetired(self, newYearRetired):
        self._yearRetired = yearRetired
    def setYearsEXP(self, newYearsEXP):
        self._yearsEXP = newYearsEXP


















