from datetime import datetime
import re
from easymoney.money import EasyPeasy
ep = EasyPeasy()
import warnings

warnings.filterwarnings('ignore')


def clean_countries(x):
    result = None
    if isinstance(x, str):
        x = re.sub(',[^\n]*', '', x)
        if x == "UK":
            result = "United Kingdom"
        elif x in ["Soviet Union", "Russia"]:
            result = "RU"
        elif x in ["South Korea"]:
            result = "KR"
        elif "Germany" in x:
            result = "Germany"
        else:
            result = x

    elif isinstance(x, list):
        result = x[0]

    return result


def clean_dates(x):
    if isinstance(x, str):
        x = re.sub('([A-z$.,\s])+', '', x)
        if len(x) == 4:
            x += "-01-01"
        return datetime.strptime(x, '%Y-%m-%d')
    else:
        return x


def clean_currency(x, column):
    val = x[column]

    if isinstance(val, str):
        amt = re.sub('([A-z$.,\s])+', '', val)
        cur_type = re.sub('([\d.,\s])+', '', val)

        if cur_type in ['USD', '$']:
            reg = "US"
        else:
            reg = x["country"]

        try:
            return round(ep.normalize(amount=int(amt),
                                      region=reg,
                                      from_year=int(x["year"]),
                                      base_currency="USD"), 2)
        except:
            # print("amount is "+amt, x["date_published"].year, x["country"])
            return None
    return (val)