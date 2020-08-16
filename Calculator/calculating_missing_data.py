#                                                 #
#   FILE THATS USED FOR MISSING DATA CALCULATION  #
#                                                 #


import Main


# Function that calculates missing data, using the data we already obtained
# INPUT Arguments _>
#                   Apylinkes_nr:       Region number
#                   list_to_go_through: LIST element to go through and calculate missing data based on
#                   position_in_csv:    Position to read data from
# OUTPUT _>
#           data: INTEGER element that we get from calculation
def calculate_misssing_data(Apylinkes_nr, list_to_go_through, position_in_csv):
    data = 0
    for x in range(position_in_csv, position_in_csv+4):
        if x == position_in_csv:
            data = Main.get_data_from_csv_list(Apylinkes_nr, list_to_go_through,x)
        else:
            data = data - Main.get_data_from_csv_list(Apylinkes_nr,list_to_go_through,x)

    return data

