import os
import json
import fitbit
import datetime
import pandas as pd
import numpy as np
import sys

class Personal_data:
    def __init__(self, name, year, client_id, client_secret, access_token, refresh_token):
        self.name = name
        self.year = year
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.split_date = datetime.date.today()
        self.authd_client = fitbit.Fitbit(self.client_id, self.client_secret, oauth2=True,
                                          access_token=self.access_token, refresh_token=self.refresh_token)

    def main(self):
        print('Process Success.')

    def specify(self):
        try:
            start_year = int(input('please enter year you want to get: '))
        except:
            raise ValueError('Please enter normally')
        try:
            start_month = int(input('please enter month you want to get: '))
        except:
            raise ValueError('Please enter normally')
        try:
            start_day = int(input('please enter day you want to get: '))
        except:
            raise ValueError('Please enter normally')

        self.start = datetime.date(start_year, start_month, start_day)
        term = int(str(self.split_date - self.start).split(' ')[0])
        date_list = np.array([self.start + datetime.timedelta(days=i) for i in range(term+1)])
        total_df = pd.DataFrame()
        for date in date_list:
            print(date)
            data_sec = self.authd_client.intraday_time_series('activities/heart', base_date=date,
                                                          detail_level='1sec')  # '1sec', '1min', or '15min'
            heart_sec = data_sec["activities-heart-intraday"]["dataset"]
            heart_df = pd.DataFrame.from_dict(heart_sec)
            heart_df.index = pd.to_datetime([str(date) + " " + t for t in heart_df.time])
            total_df = pd.concat([total_df, heart_df], axis=0)
            heart_df.to_csv(f'./project/project_{self.name}/data/original/{date}.csv')
        total_df.to_csv(f'./project/project_{self.name}/data/original_long_term/{self.start}_to_{self.split_date}.csv')



    def day(self):
        today = str(datetime.date.today())
        try:
            data_sec = self.authd_client.intraday_time_series('activities/heart', base_date=today,
                                                          detail_level='1sec')  # '1sec', '1min', or '15min'
            heart_sec = data_sec["activities-heart-intraday"]["dataset"]
            heart_df = pd.DataFrame.from_dict(heart_sec)
            heart_df.index = pd.to_datetime([today + " " + t for t in heart_df.time])
            heart_df.to_csv(f'./project/project_{self.name}/data/original/{today}.csv')
        except AttributeError:
            print('Please sync fitbit')


def read_json():
    json_file = open('./project/config/option_data.json', 'r')
    json_object = json.load(json_file)
    name = json_object['Name']
    year = json_object['Year']
    Client_Info = json_object['Client_Info']
    client_id = Client_Info['client_id']
    client_secret = Client_Info['client_secret']
    access_token = Client_Info['access_token']
    refresh_token = Client_Info['refresh_token']
    return name, year, client_id, client_secret, access_token, refresh_token

def main():
    name, year, client_id, client_secret, access_token, refresh_token = read_json()
    Person = Personal_data(name, year, client_id, client_secret, access_token, refresh_token)
    # Person = Personal_data(read_json())
    target = input('What data do you want to get?\nIs it for one day? Or do you want to get from the specified data to today[specify]? >>> ').upper().lower()
    if target == 'specify':
        Person.specify()
    elif target == 'day':
        Person.day()
    else:
        raise ValueError(f'{target} is input that we do not expect')


    Person.main()

if __name__ == '__main__':
    main()