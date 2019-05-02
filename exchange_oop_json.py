import json


# create a class that looks like our data
# create methods that load the data from json
    # pass it into instances our class

class RatesPasser:

    def __init__(self, rate_file):
        # need access to json file
        # to do this you need to open it; we can create a method to do this for us, see __open_json_file

        rates_info_dict = self.__open_json_file(rate_file)

        self.base = rates_info_dict['base']
        self.date = rates_info_dict['date']
        self.rates = rates_info_dict['rates']

        self.aud = self.rates['AUD']
        self.gbp = self.rates['GBP']

    def __open_json_file(self, file_name_path): # created a method to open a json file
        with open(file_name_path) as rates:
            return json.load(rates) #will return a dictionary

