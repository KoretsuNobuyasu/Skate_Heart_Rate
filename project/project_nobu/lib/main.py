import fitbit
import pandas as pd
import numpy as np
import os
import sys
import datetime

import Get_January_HeartRate
import Get_February_HeartRate
import Get_March_HeartRate
import Get_April_HeartRate
import Get_May_HeartRate
import Get_June_HeartRate
import Get_July_HeartRate
import Get_August_HeartRate
import Get_September_HeartRate
import Get_October_HeartRate
import Get_November_HeartRate
import Get_December_HeartRate
import all_join

token_etc = './token_etc.txt'

def main(argv):
    if (len(argv) != 0):
        for arg in argv:        
            if(arg == 'help'):
                os.system('open -n -a "Google Chrome" https://dev.fitbit.com/apps/details/22DFZH ')
                help = '''
                Januaryを入力すれば1月の心拍数が取得できます
                Februaryを入力すれば2月の心拍数が取得できます
                Marchを入力すれば3月の心拍数が取得できます
                Aprilを入力すれば4月の心拍数が取得できます
                Mayを入力すれば5月の心拍数が取得できます
                Juneを入力すれば6月の心拍数が取得できます
                Julyを入力すれば7月の心拍数が取得できます
                Augustを入力すれば8月の心拍数が取得できます
                Septemberを入力すれば9月の心拍数が取得できます
                Octoberを入力すれば10月の心拍数が取得できます
                Novemberを入力すれば11月の心拍数が取得できます
                Decemberを入力すれば12月の心拍数が取得できます
                InitializeでCLIENT_IDなどの情報を入手後、心拍数を取得してください
                '''
                print(help)
            elif(arg == 'Initialize'):
                #os.system('open -n -a "Google Chrome" https://dev.fitbit.com/apps/details/22DFZH ')
                CLIENT_ID = input("CLIENT_IDを入力してください")
                CLIENT_SECRET = input("CLIENT_SECRETを入力してください")
                ACCESS_TOKEN = input("ACCESS_TOKENを入力してください")
                REFRESH_TOKEN = input("REFRESH_TOKENを入力してください")

                with open(token_etc, mode='w') as f:
                    f.write(CLIENT_ID)
                    f.write("\n")
                    f.write(CLIENT_SECRET)
                    f.write("\n")
                    f.write(ACCESS_TOKEN)
                    f.write("\n")
                    f.write(REFRESH_TOKEN)
                    
            else:
                os.system('open -n -a "Google Chrome" https://dev.fitbit.com/apps/details/22DFZH ')
                token_list = list()
                with open(token_etc) as f:
                    for s_line in f:
                        token_list.append(s_line)
                print(token_list)
                CLIENT_ID = token_list[0].strip()
                CLIENT_SECRET = token_list[1].strip()
                ACCESS_TOKEN = token_list[2].strip()
                REFRESH_TOKEN = token_list[3].strip()
                print(CLIENT_ID)
                print(CLIENT_SECRET)
                print(ACCESS_TOKEN)
                print(REFRESH_TOKEN)
                

                
                authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True,
                             access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)
                
                if(arg == 'January'):
                    print('January')
                    Get_January_HeartRate.Get_January(authd_client)
                elif(arg == 'February'):
                    print('February')
                    Get_February_HeartRate.Get_February(authd_client)
                elif(arg == 'March'):
                    print('March')
                    Get_March_HeartRate.Get_March(authd_client)
                elif(arg == 'April'):
                    print('April')
                    Get_April_HeartRate.Get_April(authd_client)
                elif(arg == 'May'):
                    print('May')
                    Get_May_HeartRate.Get_May(authd_client)
                elif(arg == 'June'):
                    print('June')
                    Get_June_HeartRate.Get_June(authd_client)
                elif(arg == 'July'):
                    print('July')
                    Get_July_HeartRate.Get_July(authd_client)
                elif(arg == 'August'):
                    print('January')
                    Get_August_HeartRate.Get_August(authd_client)
                elif(arg == 'September'):
                    print('September')
                    Get_September_HeartRate.Get_September(authd_client)
                elif(arg == 'October'):
                    print('October')
                    Get_October_HeartRate.Get_October(authd_client)
                elif(arg == 'November'):
                    print('November')
                    Get_November_HeartRate.Get_November(authd_client)
                elif(arg == 'December'):
                    print('December')
                    Get_December_HeartRate.Get_December(authd_client)
                
                
    else:
        print("使い方がわからない場合はhelpを入力してください")

    

if __name__ == "__main__":
    main(sys.argv[1:2])

