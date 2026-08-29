import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

combined_df=pd.read_csv('combined_filtered.csv')
combined_df['log_emplvl']=np.log(combined_df['avg_emplvl'])
combined_df=combined_df.dropna(subset=['log_emplvl'])
combined_df['year_qtr']=combined_df['year'].astype(str)+'Q'+combined_df['qtr'].astype(str)

model=smf.ols(
    'log_emplvl~post+treatment:post+C(area_fips)+C(year_qtr)',
    data=combined_df
).fit(cov_type='cluster',cov_kwds={'groups':combined_df['area_fips']})
print(model.summary())

