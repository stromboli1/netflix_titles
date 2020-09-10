'''
    Forfatter: Anders Larsen (andl@eucnord.dk)
    Dette er et undervisningsprojekt i databehandling i Python på real life data.
    Data er hentet fra https://www.kaggle.com/shivamb/netflix-shows
'''

import csv

data = [] #global variabel

'''
    Denne funktion indlæser data fra csv-filen og gemmer det i den globale liste 'data'
    Hvert element i listen er en såkaldt dictionary.
'''
def setup():
    global data
    with open('netflix_titles.csv', newline='', encoding='iso-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader.fieldnames)
        data = list(reader)

'''
    Denne funktion udregner den gennemsnitlige titellængde målt i antal karakterer.
'''
def getAverageTitleLength():
    titlelength = 0
    for row in data: #Gå igennem alle rækker af data.
        title = row.get('title')
        titlelength += len(title) #Adder alle titellænderne
    return titlelength/len(data) #Divider med antallet af datapunkter

'''
    Denne funktion genererer en dictionary af instruktører og tæller hvor mange film/serier
    de er krediteret med på Netflix.
'''
def getDirectorDict():
    directors = dict()
    for row in data:
        name = row.get('director')
        if name in directors: #Tjek om instruktøren er i listen
            directors[name] += 1 #Læg en kreditering til hans navn, hvis han er i listen
        else:
            directors[name] = 1 #Opret instruktørens navn i dictionary.
    return directors

'''
    Denne funktion tager en instruktørdictionary som genereret af getDirectorDict
    som input og returnerer en liste med de samme værdier, blot sorteret efter antallet
    af intruktørkrediteringer.
'''
def getMostPopularDirectors(directorDict):
    dirList = []
    for key, val in directorDict.items():
        dirList.append([val, key])
    return sorted(dirList, reverse=True)

setup()
print(getAverageTitleLength())
