# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:27:34 2023

@author: rajab
"""
"""In this Python coding, the Pandas and Matplotlib 
libraries are used to visualize Diabetics data stored in a excel file."""
# Import the necessary modules
import matplotlib.pyplot as plt
import pandas as pd
 
def plot_Diabetics(excel_file, save_file): 
# Initialize the lists for X and Y
    dp_diabetics = pd.read_excel(excel_file)
    print(dp_diabetics)
#this is to create Data Frame 
    df = pd.DataFrame(dp_diabetics, columns=["PDU code","PDU name", 
                                         "% with HbA1c<58mmol/mol (7.5%)", "Mean HbA1c (%)"])
    print(df)
# Impute local variables X and Y
    X = list(df["PDU code"].iloc[:10])  
    Y = list(df["% with HbA1c<58mmol/mol (7.5%)"].iloc[:10])
    labels = df["PDU code"].iloc[0:10]
# Bar Plot
    plt.figure(figsize=(18,8))
    color = ('lightblue', 'blue', 'purple', 'red', 'black','yellow', 'brown', 'purple', 'red', 'green')  
# Plot the data using bar() method
    plt.bar(X, Y, color=color,label=labels)
    plt.title("Patients Diabetics analysis done by the hospital")
    plt.xlabel("Hospital code")
    plt.ylabel(" Patients Diabetics level in % ")
    plt.savefig(save_file)
# Show the plot
    plt.show()
#all the function with the excel file and desirable file name to save te png 
plot_Diabetics('Diabetics.xlsx', 'Patients Diabetics analysis done by the hospital.png')