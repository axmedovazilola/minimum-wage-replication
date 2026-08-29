import matplotlib.pyplot as plt
import pandas as pd

combined_df=pd.read_csv('combined_filtered.csv')
pretrend=combined_df[combined_df['post']==0].groupby(['year','qtr','treatment'])['avg_emplvl'].mean()
pretrend=pretrend.unstack('treatment')
first_row=pretrend.iloc[0]
indexed=(pretrend/first_row)*100
indexed.plot()
plt.show()