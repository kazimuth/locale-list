import os
import csv


for entry in os.listdir('data'):
    found = False
    with open(f'data/{entry}/locales.csv') as f:
        for line in csv.reader(f):
            if line[0] == entry:
                print(f"""    ("{line[0]}", "{line[1]}"),""")
                found = True
    assert found

