import pandas as pd
import numpy as np
import os

datapath = os.path.join('D:/', 'data', 'ess', '2018', 'ESS2018DK.csv')
df = pd.read_csv(datapath, low_memory = False)

vars_set1 = ['idno', 'cntry', 'ppltrst', 'trstprl', 'trstlgl', 'trstplc', 'trstplt', 'trstprt', 'trstep', 'trstun']
vars_set2 = ['idno','gndr','agea','region','prtvtddk','edlvddk','infqbst','grspnum']
vars_all = (vars_set1 + vars_set2[1:len(vars_set2)])

df_all = df.loc[:, vars_all]
df_set1 = df.loc[:, vars_set1]
df_set2 = df.loc[:, vars_set2]

savepath_set1 = os.path.join('D:/', 'data', 'ess', '2018', 'ESS2018DK_trst-subset_raw.csv')
savepath_set2 = os.path.join('D:/', 'data', 'ess', '2018', 'ESS2018DK_bcg-subset_raw.csv')

df_set1.to_csv(savepath_set1)
df_set2.to_csv(savepath_set2)

trust_dict = {'Complete trust': 10, 'No trust at all': 0}
trustvars = ['trstprl', 'trstlgl', 'trstplc', 'trstplt', 'trstprt', 'trstep', 'trstun']

region_dict = {'DK01': 'Hovedstaden',
               'DK02': 'Sjælland',
               'DK03': 'Syddanmark',
               'DK04': 'Midtjylland',
               'DK05': 'Nordjylland'}

for trustvar in trustvars:
	df_all[trustvar] = df_all[trustvar].replace(trust_dict)

df_all['ppltrst'] = df_all['ppltrst'].replace({'Most people can be trusted': 10, 'You can\'t be too careful': 0, 'Don\'t know': np.nan})
df_all['region'] = df_all['region'].replace(region_dict)

df_all = df_all.replace({'Not applicable': np.nan, 'No answer': np.nan, 'Refusal': np.nan, 'Don\'t know': np.nan})

savepath_all = os.path.join('D:/', 'data', 'ess', '2018', 'ESS2018DK_trst-subset_clean.csv')
df_all.to_csv(savepath, index = False)