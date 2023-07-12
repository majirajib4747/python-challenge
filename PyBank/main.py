import csv
import os

# Open Files

#input file path
script_dir = os.path.dirname(__file__)
input_rel_path = "Resources/budget_data.csv"
abs_file_path_input = os.path.join(script_dir, input_rel_path)

#output file path

script_dir = os.path.dirname(__file__)
output_rel_path = "analysis/analysisoutput.txt"
abs_file_path_output = os.path.join(script_dir, output_rel_path)


pybankfile = open (abs_file_path_input ,"r")
analysisoutputfile = open (abs_file_path_output ,"w")

reader = csv.reader(pybankfile)
monthname_collection = []

#Initialize Variables

profit_loss = []
Total_Profit_Loss = 0
Initial_Profit = 0
count = 0
max_profit = 0
min_profit = 0

headers = next(reader, None)

# Read the CSV and find the output results

for x in reader:
    monthname = x[0].split("-")[0]
    # needed for finding out unique month
    monthname_collection.append(monthname)
    profit_loss.append(int(x[1]))
    Total_Profit_Loss = Total_Profit_Loss + int(x[1])
    change_profit = int(x[1]) - Initial_Profit
    Initial_Profit = int(x[1])
    count = count + 1
    # Find the Maximum Profit
    if int(x[1]) > max_profit :
       max_profit_info = x[0] + " " + "(" +  "$" + x[1] + ")"
       max_profit = int(x[1])
    # Find the minimum Profit
    if int(x[1]) < min_profit:
        min_profit_info = x[0] + " " + "(" +  "$" + x[1] + ")"
        min_profit = int(x[1])


# Find the Unique Months
uniqueMonths = set(monthname_collection)

total_nos_of_months = len(uniqueMonths)

#Print out in Console

print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(total_nos_of_months))
print("Total Profits: " + "$" + str(Total_Profit_Loss))
print("Average Change: " + "$" + "{:.2f}".format(change_profit/count))
print("Greatest Increase in Profits: " + max_profit_info)
print("Greatest Decrease in Profits: " + min_profit_info)

# Write into output File


analysisoutputfile.write("  Financial Analysis"+ "\n")
analysisoutputfile.write("----------------------------------------------------------\n\n")
analysisoutputfile.write("    Total Months: " + str(total_nos_of_months) + "\n")
analysisoutputfile.write("    Total Profits: " + "$" + str(Total_Profit_Loss) +"\n")
analysisoutputfile.write("    Average Change: " + '$' + "{:.2f}".format(change_profit/count) + "\n")
analysisoutputfile.write("    Greatest Increase in Profits: " + max_profit_info + "\n")
analysisoutputfile.write("    Greatest Decrease in Profits: " + min_profit_info + "\n")

# Close the Files

pybankfile.close()
analysisoutputfile.close()













