import pandas as pd
import numpy as np
import dropbox
import os

dbx = dropbox.Dropbox(os.environ['DROPBOX_API'])
dbx.users_get_current_account()

years = list(range(2002, 2020))
final_df = pd.DataFrame()

#downloading files from dropbox to one dataframe
for year in years:
    path= "/Saurav/data/Stage_Specific_Ranking_-_Table_data"
    _, res = dbx.files_download(path+str(year)+".csv")
    df=pd.read_csv(res.raw)
    final_df = pd.concat([df,final_df])

#selecting required columns
filtered_data = final_df.loc[:, ['Athlete/Comp','Metric', 'Score','Finish','Gender','Temp - Air','Judge 1 Score','Judge 2 Score',
                          'Judge 3 Score','Judge 4 Score','Judge 5 Score','Judge 6 Score - 1','Judge 7 Score - 1',
                          'Major Finalist','Major Medalist','Nation','Olympic Finalist','Olympic Medalist','Temp - Snow',
                          'Season','Season/Comp','Round','Wind']]

#getting age from yob
filtered_data['age_yrs'] = 2020 - final_df['yob']
filtered_data['Athlete_name'] =  final_df['Athlete/Comp'].str.extract(r"(.*-....).-", expand=False)

filtered_data = filtered_data.reset_index(drop = True)

#Updating old scores in same scale as new metric for scores before 2014
filtered_data['Metric'] = [round(filtered_data.loc[i,'Score']/30*100, 2) if filtered_data.loc[i, 'Metric'] != filtered_data.loc[i,'Score'] \
        else filtered_data.loc[i, 'Metric'] for i in range(len(filtered_data))]

# Dropping the scores column
filtered_data = filtered_data.drop(columns = ['Score'])

# filtering the final rounds only
filtered_data = filtered_data[filtered_data['Round'].str.lower().str.extract(r'.*(final).*', expand=False).notnull()]

# dividing competition data into 3 levels
tier1_df = filtered_data[filtered_data['Season_Comp'].str.lower().str.extract(r'.*(world).*', expand=False).notnull() |\
                 filtered_data['Season_Comp'].str.lower().str.extract(r'.*(olympics).*', expand=False).notnull()]

print("Number of rows in tier 1 = ", tier1_df.shape[0])

tier2_df = filtered_data[filtered_data['Season_Comp'].str.lower().str.extract(r'.*(north american).*', expand=False).notnull()]
print("Number of rows in tier 2 = ", tier2_df.shape[0])

tier3_df = filtered_data[filtered_data['Season_Comp'].str.lower().str.extract(r'.*(canad).*', expand=False).notnull()]
print("Number of rows in tier 3 = ", tier3_df.shape[0])

if tier1_df.shape[0]+tier2_df.shape[0]+tier3_df.shape[0] == filtered_data.shape[0]:
    print("Total # of rows match")
else:
    print("Rows mismatch")

# changing order and name of columns
tier1_df = tier1_df.loc[:, ['Athlete_Comp', 'Athlete_name', 'Gender', 'age_yrs', 'Nation', 'Judge_1_Score', 'Judge_2_Score', 
                    'Judge_3_Score', 'Judge_4_Score', 'Judge_5_Score', 'Judge_6_Score_1', 'Judge_7_Score_1', 'Major_Finalist',
                    'Major_Medalist', 'Olympic_Finalist', 'Olympic_Medalist','Temp_Snow', 'Temp_Air','Wind',
                    'Season', 'Season_Comp', 'Round', 'Metric', 'Finish']]

tier2_df= tier2_df.loc[:, ['Athlete_Comp', 'Athlete_name', 'Gender', 'age_yrs', 'Nation', 'Judge_1_Score', 'Judge_2_Score', 
                    'Judge_3_Score', 'Judge_4_Score', 'Judge_5_Score', 'Judge_6_Score_1', 'Judge_7_Score_1', 'Major_Finalist',
                    'Major_Medalist', 'Olympic_Finalist', 'Olympic_Medalist','Temp_Snow', 'Temp_Air','Wind',
                    'Season', 'Season_Comp', 'Round', 'Metric', 'Finish']]

tier3_df= tier3_df.loc[:, ['Athlete_Comp', 'Athlete_name', 'Gender', 'age_yrs', 'Nation', 'Judge_1_Score', 'Judge_2_Score', 
                    'Judge_3_Score', 'Judge_4_Score', 'Judge_5_Score', 'Judge_6_Score_1', 'Judge_7_Score_1', 'Major_Finalist',
                    'Major_Medalist', 'Olympic_Finalist', 'Olympic_Medalist','Temp_Snow', 'Temp_Air','Wind',
                    'Season', 'Season_Comp', 'Round', 'Metric', 'Finish']]

tier1_df = tier1_df.rename(columns = {'Athlete_Comp' : 'Athlete_Comp_ID', 'Finish' : 'Finish_Rank', 'Metric' : 'Score_Metric'})
tier2_df = tier2_df.rename(columns = {'Athlete_Comp' : 'Athlete_Comp_ID', 'Finish' : 'Finish_Rank', 'Metric' : 'Score_Metric'})
tier3_df = tier3_df.rename(columns = {'Athlete_Comp' : 'Athlete_Comp_ID', 'Finish' : 'Finish_Rank', 'Metric' : 'Score_Metric'})

# Dividing into men and women
tier1_df_M = tier1_df[tier1_df['Gender'] == "Men"]
tier1_df_W = tier1_df[tier1_df['Gender'] == "Women"]
tier2_df_M = tier2_df[tier2_df['Gender'] == "Men"]
tier2_df_W = tier2_df[tier2_df['Gender'] == "Women"]
tier3_df_M = tier3_df[tier3_df['Gender'] == "Men"]
tier3_df_W = tier3_df[tier3_df['Gender'] == "Women"]

# copying data into csv
tier1_df_M.to_csv("../data/tier_1_comp_data_men.csv", index = False)
tier2_df_M.to_csv("../data/tier_2_comp_data_men.csv", index = False)
tier3_df_M.to_csv("../data/tier_3_comp_data_men.csv", index = False)

tier1_df_W.to_csv("../data/tier_1_comp_data_women.csv", index = False)
tier2_df_W.to_csv("../data/tier_2_comp_data_women.csv", index = False)
tier3_df_W.to_csv("../data/tier_3_comp_data_women.csv", index = False)

print("data compilation successful!")