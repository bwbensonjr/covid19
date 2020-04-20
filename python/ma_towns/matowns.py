import pandas as pd
import numpy as np

def main():
    with open("covid-19-city-town-4-14-2020.txt") as f:
        lines = f.read().split("\n")[:-1]
    city_town = lines[::3]
    count = lines[1::3]
    rate = lines[2::3]
    ct = (pd.DataFrame({city_town[0]: city_town[1:-1],
                        count[0]: count[1:-1],
                        rate[0]: rate[1:-1]})
          .replace(to_replace={"Count": "<5", "Rate": "*"}, value=np.nan))
    ct["Count"] = ct["Count"].astype(float)
    ct["Rate"] = ct["Rate"].astype(float)
    ct.to_csv("ma_covid_positives_by_town_2020_04_15.csv", index=False)

def visualize():
    ct = pd.read_csv("ma_covid_positives_by_town_2020_04_15.csv")
    plot_dist(ct)

def plot_dist(ct):
    ax = sns.distplot(ct["Rate"], kde=False)
    ax.set_title("MA Municipality COVID-19 Rate")
    ax.set_ylabel("Municipality Count")
    ax.set_xlabel("Rate (cases per 100,000 residents)")
    ax.text(1830, 2.5, "Chelsea", rotation=90)
    ax.text(1205, 2.5, "Brockton", rotation=90)
    ax.text(1073, 2.5, "Randolph", rotation=90)
    ax.text(960, 2.5, "Williamstown", rotation=90)
    ax.text(890, 3.5, "Lawrence, Everett", rotation=90)
    ax.text(824, 2.5, "Longmeadow", rotation=90)
    return ax
