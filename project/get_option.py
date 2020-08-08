import subprocess
import datetime
import json


USER = ['nobu', 'chikako', 'yota']

def _get_name():
    who = input("who's data do you want?? >>>")
    who = who.upper().lower()
    if who not in USER:
        raise ValueError(f"we don't have {who}'s data")
    return who


def _get_year():
    year = input('what year data do you want?? >>>')
    if not year.isdecimal():
        raise ValueError('You need enter int64.')
    return year


def _token_parse(command_response):
    print(command_response)


def _get_client_info(client_id, client_secret):
    command = ['python-fitbit/gather_keys_oauth2.py', client_id, client_secret]
    command_response = subprocess.check_output(command)
    access_token, refresh_token = token_parse(command_response)
    return access_token, refresh_token


def token_parse(command_response):
    command_response = str(command_response)
    command_response = command_response.split('access_token =')[1]
    access_token = command_response.split('\\nexpires_in')[0].replace(' ', '')
    refresh_token = command_response.split('refresh_token =')[1]
    refresh_token = refresh_token.split('\\nscope')[0].replace(' ', '')
    return access_token, refresh_token


def to_json(name, year, client_info):
    option = {'Name': name, 'Year': year, 'Client_Info': client_info}
    json_file = (f'./config/option_data.json')
    with open(json_file, 'w') as f:
        json.dump(option, f, indent=4)


def read_json():
    json_file = open('./config/option_data.json', 'r')
    json_object = json.load(json_file)
    print(json_object)


def main():
    print('setting option')
    reuse = input('do you want reuse before info(user, year, client_id, client_secret)?? \n Please enter yes or no>>> ').upper().lower()
    if reuse == 'yes':
        # name, year, client_info
        before_info = read_json()
    else:
        name = _get_name()
        year = _get_year()
        client_id = input("input CLIENT_ID >>> ")
        client_secret = input("input CLIENT_SECRET >>> ")
        access_token, refresh_token = _get_client_info(client_id, client_secret)
        client_info = {'client_id':client_id, 'client_secret':client_secret, 'access_token': access_token, 'refresh_token':refresh_token}
        to_json(name, year, client_info)


if __name__ == '__main__':
    main()