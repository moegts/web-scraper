import requests # IMPORT IT TO GET HTML DATA WITH IT
from bs4 import BeautifulSoup # TO HELP YOU FILTER THE HTML DATA AND ORGNIZE IT


def get_citations_needed_count(URL): # FUNC TO PARSE MULTI LINKS TO IT
    page = requests.get(URL) # REQ DATA FROM URL // RES WILL BE 200
    soup = BeautifulSoup(page.content, 'html.parser') # GET THE REAL CONTENT WITH THIS LINE
    result = soup.findAll(text='citation needed') # HERE WE DEFINE THE THING WE WANT 
    return len(result) # TO GET HOW MUCH ITEAMS THERE WE FIND


def get_citations_needed_report(URL):
    page = requests.get(URL) # REQ DATA FROM URL // RES WILL BE 200
    soup = BeautifulSoup(page.content, 'html.parser').findAll('p') # GET THE REAL CONTENT WITH THIS LINE AND FIND ALL P ONLY
    report = [] 
    for i in soup:
        a_exist = i.findAll('a', title="Wikipedia:Citation needed")
        if a_exist:
            report.append(i.text)
            report += '\n'
            print(f'The paragraph : {i.text}')
            print("🔵"*44)
    return (report)


if __name__ == "__main__":
    get_citations_needed_count(
        'https://en.wikipedia.org/wiki/History_of_Jordan')
    get_citations_needed_count(
        'https://en.wikipedia.org/wiki/History_of_Mexico')
    get_citations_needed_report(
        'https://en.wikipedia.org/wiki/History_of_Mexico')
    get_citations_needed_count(
        'https://en.wikipedia.org/wiki/History_of_chocolate')
    get_citations_needed_report(
        'https://en.wikipedia.org/wiki/History_of_chocolate')
    get_citations_needed_report(
        'https://en.wikipedia.org/wiki/History_of_Jordan')
