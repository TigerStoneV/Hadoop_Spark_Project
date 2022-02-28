from konlpy.tag import Hannanum
import pandas as pd
import re
import warnings
import datetime
warnings.filterwarnings(action='ignore')

now = datetime.datetime.now()

df = pd.read_csv('./data/article.csv')

list_csv = pd.DataFrame()
hannanum = Hannanum()

for i in range(len(df["article_title"])):
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#‥$·‧”‘’∼⓵⓶①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑮⑯→%“…&\\\=\(\'\"\♥\♡\ㅋ\ㅠ\ㅜ\ㄱ\ㅎ\ㄲ\ㅡ]', ' ', df["article_title"][i])
    list_csv=list_csv.append({
        "date" : df["date"][i],
        "event": df["event"][i],
        "nouns" : hannanum.nouns(cleaned_text)
    },ignore_index=True)
list_csv.to_csv(
    "./data/nouns_{}.csv".format(now.strftime('%Y-%m-%d')),index=False)
# list_csv.to_csv(
#     "./data/nouns_{}.csv".format("2022-02-14"),index=False)