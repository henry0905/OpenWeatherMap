# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 18:47:23 2021

@author: lammi
"""


import datetime
from pprint import pprint 
import json
import os
import matplotlib.pyplot as plt
import numpy as np

# {} type dict
# [] type list


#Define Current Path & Items in Current Working Directory
current_path = os.getcwd()
current_directory = os.listdir()
#Loop Through Items in Current Working Directory
for item in current_directory:
    
    #Find Folder for Global Weather Data
        
    #Find Folder for Output Plots
    if item.lower().find('historical weather data') >= 0:
        
        #Define File Path for Output Plots
        output_file = current_path + '/' + item + '/'
        output_file_exact = current_path + '/' + item + '/selected' + '/'
        output_file_final = current_path + '/' + item + '/final' + '/'
        
        #Find Folder for Output Plots
    elif item.lower().find('images') >= 0:
        
        #Define File Path for Output Plots
        output_plot = current_path + '/' + item + '/'


def ChasseneuilWeather_Final():
    # Open a JSON file
    # with open('ChasseneuilWeather_Final.json') as json_file:
    with open ('ChasseneuilWeather_Final_Update_Need.json') as json_file:
        data = json.load(json_file)
    # pprint(data[0]['dt']) # Type list 1609945200
    # print(datetime.datetime.fromtimestamp(data[0]['dt']).strftime(%h-%d'))
    # 16-06   
    list_dt = []
    list_dt_year = []
    list_temp = []
    list_hum = []
    list_dt_40months = []
    for i in range(len(data)):
        # Days
        # list_dt.append(datetime.datetime.fromtimestamp(data[i]['dt']).strftime('%Hh-%d/%m'))
        # Years
        list_dt.append(datetime.datetime.fromtimestamp(data[i]['dt']).strftime('%Y/%m/%d-%H'))
        list_dt_year.append(datetime.datetime.fromtimestamp(data[i]['dt']).strftime('%Y'))
        list_dt_40months.append(datetime.datetime.fromtimestamp(data[i]['dt']).strftime('%h'))


        list_temp.append(data[i]['temp'])
        list_hum.append(data[i]['humidity'])
    # print(list_dt[0])
    # print(list_dt_year[0])
    # print(list_temp)
    # print(list_dt_40months)
    return data, list_dt, list_temp, list_hum, list_dt_year, list_dt_40months

def forecast():
    # Open a JSON file
    # with open('ChasseneuilWeather_Final.json') as json_file:
    with open ('Compare.json') as json_file:
        data1 = json.load(json_file)
    list_dt1 = []
    list_temp1 = []
    list_hum1 = []
    for i in range(len(data1)):
        list_dt1.append(datetime.datetime.fromtimestamp(data1[i]['dt']).strftime('%Hh-%d/%m'))
        list_temp1.append(data1[i]['temp'])
        list_hum1.append(data1[i]['humidity'])    
        
    with open ('exact_everyhourforecast2021-02-06-00.json') as json_file:
        data2 = json.load(json_file)
    list_dt2 = []
    list_temp2 = []
    list_hum2 = []
    for i in range(len(data2)):
        list_dt2.append(datetime.datetime.fromtimestamp(data2[i]['dt']).strftime('%Hh-%d/%m'))
        list_temp2.append(data2[i]['temp'])
        list_hum2.append(data2[i]['humidity'])
    # print(len(list_dt1))
    # print(list_dt1)
    # print(list_temp1)
    return list_dt1, list_temp1, list_hum1,list_dt2, list_temp2, list_hum2

def hour_line_interval_temp_time_1year(list_dt, list_temp, list_dt_year):
    new_list_dt = []
    new_list_temp = []
    for i,year in enumerate(list_dt_year):
        if year == '1979':
            new_list_dt.append(list_dt[i])
            new_list_temp.append(list_temp[i])
        
    F1, AX1 = plt.subplots()
    AX1.plot(new_list_dt, new_list_temp)
    AX1.grid()
    plt.xticks(np.arange(0,len(new_list_dt),len(new_list_dt)/5), rotation='vertical')
    AX1.set_title('Temperature in 1979')
    AX1.set_xlabel('Time')
    AX1.set_ylabel('Temperature (K)')
    plt.savefig(output_plot + 'Temperature in 1979.png')
    plt.show()
    
def hour_line_interval_temp_time_40years(list_dt, list_temp, list_dt_40months):
    new_list_dt = []
    new_list_temp = []
    for i,month in enumerate(list_dt_40months):
        if month == 'Aug':
            new_list_dt.append(list_dt[i])
            new_list_temp.append(list_temp[i])
        
    F1, AX1 = plt.subplots()
    AX1.plot(new_list_dt, new_list_temp)
    AX1.grid()
    plt.xticks(np.arange(0,len(new_list_dt),len(new_list_dt)/5), rotation='vertical')
    AX1.set_title('The temperature in all January months 1979-2021')
    AX1.set_xlabel('Time')
    AX1.set_ylabel('Temperature (K)')
    plt.savefig(output_plot + 'The temperature in all January months 1979-2021.png')
    plt.show()
    
def hour_scatter_interval_temp_time(list_dt, list_temp):
    #Plot Latitude Data Versus Maximum Temperature Data
    F1, AX1 = plt.subplots()
    AX1.scatter(list_dt, list_temp, facecolor = 'blue', edgecolor = 'black')
    AX1.grid()
    plt.xticks(np.arange(0,len(list_dt),len(list_dt)/6), rotation='vertical')
    AX1.set_title('Temperature vs Time')
    AX1.set_xlabel('Time')
    AX1.set_ylabel('Temperature (K)')
    plt.savefig(output_plot + 'Temperature_vs_Time.png')
    
    plt.show()
    
def hour_scatter_interval_temp_hum(list_hum, list_temp):
    #Plot Latitude Data Versus Maximum Temperature Data
    F1, AX1 = plt.subplots()
    AX1.scatter(list_hum, list_temp, facecolor = 'blue', edgecolor = 'black')
    AX1.grid()
    AX1.set_title('Humidity vs Temperature 01/02/2021-06/02/2021')
    AX1.set_xlabel('Humidity')
    AX1.set_ylabel('Temperature (K)')
    plt.savefig(output_plot + 'Humidity_vs_Time.png')
    
    plt.show()

def hour_line_interval_temp_time(list_dt, list_temp):
    F1, AX1 = plt.subplots()
    AX1.plot(list_dt, list_temp)
    AX1.grid()
    plt.xticks(np.arange(0,len(list_dt),len(list_dt)/5), rotation='vertical')
    AX1.set_title('Temperature vs Time from 01/02/2021-06/02/2021')
    AX1.set_xlabel('Time')
    AX1.set_ylabel('Temperature (K)')
    plt.savefig(output_plot + 'Temperature vs Time_Line Chart.png')
    plt.show()
    
    
def compare_forecast(list_dt1, list_temp1, list_hum1, list_dt2, list_temp2, list_hum2):
    plt.plot(list_dt1, list_temp1, label = "forecast")
    plt.xticks(np.arange(0,len(list_dt1),len(list_dt1)/5), rotation='vertical')

    plt.plot(list_dt1, list_temp2, label = "historical")
    plt.xticks(np.arange(0,len(list_dt1),len(list_dt1)/5), rotation='vertical')

    plt.title('Compare Historical and Forecast Data 06/02/2021-07/02/2021')
    plt.xlabel('Time')
    plt.ylabel('Temperature (K)')
    plt.savefig(output_plot + 'Compare Historical and Forecast Data.png')
    plt.legend()
    plt.show()
    
    
def main():   
    data, list_dt, list_temp, list_hum, list_dt_year, list_dt_40months  = ChasseneuilWeather_Final()
    list_dt1, list_temp1, list_hum1,list_dt2, list_temp2, list_hum2 = forecast()
    # hour_scatter_interval_temp_time(list_dt, list_temp)
    # hour_line_interval_temp_time(list_dt, list_temp)
    # hour_line_interval_temp_time_1year(list_dt, list_temp,list_dt_year)
    # hour_line_interval_temp_time_40years(list_dt, list_temp, list_dt_40months)
    # hour_scatter_interval_temp_hum(list_hum, list_temp)
    compare_forecast(list_dt1, list_temp1, list_hum1, list_dt2, list_temp2, list_hum2)
    
if __name__ == "__main__":
    main()