"""In this Python script,We use the Pandas and  also Matplotlib 
 to visualize GDP data stored in a excel file."""
import matplotlib.pyplot as plt
import pandas as pd
 
def plot_economic_distribution(excel_file, save_file):
    # Read data from the Excel file
    GDP = pd.read_excel(excel_file)

 
    df = pd.DataFrame(GDP[:10],columns=["Country",
                           "E1: Economy",
                           "Total no. of patients ex- cluded from HbA1c out- come analy- sis*"])
    print(df)

    plt.figure(figsize=(30,15))

    plt.pie(df["E1: Economy"], labels=df["Country"], startangle=45, shadow=True, autopct='%1.1f%%')
 
# Plot the data using bar() method
#plt.bar(X, Y)
    plt.title("Economic distribution in different countries")
    plt.legend()
    plt.savefig(save_file)
# Show the plot
    plt.show()
# Call the function with your Excel file and desired save file name
plot_economic_distribution('GDP.xlsx', 'Economic distribution in different countries')   
