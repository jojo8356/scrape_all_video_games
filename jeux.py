from bs4 import BeautifulSoup as bs
import requests as r,time,requests

remove_duplicates = lambda original_list: list(set(original_list))
affiche = lambda liste: [print(i, element.text) for i, element in enumerate(liste)]

consoles_select = ['Dreamcast','Famicom','Game Boy','Game Boy Advance','Game Boy Color','GameCube','Linux','Master System','Mega Drive','par navigateur','Nintendo 3DS','Nintendo 64','Nintendo DS','Nintendo Entertainment System','Nintendo Switch','PlayStation','PlayStation 2','PlayStation 3','PlayStation 4','PlayStation 5','PlayStation Portable','PlayStation Vita','Super Famicom','Super Nintendo','Wii','Wii U','Windows (0-9)','Xbox','Xbox 360','Xbox One','Xbox Series']

start = time.time()

jeux = []
liens = []
console = []
indexes = [1, 6, 9]
urls = []

response = r.get("https://fr.wikipedia.org/wiki/Liste_de_jeux_vid%C3%A9o")
soup = bs(response.content, 'lxml')
consoles = soup.find("div", {"id": "mw-content-text"}).find_all("ul")

for index in indexes:
    for x in consoles[index].find_all("li"):
        console.append(x.find("a"))

for x in console:
    liens.append(x["href"]) if ("title" in x and x["title"].replace("Liste de jeux ","") in consoles_select) else None

for x in range(len(liens)):
    if "/wiki/" in liens[x]:
        liens[x] = "https://fr.wikipedia.org"+liens[x]

def get_links(url_index, tbody_index, td_index, td_check_index=None, td_check_value=None):
    response = r.get(liens[url_index])
    soup = bs(response.content, 'lxml')
    tbody = soup.find_all("tbody")[tbody_index]
    tr_list = tbody.find_all("tr")

    for tr in tr_list:
        try:
            if td_check_index is not None:
                td_check = tr.find_all("td")[td_check_index].text.strip()
                if td_check == td_check_value:
                    url = tr.find_all("td")[td_index].find("a")["href"]
                    if "/wiki/" in url:
                        urls.append("https://fr.wikipedia.org" + url)
            else:
                url = tr.find_all("td")[td_index].find("a")["href"]
                if "/wiki/" in url:
                    urls.append("https://fr.wikipedia.org" + url)
        except:
            pass

def famicom():
    response = r.get(liens[1])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    for x in range(2,29):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            if " - J" not in (y.text):
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)

def GB():
    response = r.get(liens[2])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(2,28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            if " - J" not in (y.text):
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)

def GBC():
    response = r.get(liens[4])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(2,29):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)
def GC():
    response = r.get(liens[5])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(27):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)

def linux():
    response = r.get(liens[6])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(47):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)
            except:
                pass

def Master_System():
    response = r.get(liens[7])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(27):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def Mega_Drive():
    response = r.get(liens[8])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                if " - J" not in (y.text) or " - Ch" not in (y.text):
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def browser():
    response = r.get(liens[9])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(27):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def trois_DS():
    response = r.get(liens[10])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(29):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                url = y.find("a")["href"]
                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def N_six_quatre():
    response = r.get(liens[11])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                if " - J" not in (y.text) or " - AUS" not in (y.text):
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
    urls_2 = ["https://fr.wikipedia.org/wiki/Nintendo_64DD","https://fr.wikipedia.org/wiki/Japon","https://fr.wikipedia.org/wiki/Australie"]
    for x in urls_2:
        del urls[urls.index(x)]

def DS():
    response = r.get(liens[12])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(29):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
    del urls[urls.index("https://fr.wikipedia.org/wiki/Liste_de_jeux_DSiWare")]
    del urls[urls.index("https://fr.wikipedia.org/wiki/DSiWare")]
def NES():
    response = r.get(liens[13])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(27):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def switch():
    response = r.get(liens[14])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                if " - J" not in (y.text) or " - AN" not in (y.text):
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass

