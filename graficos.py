import pandas as pd
import plotly.express as px

long_df = px.data.medals_long()
#print(long_df.head())

#fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
#fig.show()

wide_df = px.data.medals_wide()
#print(wide_df.head())

#fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")
#fig.show()

geo = pd.read_csv("./geoMap.csv", header=0, names=['pais', '2020', '2019'])
print(geo.info())
geo.dropna(inplace=True)
print(geo.info())
geo['2020'] = geo['2020'].apply(lambda x: int(x[:2]))
geo['2019'] = geo['2019'].apply(lambda x: int(x[:2]))
print(geo.info())
print(geo.head())

fig = px.bar(geo, x="pais", y=["2019", "2020"], title="Atendimentos")
fig.show()