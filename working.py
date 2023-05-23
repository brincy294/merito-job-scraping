import requests
import sqlite3
from bs4 import BeautifulSoup
import pandas as pd

def insertVaribleIntoTable(Title, Company, Link,Mode,Experience, Location):
    try:
        sqliteConnection = sqlite3.connect('merito.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO jobs
                        (Title, Company, Link,Mode,Experience, Location ) 
                        VALUES (?, ?, ?, ?, ?,?);"""

        data_tuple = (Title, Company, Link,Mode,Experience, Location)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into jobs table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def extract(page):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'}
    urls=["https://www.shine.com/job-search/web-developer-jobs-{page}?q=Web%20Developer","https://www.iimjobs.com/search/web+developer-0-0-100-2.html","https://in.indeed.com/jobs?q=web+developer&l=pune&from=searchOnHP&vjk=96512a78b88e5456","https://www.naukri.com/web-developer-jobs","https://www.glassdoor.co.in/Job/pune-web-developer-jobs-SRCH_IL.0,4_IC2856202_KO5,18.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&typedLocation=&context=Jobs","https://www.instahyre.com/search-jobs/?company_size=0&isLandingPage=true&offset=0&search=true&skills=web+developer","https://www.foundit.in/srp/results?query=%22Web+Developer%22&queryEntity=web+developer%3Adesignation&searchId=71081996-89e0-41a2-ade7-85a7e9942a35"]
    for j in range(8):
        # if j==0:
        #     r=requests.get(urls[0],headers)
        #     soup=BeautifulSoup(r.content,'html.parser')
        #     divs=soup.find_all('div',class_='jobCard_jobCard__jjUmu')
        #     for item in divs:
        #         title=item.find('a').text.strip()
        #         company=item.find_next('span').find_next('span').find_next('span').text
        #         experience=item.find('div',class_='jobCard_jobCard_lists_item__YxRkV').text
        #         l=item.find('div',class_='jobCard_locationIcon__zrWt2').text
        #         s = ['[','@','_','!','#','$','%','^','&','*','(',')','<','>','?','/','|','}','{','~',':','1','2','3','4','5','6','7','8','9','0','+',']']  
        #         for i in s:
        #             location = l.replace(i, '')
        #         mode=item.find('li').text
        #         if mode=="Regular" or mode=="Remote" or mode=="Internship":
        #             mode=item.find('li').text
        #         else:
        #             mode=item.find_next('li').find_next('li').text
        #         insertVaribleIntoTable(title, company,'Not Found!!',mode,experience,location)
        #         print(title)
        #         print(company)
        #         print(experience)
        #         print(location)
        #         print(mode)
        #         print("\n")
        #         job={
        #             'title':title, 
        #             'company':company,
        #             'location':location,
        #             'mode':mode,
        #             'experience':experience
        #         }
        #         joblist.append(job)
        # if j==1:
        #     r=requests.get(urls[1],headers)
        #     soup=BeautifulSoup(r.content,'html.parser')
        #     divs=soup.find_all('div',class_='unfollowopt')
        #     for item in divs:
        #         titles=item.find('a').text.split("(")
        #         locations=item.find('span',class_='disp768').text
        #         location=locations.replace(" ", "")
        #         link=soup.find("a",{"class":"mrmob5"}).get("href")
        #         title=titles[0]
        #         exp=titles[1].split("yrs")
        #         experience=exp[0]
        #         insertVaribleIntoTable(title,'null',link,'Remote',experience,location)
        #         print(title)
        #         print(experience)
        #         print(location)
        #         print(link)
        #         print("\n")
        #         job={
        #             'title':title, 
        #             'experience':experience,
        #             'location':location,
        #             'link':link
        #         }
        #         joblist.append(job)

        if j==0:
            r=requests.get(urls[5],headers)
            soup=BeautifulSoup(r.content,'html.parser')
            divs=soup.find("div").children
            # divs=soup.find(class_='srpCardHeader')
            print(divs)
            # for item in divst
                
            
            return
joblist=[] 


if __name__=="__main__":
    extract(0)
    df = pd.DataFrame(joblist)
    print(df.head())
    df.to_csv('jobs.csv')
