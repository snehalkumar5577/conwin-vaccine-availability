#!/usr/bin/env python3

# get parameters - pincode , date
# call api
# filter the response by age
# print response

## improvements -
# add scheduler to run the program after every 5 mins
# send email notification on gmail

import requests
import argparse

# get params
parser = argparse.ArgumentParser()
parser.add_argument('pincode')
parser.add_argument('date')
parser.add_argument('age', type=int)
args = parser.parse_args()
pincode = args.pincode
date = args.date
age = args.age
#print(args)

# call api

response = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}")

## filter the response by age
#min_age_limit = response.json()['sessions'][0]['min_age_limit']

sessions = response.json()['sessions']

for session in sessions:
    if age >= session['min_age_limit']:
        print(response.json())
    else:
        print("Not available")