def get_urls(i, urls):
    response = r.get(liens[i])
    soup = bs(response.content, 'lxml')
    div = soup.find("div", {"class": "mw-parser-output"})
    test = div.find_all("ul")
    for x in range(len(test)):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                if i in [15, 16, 19]:
                    url = y.find("a")["href"]
                else:
                    if " - J" in y.text:
                        continue
                    url = y.find("a")["href"]

                if "/w/index.php?title=" not in url:
                    urls.append("https://fr.wikipedia.org" + url)
            except:
                pass

def PS_vita():
    response = r.get(liens[21])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                if " - J" not in (y.text):
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def Super_Famicom():
    response = r.get(liens[22])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                if " - J" not in (y.text):
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def SNES():
    response = r.get(liens[23])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/w/index.php?title=" not in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def Wii():
    response = r.get(liens[24])
    soup = bs(response.content, 'lxml')
    div = soup.find_all("tbody")[2]
    tr = div.find_all("tr")
    del tr[0]
    for x in tr:
        try:
            url = (x.find("td").find("a")["href"])
            if "/w/index.php?title=" not in url:
                urls.append("https://fr.wikipedia.org"+url)
        except:
            pass
url_windows = "https://fr.wikipedia.org/wiki/Liste_de_jeux_Windows_"
urls_windows = [url_windows + "(" + letter + ")" for letter in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
def PC():
    x = 0
    for url in urls_windows:
        response = r.get(url)
        soup = bs(response.content, 'lxml')
        div = soup.find("div",{"class":"mw-parser-output"})
        test = div.find_all("ul")
        while True:
            try:
                for y in test[x].find_all("li"):
                    lien = y.find("a")["href"]
                    if "/wiki/Liste" not in lien:
                        if "/wiki/" in lien:
                            urls.append("https://fr.wikipedia.org"+lien)
                x += 1
            except:
                break

    
def Xbox():
    response = r.get(liens[27])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(27):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/wiki/" in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def Xbox_trois_six():
    response = r.get(liens[28])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(36):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/wiki/" in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass

def Xbox_one():
    response = r.get(liens[29])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(28):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/wiki/" in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def Xbox_series():
    response = r.get(liens[30])
    soup = bs(response.content, 'lxml')
    div = soup.find("div",{"class":"mw-parser-output"})
    test = div.find_all("ul")
    for x in range(24):
        test = div.find_all("ul")[x].find_all("li")
        for y in test:
            try:
                    url = y.find("a")["href"]
                    if "/wiki/" in url:
                        urls.append("https://fr.wikipedia.org"+url)
            except:
                pass
def main():
    DS()
    GB()
    GBC()
    GC()
    Master_System()
    Mega_Drive()
    NES()
    N_six_quatre()
    PC()
    # PS1 à PS5
    for x in range(15,19+1):
        get_urls(x, urls)
    get_links(0, 2, 0, td_check_index=1, td_check_value="#bbbbff")  # Dreamcast
    get_links(3, 1, 0, 6, "✔\n")  # GBA
    get_links(20, 2, 0, td_check_index=1, td_check_value="#bbbbff")  # PSP
    get_links(25, 2, 0, 6, "NC")  # Wii U
    PS_vita()
    SNES()
    Super_Famicom()
    Wii()
    Xbox()
    Xbox_one()
    Xbox_series()
    Xbox_trois_six()

main()
urls = remove_duplicates(urls)
with open("urls.txt","w") as f:
    for x in urls:
        f.write(x+"\n")

urls = open("urls.txt","r").readlines()
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen

def scrap_data(lien):
    try:
        response = urlopen(lien)
        soup = bs(response.read(), 'lxml')
        titre = soup.find("head").find("title").text.replace(" — Wikipédia","")
        genre_element = soup.find('th', scope='row', text='Genre')
        genre = genre_element.find_next_sibling('td').text
        platforms_element = soup.find('th', scope='row', text='Plateforme')
        platforms = platforms_element.find_next_sibling('td').text
        jeu = [titre,platforms,genre,lien]
        for x in range(len(jeu)):
            jeu[x] = jeu[x].replace("\n","")
        jeux.append("#".join(jeu))
    except:
        pass

jeux = []
with ThreadPoolExecutor() as executor:
    urls.sort()
    for x in urls:
        lien = (x.replace("\n",""))
        executor.submit(scrap_data, lien)
end = time.time()
print(end-start)
