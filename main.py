import twint
import pandas as pd


usernames=pd.read_excel('username.xlsx').usernames.map(lambda x: x.lstrip('@')).values


for username in usernames:
    c = twint.Config()
    c.Username = username
    c.Since='2020-03-01 01:00:00'
    c.Store_csv = True
    c.Output = 'CSVs/{}.csv'.format(username)
    twint.run.Search(c)
