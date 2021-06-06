'''ქვიზი 4. Dollskill საიტის კატეგორიებში მოვძებნე კატეგორია Sunglasses, რომელშიც სულ 3 გვერდია და ყოველ გვერდზე
სათვალეების სიაა. csv ფაილში გადმოვიტანე ინფორმაცია სათვალეების დასახელებებზე და ფასებზე. გავაკეთე ისე რომ ინფორმაცია
ინგლისურ ენაზე იყოს და ე.წ. დიაპაზონი შემდეგი გვერდზე გადასვლისას უდრიდეს 15 წამს, რომ სერვერმა არ დაგვბლოკოს. '''


import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

file = open('sunglasses.csv', 'w')
file.write('Title,Price\n')

p = {'p_':1}
url = 'https://www.dollskill.com/accessories/sunglasses.html'
h= {'Accept-Languange'='en-US'}

while p['p_']<=3:
    r = requests.get(url, params = p, headers=h)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    sunglasses = soup.find('div', class_='MuiGrid-root jss123 MuiGrid-container')
    all_sunglasses = sunglasses.find_all('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-sm-4 MuiGrid-grid-md-4 MuiGrid-grid-lg-3 MuiGrid-grid-xl-3')

    for each in all_sunglasses:
        title = each.find('h6', class_='MuiTypography-root jss212 MuiTypography-h6').text
        print(title)
        price = each.find('h6', class_='MuiTypography-root jss247 MuiTypography-h6').text
        print(price)
        file.write(title + ',' + price + '\n')

    p['p_'] += 1
    sleep(15)


