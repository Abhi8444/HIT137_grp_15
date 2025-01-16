import os
import pandas as pd

#folder name which containing CSV files
folder_path = 'temperature_data'

# creating empty dictionary temperatures for each month and each season
monthly_averages = {month: [] for month in range(1, 13)}
seasonal_averages = {'Summer': [], 'Autumn': [], 'Winter': [], 'Spring': []}

# for each and every csv file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        # Read the CSV file
        df = pd.read_csv(file_path)
        
            # creating  Loop for each month and calculate the average temperature
            for i, month in enumerate(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], start=1):
                monthly_avg = df[month].mean()
                monthly_averages[i].append(monthly_avg)

# Calculate the overall average temperature for each month
overall_monthly_averages = {month: sum(temps) / len(temps) for month, temps in monthly_averages.items() if temps}



# Calculating the overall average temperature for each season
overall_seasonal_averages = {season: sum(temps) / len(temps) for season, temps in seasonal_averages.items() if temps}

# Saving the results to files
with open('average_temp.txt', 'w') as file:
    for month, avg_temp in overall_monthly_averages.items():
        file.write(f"Month {month}: {avg_temp:.2f}C\n")

with open('average_seasonal_temp.txt', 'w') as file:
    for season, avg_temp in overall_seasonal_averages.items():
        file.write(f"{season}: {avg_temp:.2f}C\n")

print("Average monthly and seasonal temperatures have been calculated and saved to 'average_temp.txt' and 'average_seasonal_temp.txt'.")