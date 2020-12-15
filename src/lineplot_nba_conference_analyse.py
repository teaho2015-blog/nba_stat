import json
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from sqlalchemy import *
from src.table import *
from src.util import takeWin, takeGDP

sns.set_theme(style="ticks")
session = Session_class()

display_dict = {
    'conference': [],
    'year': [],
    'win_difference': []
}

for year in range(2001, 2017):
    data = session.query(TeamStats).filter(TeamStats.year == year).all()
    west_win_difference = 0
    east_win_difference = 0
    for elem in data:
        if elem.conference_id == 'west':
            west_win_difference += (elem.win - elem.loss)
        if elem.conference_id == 'east':
            east_win_difference += (elem.win - elem.loss)

    logging.info('year:{0}, west_win_difference:{1}, east_win_difference:{2}'.format(year, west_win_difference, east_win_difference))

    display_dict['conference'].append('west')
    display_dict['year'].append(year)
    display_dict['win_difference'].append(west_win_difference)

    display_dict['conference'].append('east')
    display_dict['year'].append(year)
    display_dict['win_difference'].append(east_win_difference)

logging.info(display_dict)

df = pd.DataFrame(display_dict)
df.head()

sns_plot = sns.lineplot(data=df, x="year", y="win_difference", hue="conference")
fig = sns_plot.get_figure()
fig.savefig('{save_path}', dpi=400)

plt.show()
