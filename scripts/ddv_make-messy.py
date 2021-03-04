import pandas as pd
import os

datapath = os.path.join("..", "datasets", "DDV_2017_redux.csv")
ddv_df = pd.read_csv(datapath)

likert_freq = {1: 'Hver dag', 2: 'Flere gange om ugen', 3: 'En eller to gange om ugen', 4: 'Sjældent', 5: 'Aldrig', 8: 'Ved ikke', 9: 'Uoplyst'}
freq_qs = ['v216', 'v217', 'v218', 'v219']

for v in freq_qs:
    ddv_df[v] = ddv_df[v].replace(likert_freq)
    
likert_goodbad = {1: "Godt", 2: "Dårligt", 3: "Ligegyldigt", 8: "Ved ikke", 9: "Uoplyst"}
goodbad_qs = ['v121', 'v122']

for v in goodbad_qs:
    ddv_df[v] = ddv_df[v].replace(likert_goodbad)
    
likert_trust = {1: 'Meget stor tillid', 2: 'Ret stor tillid', 3: 'Ikke særlig stor tillid', 4: 'Slet ingen tillid', 8: 'Ved ikke', 9: 'Uoplyst'}
trust_qs = ['v123', 'v132']

for v in ddv_df.loc[:, 'v123':'v132'].columns:
    ddv_df[v] = ddv_df[v].replace(likert_trust)
    

ddv_qs = ddv_df.loc[:, 'v57':'v224']
ddv_bcg = ddv_df.loc[:, 'v297_dk':'folkekirken']

ddv_qs = ddv_qs.join(ddv_df.loc[:, 'ipnr17'])
ddv_bcg = ddv_bcg.join(ddv_df.loc[:, 'ipnr17'])

ddv_qs = ddv_qs.loc[:, ['ipnr17'] + [ col for col in ddv_qs.columns if col != 'ipnr17' ]]
ddv_bcg = ddv_bcg.loc[:, ['ipnr17'] + [ col for col in ddv_bcg.columns if col != 'ipnr17' ]]


ddv_qs.to_csv('../datasets/DDV2017_redux_qs.csv')
ddv_bcg.to_csv('../datasets/DDV2017_redux_bcg.csv')