import pandas as pd

df1=pd.read_csv('./data/article_2022-02-14.csv')
df2=pd.read_csv('./data/article_2022-02-16.csv')
df3=pd.read_csv('./data/article_2022-02-17.csv')
df4=pd.read_csv('./data/article_2022-02-22.csv')

df= pd.concat([df1,df2,df3,df4],ignore_index=True)
df.to_csv(
        "./data/article.csv",index=False)