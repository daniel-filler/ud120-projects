#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print("number of persons:", len(enron_data))
print("number of features:", len(enron_data["SKILLING JEFFREY K"]))
number_of_pois = 0
for person in enron_data:
    if enron_data[person]["poi"] == 1:
        number_of_pois += 1
print("number of pois:", number_of_pois)
print("total stocks of James Prentice:", enron_data["PRENTICE JAMES"]["total_stock_value"])
print("email messages from Wesley Colwell to persons of interest:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print("value of stock options exercised by Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

print("total_payments of LAY KENNETH L:", enron_data["LAY KENNETH L"]["total_payments"])
print("total_payments of SKILLING JEFFREY K:", enron_data["SKILLING JEFFREY K"]["total_payments"])
print("total_payments of FASTOW ANDREW S:", enron_data["FASTOW ANDREW S"]["total_payments"])

people_with_salary = 0
people_with_email = 0
for person in enron_data:
    if enron_data[person]["salary"] != "NaN":
        people_with_salary += 1
    if enron_data[person]["email_address"] != "NaN":
        people_with_email += 1
print("people with salary:", people_with_salary)
print("people with email:", people_with_email)
"""
for feature in enron_data["PRENTICE JAMES"]:
    print(feature, enron_data["PRENTICE JAMES"][feature])
"""