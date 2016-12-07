#! /usr/bin/env python

import calendar
import datetime
import pickle
import glob, os


classifier_file = "naive_bayes_classifier"

file_path = "data/archiveteam-twitter-stream-2016-06/2016/06/"

def format_date(date):
    date_format = "{year}-{month}-{day}"
    return date_format.format(year = date.year, month = date.month, day = date.day)

def get_date_list(month, year):
    num_days = calendar.monthrange(year, month)[1]
    days = [datetime.date(year, month, day) for day in range(1, num_days + 1)]
    return days

def create_features():
    classifier = None
    #Returns a list of [date, feature, output] 
    with open(classifier_file, 'r') as cf:
        classifier = pickle.load(cf)
    print classifier

    day_list = list()

    for day_dir in os.listdir(file_path):
        day_list.append(day_dir)
        day_dir_path = file_path + day_dir + "/"
        day_dir_list = os.listdir(day_dir_path)
        for day_dir_child in day_dir_list:
            print os.listdir(day_dir_path + day_dir_child)


create_features()
print format_date(get_date_list(6, 2016)[0])
