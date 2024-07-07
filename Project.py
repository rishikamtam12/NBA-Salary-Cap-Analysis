"""
Rishi Kamtam
CS190
CS190 Final Project
Fall 2023
Project.py

This program will analyze the correlation of three team's payroll data and
win percentage data from 2001-2022 and look at the salary distribution of one 
of the teams from a specific year.

"""

# Importing libraries and defining constant variables

import csv

import matplotlib.pyplot as plt

# numpy library used for statistical calculations
import numpy as np

# All the Win percentage CSV files for each team
MILWINPER = "Milwaukee Bucks Records.csv"
GSWWINPER = "Golden State Warriors Records.csv"
LALWINPER = "Los Angeles Lakers Records.csv"

# All the payroll CSV files for each team
MILPAYROLL = "Milwaukee Bucks Payroll .csv"
GSWPAYROLL = "Golden State Warriors Payroll .csv"
LALPAYROLL = "Los Angeles Payroll.csv"

# The Bucks championship payroll CSV (2020-2021)
BUCKSCHAMPAYROLL = "Bucks Championship Payroll.csv"




def read_payroll_csv(filename):
    """
    Parameters:
        filename : A csv file of strings containing teams payrolls 
    
    Returns: two lists, one for the years (strings) and 
    the other for payrolls (integers)
    
    Does: Takes in the payroll CSV files and adds the data from each column 
    (the years column and the salary column)into two seperate lists.
   
    """
    
# Defining empty lists to append values into    
    years = []
    payroll = []
    years_updated = []
    
    
# Opening the file     
    with open(filename, "r") as infile:
        
# Converting file to CSV and reading first 2 liines (title and header)
        csv_file = csv.reader(infile)
        next(csv_file)
        next(csv_file)
    
# Iterating through CSV file and appending values to 2 lists 
        for row in csv_file:
            years.append(row[0])
            payroll.append(int(row[1]))
            
# Iterating through elements in years to slice strings (2001/02 -> 02)     
        for element in years:
            years_updated.append(element[:4])
            

        return payroll, years_updated
    
    
    
    
    
def read_records_csv(filename):
    """

    Parameters:
        filename : A csv file of strings containing teams win percentages
    
    Returns: a list of floats for the win percentages
    
    Does: Takes in the records CSV files and appends the data from the 
    column with the win percentages into a list of floats
    
    """
    
# Defining empty lists to append values into
    winpercentage = []
    
# Opening the file 
    with open(filename, "r") as infile:
        
# Converting file to CSV and reading the first line (header)
        csv_file = csv.reader(infile)
        next(csv_file)

# Iterating through CSV file and appending values to list      
        for row in csv_file:
            winpercentage.append(float(row[5]))

# Reversing list order to make it in chronological order(2001-2022)
        winpercentage = winpercentage[::-1]
        
    
        return winpercentage
    
    
    
def create_line_chart(lstyears, lst, label, color, ylabel):
    """
    Parameters:
        lstyears : a list of years that can be used for every team (strings)
        lst : a list of any numerical data (float or int)
        label: a label for the specific line on the chart (string)
        color: the color of the specific line on the chart (string)
        ylabel: what the y label of the line chart should be (string)

    Returns: nothing
    
    Does: Creates a line chart given 2 lists(years and numerical data) and 
    adds labels, colors, and a label for the y axis
    
    """
    
    
# Iterating through all three teams and plotting the data of the given list
    for i in range(len(label)):
       plt.plot(lstyears, lst[i], label = label[i], color = color[i])
       
     
# Defining the x axis increments
    plt.xticks([0, 5, 10, 15, 20])
    
# Adding labels, title, and legend    
    plt.xlabel("Years")
    plt.ylabel(ylabel)
    plt.title(ylabel + " over Years from 2001-2022")
    plt.legend()

    



def create_scatterplot(lst1, lst2, team, xlabel, ylabel, title):
    
    """
    Parameters:
        lst_1: a list of the independent (x) variable (float or int)
        lst_2 : a list of the dependent (y) variable (float or int)
        team: the team name (string)
        xlabel: what the x label of the line chart should be (string)
        ylabel: what the y label of the line chart should be (string)
        title: the title of the chart (string)

    Returns: Nothing
    
    Does: Creates a scatterplot of variable 1 vs variable 2 for any
    given lists and adds axis labels, a title, and a trendline when given 2 
    lists of numerical data
   
    """
    
