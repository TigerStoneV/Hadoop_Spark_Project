from datetime import datetime,timedelta
from selenium import webdriver as wd
import pandas as pd
import warnings
import time
warnings.filterwarnings(action='ignore')
def crawling_olympic():
    chrome_options = wd.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('headless')
    time1 = datetime(2022, 2, 17)
    time2 = datetime.today()

    link = 'https://m.sports.naver.com/beijing2022/news/index?disciplineId=&date='
    events = ['SSK','CUR','ALP','SBD','SJP','LUG','BTH','IHO','BOB','CCS','STK','FSK','FRS','NCB','SKN']

    now = datetime.now()
    print("{}크롤링 시작".format(now.strftime('%Y-%m-%d %H:%M')))
    df = pd.DataFrame()
    for i in range((time2-time1).days+1):
        for event in events:
            t = time1+timedelta(days=i)
            date=t.strftime("%Y-%m-%d")
            print("{} / 크롤링 시작".format(date))
            link_data = 'https://m.sports.naver.com/beijing2022/news/index?disciplineId='+event+'&date='+str(date)+'&sort=latest'

            driver = wd.Chrome("./chromedriver", options=chrome_options)
            driver.get(link_data)
            count = 0
            while count<10:
                try:
                    driver.find_element_by_css_selector('#content > div > div.News_main_section__1b-Va > div.news_group.News_comp_general_news__20mc- > div > div.GroupMore_group_more_area__2ghuH > button').click()
                    count+=1
                except:
                    break
            try:
                article_title_code=driver.find_element_by_css_selector('#content > div > div.News_main_section__1b-Va > div.news_group.News_comp_general_news__20mc- > div > div.news_list_area > ul')
                j=1
                time.sleep(2)
                while True:

                    try:
                        tp = '//*[@id="content"]/div/div[2]/div[1]/div/div[2]/ul/li[' + str(j) + ']/a/div[2]/em'
                        df = df.append({
                            'date':date,
                            'article_title':article_title_code.find_element_by_xpath(tp).text,
                            'event':event
                        },ignore_index=True
                        )
                        j+=1
                    except:
                        try:
                            tp = '//*[@id="content"]/div/div[2]/div[2]/div/div[2]/ul/li[' + str(j) + ']/a/div[2]/em'
                            df = df.append({
                                'date': date,
                                'article_title': article_title_code.find_element_by_xpath(tp).text
                            }, ignore_index=True
                            )
                            j += 1
                        except:
                            break
                driver.quit()
            except:
                driver.quit()

            msg1 = "{} : 총 {}개의 정보 수집 완료".format(now.strftime('%Y-%m-%d %H:%M'), len(df))
            print(msg1)
            time.sleep(2)
    df.to_csv(
        "./data/article_{}.csv".format(now.strftime('%Y-%m-%d')),index=False)

if __name__ == '__main__':
    crawling_olympic()