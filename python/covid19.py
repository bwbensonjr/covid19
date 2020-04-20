import pandas as pd

ID_COLS = [
    "date",
    "dateChecked",
    "state",
    "fips",
    "hash",
]

VALUE_COLS = [
    "positive",
    "negative",
    "pending",
    "hospitalizedCurrently",
    "hospitalizedCumulative",
    "inIcuCurrently",
    "inIcuCumulative",
    "onVentilatorCurrently",
    "onVentilatorCumulative",
    "recovered",
    "death",
    "hospitalized",
    "total",
    "totalTestResults",
    "posNeg",
    "deathIncrease",
    "hospitalizedIncrease",
    "negativeIncrease",
    "positiveIncrease",
    "totalTestResultsIncrease",
]

def main():
    sv = (pd.read_csv("https://covidtracking.com/api/v1/states/daily.csv",
                      parse_dates=["date", "dateChecked"])
          .melt(id_vars=ID_COLS, value_vars=VALUE_COLS))
    sns.bartplot(x="date", y="value", data=sv.query("state == 'MA'").query("variable == 'deathIncrease'"))
