import pandas as pd
import numpy as np
import os

savepath = os.path.join('D:/', 'data', 'ess', '2018', 'ESS2018DK_trst-subset_clean.csv')
df = pd.read_csv(savepath)

trust_dict = {'Complete trust': 10, 'No trust at all': 0}
trustvars = ['trstprl', 'trstlgl', 'trstplc', 'trstplt', 'trstprt', 'trstep', 'trstun']

region_dict = {'DK01': 'Hovedstaden',
				'DK02': 'Sjælland',
				'DK03': 'Syddanmark',
				'DK04': 'Midtjylland',
				'DK05': 'Nordjylland'}

for trustvar in trustvars:
	df[trustvar] = df[trustvar].replace(trust_dict)

df['ppltrst'] = df['ppltrst'].replace({'Most people can be trusted': 10, 'You can\'t be too careful': 0, 'Don\'t know': np.nan})
df['region'] = df['region'].replace(region_dict)

df = df.replace({'Not applicable': np.nan, 'No answer': np.nan, 'Refusal': np.nan, 'Don\'t know': np.nan})

savepath = os.path.join('D:/', 'data', 'ess', '2018', 'ESS2018DK_trst-subset_clean.csv')
df.to_csv(savepath, index = False)