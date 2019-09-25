# Reading the web page into Python
# Install requests: pip install requests
import requests
r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

# print the first 500 characters of the HTML
#print(r.text[0:500])

#Parsing the HTML using Beautiful Soup
# pip install beautifulsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

#Collecting all of the records
#<span class="short-desc"><strong>DATE</strong>LIE <span class="short-truth"><a href="URL">(EXPLANATION)</a></span></span>

results = soup.find_all('span', attrs={'class':'short-desc'})
# print len(results)
# print results[0:3]
# print results[-1]

# Extracting the date

first_result = results[0]
# print first_result

# print first_result.find('strong')

# print first_result.find('strong').text
# print first_result.find('strong').text[0:-1]
# print first_result.find('strong').text[0:-1] + ', 2017'

# Extracting the lie
#print first_result.contents
#print first_result.contents[1]
#print first_result.contents[1][1:-2]

# Extracting the explanation

#print first_result.contents[2]
#print first_result.find('a')
#print first_result.find('a').text[1:-1]

# Extracting the URL

#print first_result.find('a')['href']

# find(): searches for the first matching tag, and returns a Tag object
# findall(): searches for all matching tags, and returns a ResultSet object

# Extract info from a Tag object using two attributes:
# text: extracts the text of a Tag, and returns a string
# contents: extracts the children of a Tag, and returns a list of Tags and strings.

# Building the dataset
record = []
for result in results:
    date = result.find('strong').text[0:-1] + ', 2017'
    lie = result.contents[1][1:-2]
    explanation = result.find('a').text[1:-1]
    url = result.find('a')['href']
    record.append((date, lie, explanation, url))
#print len(record)
#print record[0:3]

# Applying a tabular data structure
import pandas as pd
df = pd.DataFrame(record, columns = ['date','lie','explanation','url'])
#print df.head()
#print df.tail()
df['date'] = pd.to_datetime(df['date'])
#print df.head()
#print df.tail()

# Exporting the dataset to a CSV file
df.to_csv('trump_lies.csv', index = False, encoding = 'utf-8')
# read csv file to df
df = pd.read_csv('trump_lies.csv', parse_dates=['date'],encoding = 'utf-8')