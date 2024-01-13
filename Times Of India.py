import sys
import subprocess
from bs4 import BeautifulSoup
import requests
import re
from Send_email import Send_email
#print(subprocess.__doc__)
URL = "https://economictimes.indiatimes.com/"
data = requests.get(URL).text
soup = BeautifulSoup(data,'lxml')
TotalNews = 0
need = "https://economictimes.indiatimes.com"
dict_data = {}
content = soup.find("ul",class_ = "newsList clearfix" )
def news():
    global TotalNews, dict_data
    for i in content:
        try:
            link = need+i.a["href"]
            text = i.get_text() 
            dict_data[text] = link
            #print(text, "\n", link )
            TotalNews += 1
        except:
            print("problem")
    return dict_data
print(f"Total News are{TotalNews}")

if __name__ == '__main__':
    really_news = news()
    if really_news:
        message = "Subject: TODAY NEWS on ECONOMICS TIME\n\n"
        for i in dict_data:
            message += f"{i}\n {dict_data[i]} \n\n"
    Send_email(message)
        
sys.help   
    

