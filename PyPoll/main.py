import csv
import os



# Initialize the Variables
count = 0
candidate = []
temp_candidate = ""
candidate_count = 0
individual_candidate_count = 0
temp_percentage = 0
winner = ""
pypoll_dict = {'name':[], 'percentage':[] , 'individual_count':[]}
name_list = []
percentage_list = []
individual_count_list = []

# Define Pypoll function for all calculation
def pypoll_calculation(candidate_list) :

    global count
    global candidate
    global temp_candidate
    global candidate_count
    global individual_candidate_count
    global temp_percentage
    global winner
    global pypoll_dict
    global name_list
    global percentage_list
    global individual_count_list

    for candidateitem in sorted(candidate_list):

        if candidate_count > 0:
            # When Candidate Name change calculate Total Votes and Percentage

            if (candidateitem != temp_candidate):
                percentage = (individual_candidate_count * 100) / len(candidate)

                name_list = temp_candidate
                percentage_list = str('{0:.2f}'.format(percentage)) + "%"
                individual_count_list = "(" + str(individual_candidate_count) + ")"

                pypoll_dict["name"].append(name_list)
                pypoll_dict["percentage"].append(percentage_list)
                pypoll_dict["individual_count"].append(individual_count_list)

                individual_candidate_count = 1

                if percentage > temp_percentage:
                    winner = temp_candidate
                    temp_percentage = percentage
                else:
                    temp_percentage = percentage

                temp_candidate = candidateitem
            else:
                individual_candidate_count = individual_candidate_count + 1
                temp_candidate = candidateitem

        else:
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

    name_list = temp_candidate
    percentage_list = str('{0:.2f}'.format(percentage)) + "%"
    individual_count_list = "(" + str(individual_candidate_count) + ")"

    pypoll_dict["name"].append(name_list)
    pypoll_dict["percentage"].append(percentage_list)
    pypoll_dict["individual_count"].append(individual_count_list)


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

# Omit the Header
headers = next(reader, None)

# Read the CSV and find the output results

for x in reader:

    count = count + 1
    candidate.append(x[2])

pypoll_calculation(candidate)




# Print summary in Console and write into output file

print("Election Result")
print("------------------------------------")
print ("Total Votes: " + str(len(candidate)))
print("------------------------------------")


analysisoutputfile.write("Election Result\n\n")
analysisoutputfile.write("------------------------------------\n")
analysisoutputfile.write ("Total Votes: " + str(len(candidate))+ "\n")
analysisoutputfile.write("------------------------------------\n")


total_nos_of_candidate = len(pypoll_dict['name'])


for i in range(total_nos_of_candidate) :
    print(f"{pypoll_dict['name'][i]} :  {pypoll_dict['percentage'][i]}  {pypoll_dict['individual_count'][i]}" )
    analysisoutputfile.write(f"{pypoll_dict['name'][i]} :  {pypoll_dict['percentage'][i]}  {pypoll_dict['individual_count'][i]}\n\n")


print("------------------------------------")

print("Winner is  : " + winner)

analysisoutputfile.write("------------------------------------\n")

analysisoutputfile.write("Winner is  : " + winner)

# Close the Files

pypollfile.close()
analysisoutputfile.close()























