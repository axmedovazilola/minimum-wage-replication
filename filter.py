import zipfile 
import  pandas as pd

county_fips=['36013','36009','36003','36101','36015','36107','36007','36025',
               '42123','42083','42105','42117','42015','42115']

all_years_dfs=[]
for year in range(2011,2017):
    with zipfile.ZipFile(f"{year}_qtrly_by_area.zip")as z:
        names=z.namelist()
        matching_files=[n for n in names if any(fips in n for fips in county_fips)]
        for fname in matching_files:
            with z.open(fname) as f:
                df=pd.read_csv(f)
                all_years_dfs.append(df)
filtered_dfs=[]
for df in all_years_dfs:
    df=df[df['industry_code']=='722']
    df=df[df['own_code']==5]
    filtered_dfs.append(df)

combined_df=pd.concat(filtered_dfs,ignore_index=True)
combined_df['avg_emplvl']=combined_df[['month1_emplvl','month2_emplvl','month3_emplvl']].mean(axis=1)
combined_df['treatment']=combined_df['area_fips'].astype(str).str.startswith('36').astype(int)
combined_df['post']=(combined_df['year']>=2013).astype(int)

print(combined_df[combined_df['year']==2013][['area_fips','year','treatment','post']].head())