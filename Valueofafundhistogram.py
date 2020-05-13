# -*- coding: utf-8 -*
"""
Created on Wed Feb 12 16:55:39 2020

@author: Drewb
"""

import numpy as np #imports the numeric Python module/package
import matplotlib.pyplot as plt #imports plotting module
listOfOutcomes = [] #creates an empty list of outcomes
for i in range(100000): #for each simulation/trial
    currentValue = 50000 #start with $50,000 investment
    for year in range(30): #for each of the next 30 years
        growth = np.random.normal(0.07,0.05) #simulate a random growth rate
        currentValue *= (1+growth) #apply the growth rate to the value of the investment
    finalValue = currentValue #final value of the fund for this trial, after 30 years have completed.
    listOfOutcomes.append(finalValue) #add the value of the fund at the end of the simulation to our list of outcomes..
    
	
listOfOutcomes.sort() #sort the outcomes from least to greatest
print('Lowest value outcome: ',listOfOutcomes[0]) #prints out the first (and thus least) value of the list of outcomes
print('Max value outcome: ',listOfOutcomes[-1]) #prints out the last value of the list of outcomes
print('10th percentile outcome: ',listOfOutcomes[9999]) #prints out the 10,000th outcome (10th percentile)
print('70th percentile outcome: ',listOfOutcomes[69999]) #prints out the 70,000th outcome (70th percentile)
print('90th percentile outcome: ',listOfOutcomes[89999]) #prints out the 90,000th outcome (90th percentile)
#can also use the Pandas library with .describe() to gain a quick look at stats surrounding the dataset/percentiles

medianOutcome = np.median(listOfOutcomes) #median outcome
meanOutcome = np.mean(listOfOutcomes) #mean outcome

print('\nThe median outcome is: ', medianOutcome)
print('\nThe mean outcome is: ', meanOutcome)

if (medianOutcome > meanOutcome):
	print('\nMedian outcome is greater than mean.')
else:
	print('\nMean outcome is greater than median.')

plt.style.use('ggplot') #grid stylizer
plt.hist(listOfOutcomes, bins = 30)
plt.title('Fund Growth Over Time')
plt.xlabel('Fund Value')
plt.ylabel('Frequency')
plt.show()

