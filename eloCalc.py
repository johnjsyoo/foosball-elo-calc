#! /usr/local/bin/python

import pandas as pd

data = pd.read_excel('EloRanking.xlsx')
data = data.drop('Date', axis=1)

eloDict = {}

# Returns the elo rating for an existing player and sets a default rating for new players
def getEloRating(playerName):
    if playerName not in eloDict:
        eloDict[playerName] = 1000
        return eloDict[playerName]
    else:
        return eloDict[playerName]

# Returns the expected win outcome
def getExpectation(rating_1, rating_2):
    calc = (1.0 / (1.0 + pow(10, ((rating_2 - rating_1) / 1000))));
    return calc;

# Modifies the elo rating of a player based on the outcome of a game
def modifyRating(oldRating, expected, result, kFactor):
    newRating = (oldRating + kFactor * (result - expected));
    return newRating;

# Iterates through the Excel sheet and updates all Elo ratings
for players in data.itertuples():
    winnersAvgRtg = (getEloRating(players[1]) + getEloRating(players[2]))/2
    losersAvgRtg = (getEloRating(players[3]) + getEloRating(players[4]))/2

    winnersExpectation = getExpectation(winnersAvgRtg, losersAvgRtg)
    losersExpectation = getExpectation(losersAvgRtg, winnersAvgRtg)

    for individual in players[1:3]:
        eloDict[individual] = modifyRating(getEloRating(individual), winnersExpectation, 1, 50)

    for individual in players[3:5]:
        eloDict[individual] = modifyRating(getEloRating(individual), losersExpectation, 0, 50)

print "\n"
print("\n".join("{}: \t{}".format(k, v).expandtabs(25) for k, v in sorted(eloDict.items(), key=lambda x:x[1], reverse=True)))
print "\n"




