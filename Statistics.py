# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 15:12:07 2018

@author: ananth.ranganatha
"""

#Read the data set
import numpy as np
import pandas as pd
readfile = pd.read_csv('Laliga.csv',skiprows=1)
football = pd.DataFrame(readfile)
print(football)

# Replace dashes with 0
football=football.replace('-','0')

#Print all the teams which have started playing between 1930-1980
for i in range(len(football['Debut'])):
    temp=football['Debut'][i]
    temp1="-"
    fir=""
    sec=""
    chk= 1930
    fir1=0
    sec1=0
    football['my_column_trim']=""
    if temp1 in temp:
        dum=temp.index(temp1)
        fir=temp[0:dum]
        sec=temp[0:2]+temp[dum+1:]       
        fir1= int(fir)
        sec1 = int(sec)
        
        if((fir1>=1930 and fir1<=1980) or (sec1>=1930 and sec1<=1980)):
            print(football['Team'][i])
        
    else:
        #print(temp)
        if((fir1>=1930 and fir1<=1980) or (sec1>=1930 and sec1<=1980)):
            print(football['Team'][i])     


#1.Print the list of teams which came Top 5 in terms of points
lst=[]
for i in range(len(football['Points'])):
    
    temp= int(football['Points'][i])
    lst.append(temp )

lst.sort(reverse=True)

for i in range(5):
    temp1=lst[i]
    for j in range(len(football['Points'])):
        
        if(int(football['Points'][j]) == temp1):
            print(football['Team'][j]) 
            

#2.Print the list of teams which came Top 5 in terms of points
points_int_numbers = []
for i in range(0, len(football['Team']) ):
    points_int_numbers_temp = int(football['Points'][i])
    points_int_numbers.append(points_int_numbers_temp)
football['Points temp values']= points_int_numbers
print(football.nlargest(5, 'Points temp values'))


# Write a function with name “Goal_diff_count” which should return all the teams with their Goal Differences. Using the same function, find the team which has maximum and minimum goal difference
def Goal_diff_count():
    goal_diff = []
    for i in range(0, len(football['Team'])):
        goal_diff_temp = int(football['GoalsFor'][i]) - int(football['GoalsAgainst'][i])
        goal_diff.append(goal_diff_temp)
    football['Goal Differences']= goal_diff
    #Print the goal difference
    print(football)
    #Print the team name with largest goal difference
    print(football.nlargest(1, 'Goal Differences'))
    #Print the team name with smallest goal difference
    print(football.nsmallest(1, 'Goal Differences'))
Goal_diff_count()


#Create a new column with name “Winning Percent” and append it to the data set 
percentage_winnning = []
for i in range(0, len(football['Team']) ):
    percentage_winnning_temp = 0
    if(int(football['GamesPlayed'][i]) != 0 ):
        percentage_winnning_temp = ( int(football['GamesWon'][i]) / int(football['GamesPlayed'][i]) )*100
    percentage_winnning.append(percentage_winnning_temp)
football['Winning Percent']= percentage_winnning
print(football)

#Print the top 5 teams which has the highest Winning percentage
print(football.nlargest(5, 'Winning Percent'))


#Group teams based on their “Best position”
print(football.groupby(['BestPosition', 'Team'])['Team'].count())


# Group teams based on their “Best position” and print the sum of their points for all positions (6 points)
#Eg: Best Position                Points

#        1                              25000

#        2                              7000 
print(football.groupby('BestPosition')['Points temp values'].sum())