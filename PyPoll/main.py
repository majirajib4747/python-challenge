import csv
import os

# Open Files

#input file path
script_dir = os.path.dirname(__file__)
input_rel_path = "Resources/election_data.csv"
abs_file_path_input = os.path.join(script_dir, input_rel_path)

#output file path

script_dir = os.path.dirname(__file__)
output_rel_path = "analysis/pollanalysisoutput.txt"
abs_file_path_output = os.path.join(script_dir, output_rel_path)


pypollfile = open (abs_file_path_input ,"r")
analysisoutputfile = open (abs_file_path_output ,"w")


reader = csv.reader(pypollfile)

# Initialize the Variables
count = 0
candidate = []
temp_candidate = ""
candidate_count = 0
individual_candidate_count = 0
temp_percentage = 0
winner = ""

# Omit the Header
headers = next(reader, None)

# Read the CSV and find the output results

for x in reader:

    count = count + 1
    candidate.append(x[2])

print("Election Result")
print("------------------------------------")
print ("Total Votes: " + str(len(candidate)))
print("------------------------------------")

analysisoutputfile.write("Election Result\n\n")
analysisoutputfile.write("------------------------------------\n")
analysisoutputfile.write ("Total Votes: " + str(len(candidate))+ "\n")
analysisoutputfile.write("------------------------------------\n")


for candidateitem in sorted(candidate):
    #print(candidateitem)

    if  candidate_count > 0 :
            # When Candidate Name change calculate Total Votes and Percentage
            if (candidateitem != temp_candidate) :
                percentage = (individual_candidate_count * 100) / len(candidate)
                print ( temp_candidate + ":    " + str('{0:.2f}'.format(percentage)) + "%" + "   " + "(" + str(individual_candidate_count)  + ")" )
                analysisoutputfile.write(temp_candidate + ":    " + str('{0:.2f}'.format(percentage)) + "%" + "   " + "(" + str(
                    individual_candidate_count) + ")" + "\n")
                individual_candidate_count = 1

                if percentage > temp_percentage :
                    winner = temp_candidate
                    temp_percentage = percentage
                else :
                    temp_percentage = percentage

                temp_candidate = candidateitem
            else :
                    individual_candidate_count = individual_candidate_count + 1
                    temp_candidate = candidateitem

    else :
                individual_candidate_count = individual_candidate_count + 1
                temp_candidate = candidateitem


    candidate_count = candidate_count + 1

# For Last record
percentage = (individual_candidate_count * 100) / len(candidate)

if percentage > temp_percentage:
    winner = temp_candidate
    temp_percentage = percentage
else:
    temp_percentage = percentage

print ( temp_candidate + ":    " + str('{0:.2f}'.format(percentage)) + "%" + "   " + "(" + str(individual_candidate_count)  + ")" + "\n")

print("------------------------------------")

print ("Winner: " + winner + "\n")
print("------------------------------------")


analysisoutputfile.write ( temp_candidate + ":    " + str('{0:.2f}'.format(percentage)) + "%" + "   " + "(" + str(individual_candidate_count)  + ")" + "\n")

analysisoutputfile.write("------------------------------------\n\n")

analysisoutputfile.write ("Winner: " + winner + "\n\n")
analysisoutputfile.write("------------------------------------")

# Close the Files

pypollfile.close()
analysisoutputfile.close()























