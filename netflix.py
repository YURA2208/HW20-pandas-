import pandas as pd
netflix_titles = pd.read_csv('netflix_titles.csv', delimiter=',', usecols=['release_year']).value_counts().reset_index()
netflix_titles.columns = ['year', 'count']
print(netflix_titles)
