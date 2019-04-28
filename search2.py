from selenium import webdriver
from bs4 import BeautifulSoup
import sqlite3
import sys
import urllib.request
n = 3
conn = sqlite3.connect('topic100.sqlite')  #데이베이스 생성
cur = conn.cursor()


#cur.execute("CREATE TABLE Topic(Name text, Date text);")
cur.execute("CREATE TABLE Topic(Name text);")



#path="chromedriver"
#driver = webdriver.Chrome(path)
#driver.get("https://github.com/login")


#driver.find_element_by_name('login').send_keys('kimtuyer@naver.com')

#driver.find_element_by_name('password').send_keys('hyer3078')
#driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[4]').click()

#driver.get("https://github.com/topics/python")
#driver.get("https://github.com/search?p=4&q=python&type=Repositories")


#req=driver.page_source
#soup=BeautifulSoup(req,'html.parser')
#b=1



#driver.find_element_by_xpath('/html/body/div[4]/main/div/div[2]/div[1]/form/button').click()

whole_source = ""
#for page_number in range(1, 10):
	#URL = 'https://github.com/search?q=python&type=Repositories&p=' + str(page_number)
	#response = requests.get(URL)
#whole_source = whole_source + response.text
#soup = BeautifulSoup(whole_source, 'html.parser')




#for link in soup.find_all('a', class_="topic-tag topic-tag-link f6 my-1"):
      #  a = link.get('href')
       # s = a[8:]
       # sql = "insert into Topic(Name) values(?)"
       # cur.execute(sql, (s,))

#################################################################
pagenum="https://github.com/search?o=desc&p="

keword='&q='

Rest='&s=stars&type=Repositories'


def get_link_from_search(page_num,URL):


    for i in range(page_num):
     current_page_num = 1 + i
     position = URL.index('p=')
     URL_with_page_num = URL[: position + 2] + str(current_page_num) \
                    + URL[position + 2:]
     source_code_from_URL= urllib.request.urlopen(URL_with_page_num)
     soup = BeautifulSoup(source_code_from_URL, 'lxml'
                    )
     for link in soup.find_all('a', class_="topic-tag topic-tag-link f6 my-1"):
      a = link.get('href')
      s = a[8:]
      sql = "insert into Topic(Name) values(?)"
      cur.execute(sql, (s,))

def main(argv):
    #if len(argv) != 3:
       # print("python [모듈이름] [키워드] [가져올 페이지 숫자] ")
        #return
    print("검색할 키워드 입력")
    #keyword = argv[1]
    keyword=input()
    print("검색할 페이지 입력")
    page_num=int(input())

    #page_num = int(argv[2])
    target_URL = pagenum + keword + keyword + Rest

    get_link_from_search(page_num, target_URL)

if __name__ == '__main__':
    main(sys.argv)


conn.commit()
conn.close()






   # for link2 in soup.find_all('p',class_="f6 text-gray mr-3 mb-0 mt-2"): 날짜정보 가져오려고

       # time1 = link2.get('datetime')
       # ss=str(time1)
       # t1 = ss[0:9]
       # print(t1)






#for link3 in soup.find_all('div', class_="d-flex d-md-inline-block pagination"): #topic에서 loadmore 하려고
   #page=link3.get('href')
#driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/div[3]/div/a[2]').click()
#'https://github.com/search?q=python&type=Repositories&p='




