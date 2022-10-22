import datetime
import get_weather as gw

dt_now = datetime.datetime.now()

conditions = {"season":{"spring":[3,4,5],"summer":[6,7,8],"fall":[9,10,11],"winter":[12,1,2]},"time":{"morning":[5,6,7,8,9,10],"noon":[11,12,13,14],"evening":[15,16,17,18],"night":[19,20,21,22,23,24,1,2,3,4]},"weather":""}
# condition = ["season","time","weather"]
now_list = []

for condition in conditions:
    # now = ""
    date = ""
    if conditions[condition]:
        if condition == "season":
            date = dt_now.month
        else:
            date = dt_now.hour
        for key in conditions[condition]:
            if date in conditions[condition][key]:
                now_list.append(key)
    else:
        now_list.append(gw.return_weather())