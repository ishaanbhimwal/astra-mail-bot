from datetime import datetime, timedelta

import pytz

# use "special holidays" instead
my_dict = {
    "September": {
        0: {"Name": "Saturday", "Day": "10-09"},
        1: {"Name": "Sunday", "Day": "11-09"},
        2: {"Name": "Monday", "Day": "12-09"},
        3: {"Name": "Tuesday", "Day": "13-09"},
        4: {"Name": "Wednesay", "Day": "14-09"},
        5: {"Name": "Thursday", "Day": "15-09"},
        6: {"Name": "Friday", "Day": "16-09"},
        7: {"Name": "Saturday", "Day": "17-09"},
        8: {"Name": "Sunday", "Day": "18-09"},
        9: {"Name": "Monday", "Day": "19-09"},
        10: {"Name": "Tuesday", "Day": "20-09"},
        11: {"Name": "Wednesday", "Day": "21-09"},
        12: {"Name": "Thursday", "Day": "22-09"},
        13: {"Name": "Friday", "Day": "23-09"},
        14: {"Name": "Saturday", "Day": "24-09"},
        15: {"Name": "Sunday", "Day": "25-09"},
        16: {"Name": "Monday", "Day": "26-09"},
        17: {"Name": "Tuesday", "Day": "27-09"},
        18: {"Name": "Wednesday", "Day": "28-09"},
        19: {"Name": "Thursday", "Day": "29-09"},
        20: {"Name": "Friday", "Day": "30-09"},
    },
    "October": {
        0: {"Name": "Saturday", "Day": "01-10"},
        1: {"Name": "Gandhi Jayanti", "Day": "02-10"},
    },
}

datetime_india = datetime.now(pytz.timezone("Asia/Kolkata"))

date_month_advance = (datetime_india.today() + timedelta(days=7)).strftime("%d-%m")

month_current = datetime_india.today().strftime("%B")
month_advance = (datetime_india.today() + timedelta(days=30)).strftime("%B")
month_list = [month_current, month_advance]


def calc_res():
    for month in month_list:
        if month in my_dict:
            for i in my_dict[month]:
                if date_month_advance == my_dict[month][i]["Day"]:
                    # modify the format of the message
                    result = f"{my_dict[month][i]['Name']} is on {my_dict[month][i]['Day']}. Hurry up!\n\nTime right now - {datetime_india.strftime('%a %_d %b, %I:%M %p')}"
                    return result
