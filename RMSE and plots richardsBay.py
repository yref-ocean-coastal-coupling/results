# get rmse's and plots for different cases:

from sklearn.metrics import mean_squared_error

import function_get_validation_data as vd
import function_get_simulation_data as sd
# plotting:
plotfolder = "PLOTSRB/"

# simulation data:
foldername = "38rbrun"
water_levels = sd.get_water_levels(foldername)
dav = sd.get_depth_averaged_velocity(foldername)
dav_flow_direction = sd.get_velocity_in_depth_averaged_flow_direction(foldername)
horz_vel_1 = sd.get_horizontal_velocity_level_1(foldername)
horz_vel_2 = sd.get_horizontal_velocity_level_2(foldername)

# validation data:
durban_currents_validation = vd.get_durban_currents()
durban_wave_validation = vd.get_durban_HS()
richardsbay_currents_validation = vd.get_richards_bay_currents()
richardsbay_wave_validation = vd.get_richards_bay_HS()


################################### RMSE ###################################
# water levels:
# combine the dataframes and then filter out nan entries
water_levels_combined = richardsbay_wave_validation.merge(water_levels, how='inner', on=None, left_on=None, right_on=None, left_index=True, right_index=True, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
# print(water_levels_combined,water_levels_combined.isnull().sum())

## get rmse:
realVals_water_levels = water_levels_combined["hm0"]
predictedVals_water_levels = water_levels_combined["water_level(m)"]
bias_water_levels = ((realVals_water_levels - predictedVals_water_levels))
rmse_water_levels = mean_squared_error(realVals_water_levels, predictedVals_water_levels,squared = False)
# print(rmse_water_levels,bias_water_levels)

# depth average velocity:
# combine the dataframes and then filter out nan entries
dav_combined = richardsbay_currents_validation.merge(dav, how='inner', on=None, left_on=None, right_on=None, left_index=True, right_index=True, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
# print(dav_combined,dav_combined.isnull().sum(),dav_combined.columns)

## get rmse:
realVals_dav_speed = dav_combined["speed"]
predictedVals_dav_speed = dav_combined["speedsim"]
bias_dav_speed = ((realVals_dav_speed - predictedVals_dav_speed))
rmse_dav_speed = mean_squared_error(realVals_dav_speed, predictedVals_dav_speed,squared = False)
# print(rmse_dav_speed,bias_dav_speed)

realVals_dav_direction = dav_combined["direction"]
predictedVals_dav_direction = dav_combined["directionsim"]
bias_dav_direction = ((realVals_dav_direction - predictedVals_dav_direction))
rmse_dav_direction = mean_squared_error(realVals_dav_direction, predictedVals_dav_direction,squared = False)
# print(rmse_dav_direction,bias_dav_direction)


# level 1 currents:
# combine the dataframes and then filter out nan entries
current_lv1_combined = richardsbay_currents_validation.merge(horz_vel_1, how='inner', on=None, left_on=None, right_on=None, left_index=True, right_index=True, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
# print(current_lv1_combined,current_lv1_combined.isnull().sum())

## get rmse:
realVals_lv1_speed = current_lv1_combined["speed"]
predictedVals_lv1_speed = current_lv1_combined["speedsim"]
bias_lev1_speed = ((realVals_lv1_speed - predictedVals_lv1_speed))
rmse_lev1_speed = mean_squared_error(realVals_lv1_speed, predictedVals_lv1_speed,squared = False)
# print(rmse_lev1_speed,bias_lev1_speed)

realVals_lv1_direction = current_lv1_combined["direction"]
predictedVals_lv1_direction = current_lv1_combined["directionsim"]
bias_lev1_direction = ((realVals_lv1_direction - predictedVals_lv1_direction))
rmse_lev1_direction = mean_squared_error(realVals_lv1_direction, predictedVals_lv1_direction,squared = False)
# print(rmse_lev1_direction,bias_lev1_direction)

# level 2 currents:
# combine the dataframes and then filter out nan entries
current_lv2_combined = richardsbay_currents_validation.merge(horz_vel_2, how='inner', on=None, left_on=None, right_on=None, left_index=True, right_index=True, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
# print(current_lv2_combined,current_lv2_combined.isnull().sum())

## get rmse:
realVals_lv2_speed = current_lv2_combined["speed"]
predictedVals_lv2_speed = current_lv2_combined["speedsim"]
bias_lev2_speed = ((realVals_lv2_speed - predictedVals_lv2_speed))
rmse_lev2_speed = mean_squared_error(realVals_lv2_speed, predictedVals_lv2_speed,squared = False)
# print(rmse_lev2_speed,bias_lev2_speed)

realVals_lv2_direction = current_lv2_combined["direction"]
predictedVals_lv2_direction = current_lv2_combined["directionsim"]
bias_lev2_direction = ((realVals_lv2_direction - predictedVals_lv2_direction))
rmse_lev2_direction = mean_squared_error(realVals_lv2_direction, predictedVals_lv2_direction,squared = False)
# print(rmse_lev2_direction,bias_lev2_direction)
with open(plotfolder+foldername+"_RMSEs.txt","w") as outfile:
    print("######################################################################",file=outfile)
    print("##############################  RMSE's  ##############################",file=outfile)
    print("######################################################################",file=outfile)

    print(foldername,file=outfile)
    print("rmse_water_levels:   ",rmse_water_levels,file=outfile)
    print("rmse_dav_speed:      ",rmse_dav_speed,file=outfile)
    print("rmse_dav_direction:  ",rmse_dav_direction,file=outfile)
    print("rmse_lev1_speed:     ",rmse_lev1_speed,file=outfile)
    print("rmse_lev1_direction: ",rmse_lev1_direction,file=outfile)
    print("rmse_lev2_speed:     ",rmse_lev2_speed,file=outfile)
    print("rmse_lev2_direction: ",rmse_lev2_direction,file=outfile)

    print("############################      END     ############################",file=outfile)

################################### plots ###################################
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def _plot_bias(dates,ydata,figname,title,xaxis,yaxis):
    plt.figure(figsize=(20,10))
    plt.title(foldername+": "+title,fontsize=24)
    plt.xlabel(xaxis,fontsize=20)
    plt.ylabel(yaxis,fontsize=20)
    plt.plot(dates,ydata)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.savefig(plotfolder+foldername+"_"+figname,bbox_inches="tight")


def _plot_comparison(dates,validation,simulation,figname,title,xaxis,yaxis):
    plt.figure(figsize=(20,10))
    plt.title(foldername+": "+title,fontsize=24)
    plt.xlabel(xaxis,fontsize=20)
    plt.ylabel(yaxis,fontsize=20)
    plt.plot(dates,validation,"b*",label="validation")
    plt.plot(dates,simulation,"r--",label="simulation")
    plt.legend(fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.savefig(plotfolder+foldername+"_"+figname,bbox_inches="tight")

# water levels:
_plot_bias(realVals_water_levels.index,bias_water_levels,"waterlevel_bias.png","Water level bias (validation-simulation)","Date","Water level (m)")
_plot_comparison(realVals_water_levels.index,realVals_water_levels,predictedVals_water_levels,"waterlevels.png","Water levels","Date","Water level (m)")

# dav:
## speed
_plot_bias(realVals_dav_speed.index,bias_dav_speed,"depth_average_velocity_speed_bias.png","Depth average velocity speed bias (validation-simulation)","Date","Speed (m/s)")
_plot_comparison(realVals_dav_speed.index,realVals_dav_speed,predictedVals_dav_speed,"depth_average_velocity_speed.png","Depth average velocity speed","Date","Speed (m/s)")
## direction
_plot_bias(realVals_dav_direction.index,bias_dav_direction,"depth_average_velocity_direction_bias.png","Depth average velocity direction bias (validation-simulation)","Date","Direction (nautical)")
_plot_comparison(realVals_dav_direction.index,realVals_dav_direction,predictedVals_dav_direction,"depth_average_velocity_direction.png","Depth average velocity direction","Date","Direction (nautical)")

# lev1:
## speed
_plot_bias(realVals_lv1_speed.index,bias_lev1_speed,"horz_velocity_lv1_speed_bias.png","Horizontal velocity (lv1) speed bias (validation-simulation)","Date","Speed (m/s)")
_plot_comparison(realVals_lv1_speed.index,realVals_lv1_speed,predictedVals_lv1_speed,"horz_lv1_velocity_speed.png","Horizontal velocity (lv1) speed","Date","Speed (m/s)")
## direction
_plot_bias(realVals_lv1_direction.index,bias_lev1_direction,"horz_velocity_lv1_direction_bias.png","Horizontal velocity (lv1) direction bias (validation-simulation)","Date","Direction (nautical)")
_plot_comparison(realVals_lv1_direction.index,realVals_lv1_direction,predictedVals_lv1_direction,"horz_lv1_velocity_direction.png","Horizontal velocity (lv1) direction","Date","Direction (nautical)")

# lev2:
## speed
_plot_bias(realVals_lv2_speed.index,bias_lev2_speed,"horz_velocity_lv2_speed_bias.png","Horizontal velocity (lv2) speed bias (validation-simulation)","Date","Speed (m/s)")
_plot_comparison(realVals_lv2_speed.index,realVals_lv2_speed,predictedVals_lv2_speed,"horz_lv2_velocity_speed.png","Horizontal velocity (lv2) speed","Date","Speed (m/s)")
## direction
_plot_bias(realVals_lv1_direction.index,bias_lev1_direction,"horz_velocity_lv2_direction_bias.png","Horizontal velocity (lv2) direction bias (validation-simulation)","Date","Direction (nautical)")
_plot_comparison(realVals_lv1_direction.index,realVals_lv1_direction,predictedVals_lv1_direction,"horz_lv2_velocity_direction.png","Horizontal velocity (lv2) direction","Date","Direction (nautical)")



