# opens the simulation data:
import numpy as np
import pandas as pd


# this function will get the wind direction from the u and v component of the wind and then convert it into degrees

def _getWindDir(udata, vdata):
    # length to loop over
    # lengthOfData = len(udata)
    # data arrays
    # direction = np.zeros(lengthOfData)

    # 5 cases to consider:
    """
    uv   uv   uv   uv   uv
    ++   --   +-   -+   00
    """

    # for i in range(lengthOfData):
    # get the components
    ucom = udata
    vcom = vdata

    # get the abs for the calculation
    absu = np.abs(ucom)
    absv = np.abs(vcom)

    if ucom <= 1e-6 and ucom >= -1e-6 or vcom <= 1e-6 and vcom >= -1e-6:
        if ucom <= 1e-6 and ucom >= -1e-6 and vcom <= 1e-6 and vcom >= -1e-6:  ## both components 0
            direction = 0
        elif (ucom <= 1e-6 and ucom >= -1e-6) and not (vcom <= 1e-6 and vcom >= -1e-6):  # u component 0
            if vcom > 0:
                direction = 0  # point up
            else:
                direction = 180  # point down
        else:  # v component 0
            if ucom > 0:
                direction = 90  # point right
            else:
                direction = 270  # point left
    elif ucom > 0 and vcom > 0:  # first quadrant, angle offset = 90 -
        direction = 90 - np.arctan(absv / absu) * 180 / np.pi
    elif ucom < 0 and vcom < 0:  # third quadrant, angle offset = 270 -
        direction = 270 - np.arctan(absv / absu) * 180 / np.pi
    elif ucom < 0 and vcom > 0:  # forth quadrant, angle offset = 270 +
        direction = 270 + np.arctan(absv / absu) * 180 / np.pi
    elif ucom > 0 and vcom < 0:  # second quadrant, angle offset = 90 +
        direction = 90 + np.arctan(absv / absu) * 180 / np.pi
    else:
        print("Something went wrong???"  + "  commponents: u-" + str(absu) + "  v-" + str(absv))

    return direction

def get_water_levels(folder_name):
    data = pd.read_csv(folder_name+"/water level.csv",delimiter=",")
    data.columns = ["date","water_level(m)"]
    data = data.set_index(data["date"])
    return data

def get_depth_averaged_velocity(folder_name):
    data = pd.read_csv(folder_name+"/depth averaged velocity.csv",delimiter=",")
    data.columns = ["date","dav_Xcurrent(m/s)","dav_Ycurrent(m/s)"]
    # speed
    data["speedsim"] = np.sqrt(np.square(data["dav_Xcurrent(m/s)"]) + np.square(data["dav_Ycurrent(m/s)"]))
    # direction
    direction = []
    for index,line in data.iterrows():
        direction.append(_getWindDir(line["dav_Xcurrent(m/s)"],line["dav_Ycurrent(m/s)"]))
    data["directionsim"] = np.array(direction)
    data = data.set_index(data["date"])
    return data

def get_velocity_in_depth_averaged_flow_direction(folder_name):
    data = pd.read_csv(folder_name+"/velocity in depth averaged flow direction.csv",delimiter=",",skiprows=1)
    data.columns = ["date","dav_flow_direction_level_1(m/s)","dav_flow_direction_level_2(m/s)","dav_flow_direction_level_3(m/s)","dav_flow_direction_level_4(m/s)","dav_flow_direction_level_5(m/s)","dav_flow_direction_level_6(m/s)","dav_flow_direction_level_7(m/s)","dav_flow_direction_level_8(m/s)","dav_flow_direction_level_9(m/s)","dav_flow_direction_level_10(m/s)"]
    data = data.set_index(data["date"])
    return data

def get_horizontal_velocity_level_1(folder_name):
    data = pd.read_csv(folder_name+"/velocity (horizontal) 1.csv",delimiter=",",skiprows=1)
    data.columns = ["date","Xcurrent_level_1(m/s)","Ycurrent_level_1(m/s)"]
    # speed
    data["speedsim"] = np.sqrt(np.square(data["Xcurrent_level_1(m/s)"]) + np.square(data["Ycurrent_level_1(m/s)"]))
    # direction
    direction = []
    for index, line in data.iterrows():
        direction.append(_getWindDir(line["Xcurrent_level_1(m/s)"], line["Ycurrent_level_1(m/s)"]))
    data["directionsim"] = np.array(direction)
    data = data.set_index(data["date"])
    return data

def get_horizontal_velocity_level_2(folder_name):
    data = pd.read_csv(folder_name+"/velocity (horizontal) 2.csv",delimiter=",",skiprows=1)
    data.columns = ["date","Xcurrent_level_2(m/s)","Ycurrent_level_2(m/s)"]
    # speed
    data["speedsim"] = np.sqrt(np.square(data["Xcurrent_level_2(m/s)"]) + np.square(data["Ycurrent_level_2(m/s)"]))
    # direction
    direction = []
    for index, line in data.iterrows():
        direction.append(_getWindDir(line["Xcurrent_level_2(m/s)"], line["Ycurrent_level_2(m/s)"]))
    data["directionsim"] = np.array(direction)
    data = data.set_index(data["date"])
    return data



if __name__ == '__main__':
    print(get_water_levels("01dbnrun"))
    print(get_depth_averaged_velocity("01dbnrun").iloc[0])
    print(get_velocity_in_depth_averaged_flow_direction("01dbnrun"))
    print(get_horizontal_velocity_level_1("01dbnrun"))
    print(get_horizontal_velocity_level_2("01dbnrun"))


