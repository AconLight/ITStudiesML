from csv import reader
from os import getcwd, sep

cwd = getcwd()

columnSplitter = "^"


def parse_add_conf(conf, path):
    with open(cwd.split("src" + sep + "main")[0] + "conf" + sep + path, newline='') as csv_file:
        conf_reader = reader(csv_file, delimiter=' ', quotechar='|')
        for row in conf_reader:
            columns = row[1].split(columnSplitter)
            if len(columns) < 2:
                conf.update({row[0]: row[1]})
            else:
                conf.update({row[0]: columns})
    return conf
