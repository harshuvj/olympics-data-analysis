# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading 
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'],'Both',data['Better_Event'])
#better_event =data['Better_Event'].value_counts()

# Summer or Winter
better_event =data['Better_Event'].value_counts()
better_event = better_event.index[0]
print(better_event)

# Top 10

top_countries = data.loc[:,['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(index=146,inplace=True)

def top_ten(df, col):
    country_list = []
    top=df.nlargest(10,col)
    country_list =list(top['Country_Name'])
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')


cm1= set(top_10_summer).intersection(set(top_10_winter))
cm = cm1.intersection(set(top_10))

common =list(cm)
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

# Plotting top 10
fig = plt.figure(figsize=(15,7))
x=summer_df['Country_Name']
y=summer_df['Total_Medals']
plt.bar(x,y)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=13)
plt.xlabel(' Top 10 Countries in Summer Olympics ', fontsize=15)
plt.ylabel(' Total Medals won ', fontsize=15)
plt.show()

fig = plt.figure(figsize=(15,7))
x=winter_df['Country_Name']
y=winter_df['Total_Medals']
plt.bar(x,y)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=13)
plt.xlabel(' Top 10 Countries in Summer Olympics ', fontsize=15)
plt.ylabel(' Total Medals won ', fontsize=15)
plt.show()

fig = plt.figure(figsize=(15,7))
x=top_df['Country_Name']
y=top_df['Total_Medals']
plt.bar(x,y)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=13)
plt.xlabel(' Top 10 Countries in Summer Olympics ', fontsize=15)
plt.ylabel(' Total Medals won ', fontsize=15)
plt.show()
# Top Performing Countries
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = round(summer_df['Golden_Ratio'].max(),2)
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax()][0]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = round(winter_df['Golden_Ratio'].max(),2)
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax()][0]

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = round(top_df['Golden_Ratio'].max(),2)
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax()][0]
# Best in the world 
data1 = data.drop(index=146)
data1['Total_Points'] = data1['Gold_Total']*3 +data1['Silver_Total']*2 + data1['Bronze_Total']
most_points = data1['Total_Points'].max()
best_country=data1.loc[data1['Total_Points'].idxmax()][0]

best = data[data['Country_Name']==best_country]
best = best.loc[:,['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.xticks(rotation=45)
plt.ylabel('Medals Tally')


# Plotting the best



