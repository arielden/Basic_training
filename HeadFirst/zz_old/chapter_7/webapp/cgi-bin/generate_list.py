#! /home/arield/miniconda3/envs/training_env/bin/python

import glob

import athletemodel
import yate

my_path = "/home/arield/Documentos/CODE/Python/Basic_training/HeadFirst/chapter_7/webapp/"

data_files = glob.glob(f"{my_path}data/*.txt")
athletes = athletemodel.put_to_store(data_files)

print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("Select an athlete from the list to work with:"))
for each_athlete in athletes:
    print(yate.radio_button("which_athlete", athletes[each_athlete].name))
print(yate.end_form("Select"))
print(yate.include_footer({"Home": "/index.html"}))
