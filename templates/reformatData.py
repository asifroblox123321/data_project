import csv
import json
import os

csv_file_path = "life_expectancy.csv"
json_file_path = "life_expectancy.json"

if not os.path.exists(csv_file_path):
    print(f"")
else:
    try:
        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            dictionary = {}
            for row in reader:
                geography = row['Geography']
                year = row['TimePeriod']
                if geography not in dictionary:
                    dictionary[geography] = {}
                if year not in dictionary[geography]:
                    dictionary[geography][year] = {}    
                dictionary[geography][year] = {
                    "Geography": geography, 
                    "GeoType": row['GeoType'],
                    "Number": row['Number'],
                    "Percent That Are Obese": row['Percent That Are Obese']
                }

        if dictionary:
            with open(json_file_path, "w") as json_file:
                json.dump(dictionary, json_file, indent=4)
            print(f"JSON file '{json_file_path}' created successfully with data from multiple years.")
        else:
            print("")

    except Exception as e:
        print("", e)