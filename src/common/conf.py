import csv
import os

cwd = os.getcwd()

columnSplitter = "^"

def parseAddConf(conf, path):
    with open(cwd.split("src/main")[0] + "conf/" + path, newline='') as csvfile:
        confReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in confReader:
            columns = row[1].split(columnSplitter)
            if len(columns) < 2:
                conf.update({row[0]: row[1]})
            else:
                conf.update({row[0]: columns})
    return conf
