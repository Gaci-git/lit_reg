#                             #
#   MAIN PROJECT FILE TO RUN  #
#                             #


from flask import Flask, render_template, request
import Main
import Calculator.calculating_missing_data

# DATA SOURCE: https://gionkunz.github.io/chartist-js/getting-started.html

app = Flask(__name__)

# Injecting Enumerate function into Template manager.
# By default Flasks template engine doesnt support Enumerate
@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)


# Home page, Index page
# Reading CSV and creating list of regions (Apylinkes)

@app.route("/")
def home_page():
    output_2020_list = Main.read_csv_file_and_save_data("Output_2020_csv.csv")
    apylinkiu_sarasas = []
    for elementas in output_2020_list:
        apylinkiu_sarasas.append(elementas[1])




    # Calculating and saving missing data to LIST

    total_lt_2015 = Main.read_csv_file_and_save_total_lt_data("Output_2015_csv.csv")
    total_lt_2016 = Main.read_csv_file_and_save_total_lt_data("Output_2016_csv.csv")
    total_lt_2017 = Main.read_csv_file_and_save_total_lt_data("Output_2017_csv.csv")
    total_lt_2018 = Main.read_csv_file_and_save_total_lt_data("Output_2018_csv.csv")
    total_lt_2019 = Main.read_csv_file_and_save_total_lt_data("Output_2019_csv.csv")
    total_lt_2020 = Main.read_csv_file_and_save_total_lt_data("Output_2020_csv.csv")

    total_lt_duomenys = [int(total_lt_2015[2]),
                         int(total_lt_2016[2]),
                         int(total_lt_2017[3]),
                         int(total_lt_2018[2]),
                         int(total_lt_2019[2]),
                         int(total_lt_2020[2])]


    return render_template("Selection_template_bootstrap.html", apylinkiu_sarasas=apylinkiu_sarasas,
                                                                selektionai=Main.Settings.selektionai,
                                                                total_lt_duomenys=total_lt_duomenys)



# Redirection according to filter and region selection
# INPUT ARGUMENTS _>
#           Apylinkes_nr: Region number
#           filterBy:     Category filter selector (example: Kids, Adults, etc)
@app.route("/selectedApl")
def redirectToChart():
    Apylinkes_nr = request.args.get("Apylinke")
    filterBy = request.args.get("filterBy")
    return f'<html><head><script>window.location = "/Charts?Apylinke={Apylinkes_nr}&filterBy={filterBy}"</script></head></html>'


# Charts page
# Reading data according to selection
# INPUT ARGUMENTS: _>
#                   Apylinkes_nr: Region selection
#                   filterBy: Category filter selection
# FAILSAFE if no arguments are given: Throws "Informacija nepasiekiama"
@app.route("/Charts")
def display_chart():

    #Reading data from CSV into LISTs
    output_2015_list = Main.read_csv_file_and_save_data("Output_2015_csv.csv")
    output_2016_list = Main.read_csv_file_and_save_data("Output_2016_csv.csv")
    output_2017_list = Main.read_csv_file_and_save_data("Output_2017_csv.csv")
    output_2018_list = Main.read_csv_file_and_save_data("Output_2018_csv.csv")
    output_2019_list = Main.read_csv_file_and_save_data("Output_2019_csv.csv")
    output_2020_list = Main.read_csv_file_and_save_data("Output_2020_csv.csv")

    try:
        Apylinkes_nr = int(request.args.get("Apylinke"))
        filterBy = int(request.args.get("filterBy"))+2  # +2 to fix missaligned data in CSVs


        # If filterBy selection number is 6, we calculate missing data ourselves and fill the LISTs

        if filterBy == 6:
            pasirinkimo_pavadinimas = Main.Settings.selektionai[filterBy - 2]
            BGS2015 = Calculator.calculating_missing_data.calculate_misssing_data(Apylinkes_nr, output_2015_list, 2)
            BGS2016 = Calculator.calculating_missing_data.calculate_misssing_data(Apylinkes_nr, output_2016_list, 2)
            BGS2017 = Calculator.calculating_missing_data.calculate_misssing_data(Apylinkes_nr + 2, output_2017_list, 2 + 1)
            BGS2018 = Calculator.calculating_missing_data.calculate_misssing_data(Apylinkes_nr, output_2018_list, 2)
            BGS2019 = Calculator.calculating_missing_data.calculate_misssing_data(Apylinkes_nr, output_2019_list, 2)
            BGS2020 = Calculator.calculating_missing_data.calculate_misssing_data(Apylinkes_nr, output_2020_list, 2)

        else:

            #Fill the list elements according to selection

            pasirinkimo_pavadinimas = Main.Settings.selektionai[filterBy-2]
            BGS2015 = Main.get_data_from_csv_list(Apylinkes_nr,output_2015_list,filterBy)
            BGS2016 = Main.get_data_from_csv_list(Apylinkes_nr,output_2016_list,filterBy)
            BGS2017 = Main.get_data_from_csv_list(Apylinkes_nr + 2,output_2017_list,filterBy+1)
            BGS2018 = Main.get_data_from_csv_list(Apylinkes_nr, output_2018_list,filterBy)
            BGS2019 = Main.get_data_from_csv_list(Apylinkes_nr, output_2019_list,filterBy)
            BGS2020 = Main.get_data_from_csv_list(Apylinkes_nr, output_2020_list,filterBy)
    except:
        return ("Informacija nepasiekiama")




    #Return template with DATA lists
    #Arguments: _>
    #             Duomenys:                DATA Lists for charts
    #             pasirinkimo_pavadinimas: Selection name as a string
    return render_template("chart_template.html", duomenys = [BGS2015,
                                                              BGS2016,
                                                              BGS2017,
                                                              BGS2018,
                                                              BGS2019,
                                                              BGS2020],
                           pasirinkimo_pavadinimas=pasirinkimo_pavadinimas)



#Set debug to True for debugging mode
#Set debug to False for production mode
app.run(debug=False)


