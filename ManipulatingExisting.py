import pandas
from fuzzywuzzy import process

dirtydata_df = pandas.read_csv('DirtyData.csv')
knownlist_df = pandas.read_csv('https://raw.githubusercontent.com/click-here/Power-BI-and-Python/master/KnownList.csv',encoding='ISO-8859-1')

known_companies = list(knownlist_df['Security'])


def get_cleaned_company(company):
    return process.extractOne(company, known_companies)[0]

dirtydata_df['Cleaned Companies'] = dirtydata_df['Security'].map(lambda a: get_cleaned_company(a))

