import csv
import os

cwd = os.getcwd()


def parseAddConf(conf, path):
    with open(cwd.split("src/main")[0] + "conf/" + path, newline='') as csvfile:
        confReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in confReader:
            conf.update({row[0]: row[1]})
    return conf
