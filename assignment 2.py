# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 23:42:24 2023

@author: rajab
"""
"""In this Python script, the Pandas and Matplotlib 
libraries are used to visualize office data stored in a CSV file. 
The datas that are include information about the usage period, 
the number of files held, and the number of documents held."""

import pandas as pd
import matplotlib.pyplot as plt

def plot_office_data(csv_file,save_file):    
# Read the data from the CSV file
    data = pd.read_csv(csv_file)

# Extract the columns
    x = data['UsagePeriod'][:35]
    y1 = data['NumberOfFilesHeld'][:35]
    y2 = data['NumberOfDocumentsHeld'][:35]

# The program creats te line plot by using plt.plot  with x as the x-axis and y1 and y2 as the two y-axes
    plt.plot(x, y1, label='Number Of Files Held')
    plt.plot(x, y2, label='Number Of Documents Held')

#this use to Customize the plot
    plt.xlabel('UsagePeriod')
    plt.ylabel('Numbers')
    plt.title('Total files held in the office over years')
    plt.legend()
# This plot is use to save the plot in png form with given file name     
    plt.savefig(save_file)
# Display the plot
    plt.show() 
plot_office_data('office_data.csv', 'Total files held in the office over years.png')