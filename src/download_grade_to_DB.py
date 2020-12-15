import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

from src.table import *


team_dict = {
    "Philadelphia 76ers": 9,
    "Miami Heat": 3,
    "New York Knicks": 8,
    "Orlando Magic": 4,
    "Boston Celtics": 6,
    "New Jersey Nets": 7,
    "Washington Wizards": 5,
    "Milwaukee Bucks": 15,
    "Toronto Raptors": 10,
    "Charlotte Hornets": 2,
    "Indiana Pacers": 14,
    "Detroit Pistons": 13,
    "Cleveland Cavaliers": 12,
    "Atlanta Hawks": 1,
    "Chicago Bulls": 11,
    "San Antonio Spurs": 20,
    "Utah Jazz": 25,
    "Dallas Mavericks": 16,
    "Minnesota Timberwolves": 22,
    "Houston Rockets": 17,
    "Denver Nuggets": 21,
    "Vancouver Grizzlies": 32,
    "Los Angeles Lakers": 28,
    "Sacramento Kings": 30,
    "Phoenix Suns": 29,
    "Portland Trail Blazers": 24,
    "Seattle SuperSonics": 31,
    "Los Angeles Clippers": 27,
    "Golden State Warriors": 26,
    "Oklahoma City Thunder": 23,
    "New Orleans Pelicans": 19,
    "New Orleans Hornets": 19,
    "Charlotte Bobcats": 2,
    "Memphis Grizzlies": 18,
    "Brooklyn Nets": 33,
    "New Orleans/Oklahoma City Hornets": 19
}

url_pattern = 'https://www.basketball-reference.com/leagues/NBA_{0}.html'

for i in range(2001, 2017):
    req = urllib.request.Request(url_pattern.format(i))
    with urllib.request.urlopen(req) as res:
        print(res.getheaders())
        html_str = res.read().decode('utf-8')

        # BeautifulSoup：解析页面
        # lxml：解析器
        soup = BeautifulSoup(html_str, 'lxml')
        # 东部
        elems = soup.select('table.stats_table#divs_standings_E tr.full_table')

        # print(type(elems))
        # print(len(elems))
        print('year: %d' %i)
        for elem in elems:
            team_name = elem.find(attrs={'data-stat': "team_name"}).select('a')[0].text
            wins = elem.find(attrs={'data-stat': "wins"}).text
            losses = elem.find(attrs={'data-stat': "losses"}).text
            print('team_name:{0}, team_id:{1}, conference:{2}, wins:{3}, losses:{4}'.format(team_name,
                                                                                            team_dict.get(team_name),
                                                                                            'east', wins, losses))
            stmt = t_team_stats.insert(values=dict(team_id=team_dict.get(team_name), year=i, win=wins, loss=losses, conference_id='east'))
            stmt.execute()


        # 西部
        elems = soup.select('table.stats_table#divs_standings_W tr.full_table')
        for elem in elems:
            team_name = elem.find(attrs={'data-stat': "team_name"}).select('a')[0].text
            wins = elem.find(attrs={'data-stat': "wins"}).text
            losses = elem.find(attrs={'data-stat': "losses"}).text
            print('team_name:{0}, team_id:{1}, conference:{2}, wins:{3}, losses:{4}'.format(team_name,
                                                                                            team_dict.get(team_name),
                                                                                            'west', wins, losses))
            stmt = t_team_stats.insert(values=dict(team_id=team_dict.get(team_name), year=i, win=wins, loss=losses, conference_id='west'))
            stmt.execute()

class DataError(Exception):
    pass
