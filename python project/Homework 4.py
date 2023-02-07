#!/usr/bin/env python
# coding: utf-8

# <div>
#     <img src="images/emlyon.png" style="height:60px; float:left; padding-right:10px; margin-top:5px" />
#     <span>
#         <h1 style="padding-bottom:5px;"> Python BootCamp </h1>
#         <a href="https://masters.em-lyon.com/en/msc-in-digital-marketing-data-science">[Emlyon]</a> MSc in Digital Marketing & Data Science (DMDS) <br/>
#          September 2022, Paris | © Saeed VARASTEH [RP] | Lucas VILLAIN
#     </span>
# </div>

# <div class="alert-info" style="border-bottom: solid 1px lightgray; background-color:#fff4e3;">
#     <img src="images/homework.png" style="height:60px; float:left; padding-right:10px;" />
#     <span style="font-weight:bold; color:#db9425">
#         <h4 style="padding-top:25px;"> HOMEWORK 04 </h4>
#     </span>
# </div>

# ### Homework 04 - Global Temperature
# 
# ---

# Let us implement a simplified formula for the increase in global temperature levels due to the radiative forcing of CO2 level changes.

# Radiative forcing due to change in CO2 level: $ \Delta F = \alpha * ln(\frac{c_1}{c_0}) $
# 
# Relation between radiative forcing and temperature: $ \lambda = \frac{\Delta T}{\Delta F} $
# 
# $\alpha$ is fixed at $5.35$ while $\lambda$ differs from model to model - we will simply use $0.5$.
# 
# $c_1$ denotes the changed CO2 level, $c_0$ denotes the unchanged CO2 level.
# 
# Let’s take the CO2 level of January 1970 as the unchanged CO2 level, so $c_0 = 325.03$.
# 
# Current levels of CO2 were at $c_1 = 411.97$ as of March 2019. We will just assume that the CO2 level has not changed significantly since then for the purposes of our calculations.
# 
# This would result in a $0.63 K$ increase in global temperature since 1970, which is consistent with the actual change in global temperature, especially considering that there are also other influences on the global climate such as other greenhouse gases.

# __Your Task__
# 
# 1. Calculate how many hours have passed since January 1st 1970 00:00:00.
# 2. Use this time difference to calculate the average CO2 increase per hour since 1970.
# 3. Use this CO2 increase per hour to calculate a projection of what the CO2 level could be in 2100 (assuming that the CO2 increase per hour stays constant).
# 4. Calculate the increase in temperature in from 1970 to 2100 (use your projected CO2 level as $c_1$ and the value from 1970 as $c_0$).
# 5. Now generalize steps 3. and 4. by writing a function "predict_increase" that takes an int year larger than 1970 as an input and returns the increase in temperature from 1970 to year.

# Hint: A year has on average 365.25 days.<br/>
# Hint: You can use `time` or `datetime` modules.

# In[ ]:


# your code

a = 5.35 
b = 0.5
c_0 = 325.03 
c_1 = 411.97 

import datetime 
import math 
time_1970 = datetime.datetime (1970, 1 ,1 )
time_now  = datetijme.datetime. now ()
daycount  = (time_now - time_1970). days
hours = daycount * 24 

Avg_co2 = (C_1 - C_0) / hours 


Def predict_increase(time):
    #co2 increase as C_1 
    time_target = datetime.datetime(time,1, 1)
    daycount2 = (time_target - time_1970) . days
    hours2 = dayscount2 * 24 
    increase = hours2 * avg_Co2
    C_2 = c_0 + increase 
    
    #Temperature increase as delta_t 
    delta_t = (a * math.log(c_2 / c_0)) * b
    return delta_t
    


# ---

# In[ ]:




