from csv import reader
from os import getcwd, sep

cwd = getcwd()

columnSplitter = "^"

def parseAddConf(conf, path):
    with open(cwd.split("src" + sep + "main")[0] + "conf" + sep + path, newline='') as csvfile:
        confReader = reader(csvfile, delimiter=' ', quotechar='|')
        for row in confReader:
            columns = row[1].split(columnSplitter)
            if len(columns) < 2:
                conf.update({row[0]: row[1]})
            else:
                conf.update({row[0]: columns})
    return conf
