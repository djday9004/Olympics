
"""
Created on Mon Feb 22 13:11:53 2021

@author: dennis.day
"""

import pandas as pd

file_location = 'athlete_events.csv'

oly_df = pd.read_csv(file_location)

oly_df.info()

oly_df.apply(lambda x: sum(x.isnull()), axis = 0)

basketball_gold = oly_df[((oly_df['Event'] == "Basketball Men's Basketball") & (oly_df['Medal'] == 'Gold'))]
basketball_gold.info()
basketball_gold[["Year", "Team", "Medal"]].drop_duplicates().sort_values("Year")

oly_df[oly_df["Medal"]!= 'N/A'].groupby(["Name", "Team", "Sport"])["Medal"].count().nlargest(20)
