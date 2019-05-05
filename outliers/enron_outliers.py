#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL", 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

bonuses_5_mil = filter(lambda member: (member["bonus"] > 5000000) & (member["bonus"] != "NaN"), data_dict.values())
guys = filter(lambda member: (member["salary"] > 1000000) & (member["salary"] != "NaN"), bonuses_5_mil)

feature = "salary"
feature_data = []
for member in data_dict.values():
    feature_data.append(member[feature])
feature_data = filter(lambda member: member != "NaN", feature_data)
print("max", feature, ":", max(feature_data))
print("min", feature, ":", min(feature_data))