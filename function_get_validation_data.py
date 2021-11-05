# functions to get the validation data:
import numpy as np
import pandas as pd

def get_durban_currents():
    # open files:
    validationdata = pd.read_csv("validationdata/Dbn_cur_180.csv", delim_whitespace=True, skiprows=60, skipfooter=1)
    validationdata.columns = ["date","time", "speed", "direction"]
    validationdata_temp = pd.to_datetime(validationdata['date']+" "+validationdata['time'])
    validationdata = validationdata.set_index(validationdata_temp)
    # remove nan
    validationdata[validationdata["speed"] > 10] = np.nan
    validationdata[validationdata["direction"] > 400] = np.nan
    validationdata = validationdata[validationdata['speed'].notna()]
    validationdata = validationdata[validationdata['direction'].notna()]
    return validationdata




def get_richards_bay_currents():
    # open files:
    validationdata = pd.read_csv("validationdata/RBay_cur_180.csv", delim_whitespace=True, skiprows=48, skipfooter=1)
    validationdata.columns = ["date","time", "speed", "direction"]
    validationdata_temp = pd.to_datetime(validationdata['date']+" "+validationdata['time'])
    validationdata = validationdata.set_index(validationdata_temp)
    # remove nan
    validationdata[validationdata["speed"] > 10] = np.nan
    validationdata[validationdata["direction"] > 400] = np.nan
    validationdata = validationdata[validationdata['speed'].notna()]
    validationdata = validationdata[validationdata['direction'].notna()]
    return validationdata


def get_durban_HS():
    # open files:
    validationdata = pd.read_csv("validationdata/db08_180.csv", delim_whitespace=True, skiprows=12, skipfooter=1)
    validationdata.columns = ["index", "year", "month", "day", "hour", "hm0", "h1", "tp", "tz", "tc", "tb", "direction",
                              "spreaddf", "hs", "hmax", "instrumentcode"]
    # divide by hundred because pandas doesnt take the time into consideration and difficult to combine through traditional methods found online.
    for index,line in validationdata.iterrows():
        validationdata.at[index,"hour"] = line["hour"]/100
    validationdata_temp = pd.to_datetime(validationdata[["year","month","day","hour"]])
    validationdata = validationdata.set_index(validationdata_temp)
    # remove nan
    validationdata[validationdata["hm0"] > 40] = np.nan
    validationdata[validationdata["direction"] > 400] = np.nan
    validationdata = validationdata[validationdata['hm0'].notna()]
    validationdata = validationdata[validationdata['direction'].notna()]
    return validationdata

def get_richards_bay_HS():
    # open files:
    validationdata = pd.read_csv("validationdata/rb01_180.csv", delim_whitespace=True, skiprows=12, skipfooter=1)
    validationdata.columns = ["index", "year", "month", "day", "hour", "hm0", "h1", "tp", "tz", "tc", "tb", "direction",
                              "spreaddf", "hs", "hmax", "instrumentcode"]
    # divide by hundred because pandas doesnt take the time into consideration and difficult to combine through traditional methods found online.
    for index, line in validationdata.iterrows():
        validationdata.at[index, "hour"] = line["hour"] / 100
    validationdata_temp = pd.to_datetime(validationdata[["year", "month", "day", "hour"]])
    validationdata = validationdata.set_index(validationdata_temp)
    # remove nan
    validationdata[validationdata["hm0"] > 40] = np.nan
    validationdata[validationdata["direction"] > 400] = np.nan
    validationdata = validationdata[validationdata['hm0'].notna()]
    validationdata = validationdata[validationdata['direction'].notna()]
    return validationdata


if __name__ == '__main__':
    print(get_durban_currents())
    print(get_richards_bay_currents())
    print(get_durban_HS())
    print(get_richards_bay_HS())

