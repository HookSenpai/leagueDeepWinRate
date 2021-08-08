from riotwatcher import LolWatcher, ApiError
from champlist import *
import pandas as pd

# golbal variables
api_key = 'RGAPI-fc9bfe05-e03c-433a-9dc3-1a074149a5ec'
watcher = LolWatcher(api_key)
my_region = 'na1'
my_name = 'whitelexp'

apiprint = watcher.champion.rotations(my_region)
freeChampIdList = apiprint['freeChampionIds']

# playerIdResponse = watcher.summoner.by_name(my_region, my_name)
# playerId = playerIdResponse['id']
# # print(playerIdResponse)

# masteryCheck = watcher.champion_mastery.by_summoner_by_champion(my_region, playerId, 107)
# # print(masteryCheck)
# masteryLevel = masteryCheck['championLevel']
# print(masteryLevel)

for championId in freeChampIdList:
    championName = watcher.champion.rotations(my_region)
    name = nameById(championId)
    print(name, championId)

# Scrape summoner names and find match history
# compare against lane opponent
    