# Plotting scatterplot 
    plt.scatter(lst1, lst2)
       
# Addinf axis labels and titles    
    plt.xlabel(team + xlabel)
    plt.ylabel(team + ylabel)
    plt.title(team + title)
    
    
# Adding trendline to the plot
    equation = np.polyfit(lst1, lst2, 1)
    plot = np.poly1d(equation)

# Plots the trendline in reference to the x axis (independent variable)
    plt.plot(lst1, plot(lst1))

    
    plt.show()
    
    
    



def calculate_stats(lst):
    """
    Parameters: 
        lst: any list of numbers (float or int)
        
    Returns: the mean, median, and standard deviation for the list of numbers
    rounded to 2 decimal points (floats)
    
    Does: Calculates the avg, median, and std dev for a given list of numbers
    (float or int)
    
    """
    
# Used with numpy library
    
# Saving the calculations of the basic stats to variables
    mean = round(np.mean(lst), 2)
    
    median = round(np.median(lst), 2)
    
    std_dev = round(np.std(lst), 2)
    
    return mean, median, std_dev





def correlation_coefficient(lst1, lst2):
    """
    Parameters:
        lst1 : any list of numbers (float or int)
        lst2 : any list of numbers (float or int)
        
    Returns: the correlation coefficient between two lists (floats)
   
    Does: takes in two lists with numerical data and returns the Pearsons
    Correlation Coefficient between the lists

    """
# Used with numpy library

# Calculating the correlation coefficient between the data from the two lists
    correlation_coefficient = np.corrcoef(lst1, lst2)
    
    return correlation_coefficient






def read_sznpayroll_csv(filename):
    """
    Parameters:
        filename : A csv file of strings containing a team's salary for a 
        specific year and the associated players

    Returns: two lists, one for the players (strings) and one for the 
    salaries of each player (float)

    Does: takes in a CSV file of strings, adds the data from the column 
    containing the players names into a list of strings and adds the data 
    from the column containing the players salaries into a list of floats

    """
    
# Defining empty lists to append values into
    players = []
    players_salary = []
    players_salary_float = []
    
    
# Opening the file and converting to csv
    with open(filename, "r") as infile:
        csv_file = csv.reader(infile)
        next(csv_file)
    
    
# Iterating through the csv file and appending data depending on column
        for row in csv_file:
            players.append(row[1])
            players_salary.append(row[2])
            
            
# Iterating through the data in the players salary 
        for element in players_salary:
# Replacing characters in each element to convert to float
            element = (element.replace("$", "").replace(",", ""))
            if element != "" and element != "-":    
# Converting to float and dividing by million 
# This keeps payroll data consistent with the other CSV files
                players_salary_float.append(float(element)/1000000)
        
       
    return players, players_salary_float





def create_histogram(data, bin_width, xlabel, ylabel, title):
    """
    Parameters:
        data : a list of any numerical data (floats or ints)
        bin_width : the width of each individual bar in the histogram (int)
        xlabel : label for the x axis (string)
        ylabel : label for the y axis (string)
        title : any title for the histogram (string)

    Returns: nothing
    
    Does: Takes in data from a list and creates a histogram showing the 
    distrbution of the data

    """
        
    
# Creating an array of bin edges for the histogram.
# Arranging the bins depending on the min and max values for the given data
    bins = np.arange(min(data), max(data)
                     + bin_width, bin_width)
    
    
# Finding the average and plotting the average line on the histogram
    average = np.mean(data)
    
    plt.axvline(average, color = "Red", linewidth = 3, 
                label = "Average Salary of the Roster")

# Plot the histogram using matplotlib

    plt.hist(data, bins = bins, edgecolor ='black')

# Add axis labels, title, and legend
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    
    plt.show()

    
    
    

    

def main():
    
    
# Reading years and saving them to 1 variable becuase years are consistent 
    years = read_payroll_csv(GSWPAYROLL)[1]
    
# Reading the payrolls for each team and saving them to variables
    gswpayroll = read_payroll_csv(GSWPAYROLL)[0]
    milpayroll = read_payroll_csv(MILPAYROLL)[0]
    lalpayroll = read_payroll_csv(LALPAYROLL)[0]
    
# Creating a 2d list of all the payrolls
    payrolls = [gswpayroll, milpayroll, lalpayroll]
   

