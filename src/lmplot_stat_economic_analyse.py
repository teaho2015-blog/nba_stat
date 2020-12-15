import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import *
from src.table import *
from src.util import takeWin, takeGDP

sns.set_theme(style="ticks")

display_dict = {
    'dataset': [],
    'x': [],
    'y': []
}

session = Session_class()
for year in range(2001, 2017):
    result = session.execute(
        "select DISTINCT ts.id, ts.team_id, ts.`year`, ts.win, ts.loss, t.city_id, cg.gdp from team_stats ts, team t, city_gdp cg where ts.team_id = t.id and cg.city_id = t.city_id and ts.`year` = {0} and cg.year = {1}".format(year, year))
    lr = list(result)

    print("List : ", lr)

    result_dict = {}
    for row in lr:
        result_dict.setdefault(row['team_id'], {})

    print(result_dict)
    # get wins sort
    lr.sort(key=takeWin)
    for i, row in enumerate(lr):
        result_dict.get(row['team_id'])['stat_level'] = i + 1

    # get gdp sort
    lr.sort(key=takeGDP)
    for i, row in enumerate(lr):
        result_dict.get(row['team_id'])['gdp_level'] = i + 1

    print(result_dict)

    for elem in result_dict:
        display_dict['dataset'].append(year)
        display_dict['x'].append(result_dict[elem]['stat_level'])
        display_dict['y'].append(result_dict[elem]['gdp_level'])

# print the final display data
print(json.dumps(display_dict, indent=2, ensure_ascii=False))

#show data
df = pd.DataFrame(display_dict)
df.head()
# Show the results of a linear regression within each dataset
fig = sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
           col_wrap=4, ci=None, palette="muted", height=4,
           scatter_kws={"s": 50, "alpha": 1})
fig.savefig('{save_path}', dpi=400)

plt.show()
