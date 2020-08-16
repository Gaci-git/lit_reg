#                                      #
#   MAIN FILE CONTAINING FUNCTIONS     #
#                                      #


import pdftables_api
import Settings
import requests
import csv



# Function that downloads files from the internet
# INPUT Arguments _>
#                   source_file: Source address to download file from (www.example.com/file.pdf)
#                   output_file: Destination file name (file.pdf)
def download_from_internet(source_file, output_file):
    response = requests.get(source_file)
    outputfile = open(output_file, "wb")
    outputfile.write(response.content)
    outputfile.close()


# Reading file and returning data as a list
# Arguments _>
#             csv_file: file from local storage (file.csv)
# NOTES: File can be any format (csv,txt,..), as long as it's formated as CSV file.
# OUTPUT _>
#           output_list: LIST element
def read_csv_file_and_save_data(csv_file):
    output_list = []
    with open(csv_file) as csv_file_read:
        data = csv.reader(csv_file_read)
        for row in data:

            #Filtering by entries that has numeric value in the first(row[0]) element.
            #If it's not numeric, pass
            #If it's numeric, append to the list
            try:
                int(row[0])
                output_list.append(row)
            except:
                pass
    return output_list


# Reading CSV file and outputing last row of the CSV file.
# INPUT Arguments _>
#                   csv_file: Local file on disk (file.csv)
# OUTPUT: _>
#           total_lt[0]: LIST Element
def read_csv_file_and_save_total_lt_data(csv_file):
    total_lt = []
    with open(csv_file) as csv_file_read:
        for row in reversed(list(csv.reader(csv_file_read))):
            total_lt.append(row)
    return total_lt[0]


# Commended to save API Calls. Function cluster to download and convert PDFs to CSVs bellow

# download_from_internet(Settings.Source_2020, 'Output_2020.pdf')
# download_from_internet(Settings.Source_2019, 'Output_2019.pdf')
# download_from_internet(Settings.Source_2018, 'Output_2018.pdf')
# download_from_internet(Settings.Source_2017, 'Output_2017.pdf')
# download_from_internet(Settings.Source_2016, 'Output_2016.pdf')
# download_from_internet(Settings.Source_2015, 'Output_2015.pdf')
#
#
# convert_pdf_to_csv("Output_2020.pdf", "Output_2020_csv")
# convert_pdf_to_csv("Output_2019.pdf", "Output_2019_csv")
# convert_pdf_to_csv("Output_2018.pdf", "Output_2018_csv")
# convert_pdf_to_csv("Output_2017.pdf", "Output_2017_csv")
# convert_pdf_to_csv("Output_2016.pdf", "Output_2016_csv")
# convert_pdf_to_csv("Output_2015.pdf", "Output_2015_csv")





# If the data is missaligned, try moving up to 5 positions further.
# ARGUMENTS _>
#               Apylinkes_nr:    Region number
#               input_list:      LIST element containing data already extracted from CSV
#               position_in_csv: Starting position
# OUTPUT _>
#           data: fixed list with new positioning
def get_data_from_csv_list(Apylinkes_nr, input_list, position_in_csv):
    Addition = 0
    while True:
        try:
            data = int(input_list[Apylinkes_nr][position_in_csv+Addition])
            break
        except:
            if Addition == 5:
                break
            Addition +=1
    return data