# Reading the win percentages for each team and saving them to variables
    gswinper = read_records_csv(GSWWINPER)
    milwinper = read_records_csv(MILWINPER)
    lalwinper = read_records_csv(LALWINPER)

# Creating a 2d list of all the win percentages
    winpers = [gswinper, milwinper, lalwinper]


# Communication - Through Graphs

# Saving the labels and associated colors of each team for graphing purposes
    labels = ["GSW", "MIL", "LAL"]
    colors = ["gold", "green", "purple"]


# Plotting the line charts for the payrolls and win percentages
    create_line_chart(years, payrolls, labels, 
                      colors, "Payrolls (in millions) of dollars")
    plt.show()
    
    create_line_chart(years, winpers, labels, colors, "Win Percentages")
    
    plt.show()
    
    
     
# Creating scatterplots of payrolls vs winpers for each team

    create_scatterplot(gswpayroll, gswinper, "GSW ", 
    "Payrolls (in millions) of dollars", "Win Percentages",
    "Payrolls (in millions) of dollars vs Win Percentages from 2001-2022")
    
    create_scatterplot(milpayroll, milwinper, "MIL ", 
    "Payrolls (in millions) of dollars", "Win Percentages",
    "Payrolls (in millions) of dollars vs Win Percentages from 2001-2022")
    
    create_scatterplot(lalpayroll, lalwinper, "LAL ",
    "Payrolls (in millions) of dollars", "Win Percentages", 
    "Payrolls (in millions) of dollars vs Win Percentages from 2001-2022")
    
    
    
# Calculating stats (mean, median, and standard deviation) of teams winper    
    for i in range(len(winpers)):
        winper = winpers[i]
        label = labels[i]
        winper_stats = calculate_stats(winper)
        print("The mean, median, and std.dev for the",
              label, "win percentages are", winper_stats)
        
       
    
# Calculating correlation coefficients of payroll and winper data for teams    
# Cor cof given as matrix. "[0,1]" accesses the the correct value in matrix
        
    gswcorcof = correlation_coefficient(gswpayroll, gswinper)
    print("Correlation coefficient for GSW:", round(gswcorcof[0,1], 2))
    
    milcorcof = correlation_coefficient(milpayroll, milwinper)
    print("Correlation coefficient for MIL:", round(milcorcof[0,1], 2))
    
    lalcorcof = correlation_coefficient(lalpayroll, lalwinper)
    print("Correlation coefficient for LAL:", round(lalcorcof[0,1], 2))
    

# Calculating the Coefficient of Determination value for teams
    gswcofdet = round((gswcorcof[0,1] ** 2), 2)
    print("Coefficient of Determination for GSW:", gswcofdet)
    milcofdet = round(milcorcof[0,1] ** 2, 2)
    print("Coefficient of Determination for MIL:", milcofdet)
    lalcofdet = round(lalcorcof[0,1] ** 2, 2)
    print("Coefficient of Determination for LAL:", lalcofdet)
    
    
    

# Calling the functions related to the Bucks Championship Payroll Data

# Reading the players and associated payroll of a specific season data 
# Data is the Bucks Championship team (2020-2021) 
    bucks_champ_players = read_sznpayroll_csv(BUCKSCHAMPAYROLL)[0]
    bucks_champ_payroll = read_sznpayroll_csv(BUCKSCHAMPAYROLL)[1]
    
    
# Calculating stats (mean, median, and standard deviaiton) for 2020 Bucks
    bucks_champ_stats = calculate_stats(bucks_champ_payroll)
    print("The Bucks stats for their championship year are:", 
          bucks_champ_stats)
    
    
# Iterating by position through bucks championship payroll list
    for i in range(len(bucks_champ_payroll)):
# Seeing if players payrolls is above the average
        if bucks_champ_payroll[i] > bucks_champ_stats[0]:
# Printing the players who are making above the average 
# Also printing how much they are making
           print(bucks_champ_players[i], 
                 "is making $", round(bucks_champ_payroll[i], 2), "million")
            
            
    
# Plotting the Histogram using the Bucks 2020 season payroll 
    create_histogram(bucks_champ_payroll, 1,
    "Salaries(in millions) of dollars" ,"Frequency",
    "Salary Distribution for the MIL Bucks Championship Season")
    
    


main()

